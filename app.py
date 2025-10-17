import os
from dotenv import load_dotenv
import streamlit as st

from google import genai
from google.genai import types

# =========================
# 1) SETUP & SAFE CLIENT
# =========================
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Gemini Chat", page_icon="✨")
st.title("✨ Gemini Chat (Streamlit)")

if not API_KEY:
    st.error("Set GEMINI_API_KEY (or GOOGLE_API_KEY) in your .env file.")
    st.stop()

@st.cache_resource
def get_gemini_client(api_key: str):
    # Cached for app lifetime: prevents the underlying HTTP client from being closed across reruns.
    return genai.Client(api_key=api_key)

client = get_gemini_client(API_KEY)

# =========================
# 2) SESSION STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "inflight" not in st.session_state:
    st.session_state.inflight = False  # True while we are streaming a model reply

# We'll store the current effective settings so we can detect changes
def _ensure_chat(model: str, system_prompt: str, temperature: float):
    """Create or (safely) recreate the chat session if settings changed and we're not inflight."""
    settings_changed = (
        st.session_state.get("model") != model
        or st.session_state.get("system_prompt") != system_prompt
        or st.session_state.get("temperature") != temperature
        or ("chat" not in st.session_state)
    )

    if settings_changed and not st.session_state.inflight:
        cfg = types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=temperature,
        )
        st.session_state.chat = client.chats.create(model=model, config=cfg)
        st.session_state.model = model
        st.session_state.system_prompt = system_prompt
        st.session_state.temperature = temperature

# =========================
# 3) SIDEBAR (DISABLE WHILE STREAMING)
# =========================
with st.sidebar:
    st.subheader("Settings")
    disabled = st.session_state.inflight  # lock controls during streaming

    model = st.selectbox(
        "Model",
        ["gemini-2.5-flash", "gemini-2.5-pro"],
        index=0,
        help="Flash is faster/cheaper, Pro is stronger.",
        disabled=disabled,
        key="ui_model",
    )
    system_prompt = st.text_area(
        "System instruction",
        value=st.session_state.get("system_prompt", "You are a helpful assistant."),
        help="Guides the assistant’s tone/behavior.",
        disabled=disabled,
        key="ui_sys",
    )
    temperature = st.slider(
        "Creativity (temperature)",
        0.0, 2.0, st.session_state.get("temperature", 1.0), 0.1,
        disabled=disabled,
        key="ui_temp",
    )

    col1, col2 = st.columns(2)
    with col1:
        reset_clicked = st.button("🔄 Reset chat", disabled=disabled)
    with col2:
        st.write("")  # spacer

    if reset_clicked and not st.session_state.inflight:
        st.session_state.clear()
        st.rerun()

# Create (or recreate) the chat if needed and safe
_ensure_chat(model=st.session_state.ui_model,
             system_prompt=st.session_state.ui_sys,
             temperature=st.session_state.ui_temp)

# If user changed settings mid-stream, let them know changes will apply next turn
if st.session_state.inflight:
    pending_change = (
        st.session_state.get("model") != st.session_state.ui_model
        or st.session_state.get("system_prompt") != st.session_state.ui_sys
        or st.session_state.get("temperature") != st.session_state.ui_temp
    )
    if pending_change:
        st.sidebar.info("Changes will apply after the current response finishes.")

# =========================
# 4) RENDER HISTORY
# =========================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# 5) CHAT INPUT & ROBUST STREAMING
# =========================
user_text = st.chat_input("Ask me anything…")
if user_text:
    # Show user bubble + persist
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # Stream model response in real-time with safe guards
    with st.chat_message("assistant"):
        def stream_once():
            # Use the currently active chat session
            for chunk in st.session_state.chat.send_message_stream(user_text):
                if getattr(chunk, "text", None):
                    yield chunk.text

        try:
            st.session_state.inflight = True
            full_text = st.write_stream(stream_once())
        except RuntimeError as e:
            # Graceful recovery if the underlying HTTP client was closed
            if "client has been closed" in str(e).lower():
                # Recreate the chat with the current UI settings and fall back to non-streaming
                cfg = types.GenerateContentConfig(
                    system_instruction=st.session_state.ui_sys,
                    temperature=st.session_state.ui_temp,
                )
                st.session_state.chat = client.chats.create(
                    model=st.session_state.ui_model,
                    config=cfg
                )
                resp = st.session_state.chat.send_message(user_text)
                full_text = resp.text
                st.write(full_text)
            else:
                # Unknown error—re-raise so Streamlit shows the traceback
                raise
        finally:
            st.session_state.inflight = False

    # Save assistant message so it appears on rerun
    st.session_state.messages.append({"role": "assistant", "content": full_text})
