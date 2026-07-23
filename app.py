import streamlit as st
import time
import base64
from groq import Groq

# ===========================================================
# ICON SYSTEM
# ===========================================================
_ICON_PATHS = {
    "sparkles": ("M12 2L13.8 9.2L21 11L13.8 12.8L12 20L10.2 12.8L3 11L10.2 9.2L12 2Z", "solid"),
    "settings": (
        '<circle cx="12" cy="12" r="3"/>'
        '<path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 '
        '1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 '
        '1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 '
        '9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 '
        '1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 '
        '1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>', "stroke_raw"
    ),
    "user": (
        '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>', "stroke_raw"
    ),
    "key": (
        '<circle cx="7.5" cy="15.5" r="4.5"/><path d="M10.6 12.4 19 4l3 3-2 2-2-2-2 2 2 2-2 2"/>', "stroke_raw"
    ),
    "chat": (
        '<path d="M21 11.5a8.4 8.4 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.4 8.4 0 0 1-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 0 1-.9-3.8 '
        '8.5 8.5 0 0 1 4.7-7.6 8.4 8.4 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>', "stroke_raw"
    ),
    "bar-chart": (
        '<line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/>',
        "stroke_raw"
    ),
}

def icon_svg(name: str, size: int = 18, color: str = "currentColor") -> str:
    body, kind = _ICON_PATHS[name]
    if kind == "solid":
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}"><path d="{body}"/></svg>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'

def icon_data_uri(name: str, size: int = 64, color: str = "%23D97706") -> str:
    body, kind = _ICON_PATHS[name]
    color_raw = color.replace("%23", "#")
    if kind == "solid":
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color_raw}"><path d="{body}"/></svg>'
    else:
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color_raw}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    return f"data:image/svg+xml;base64,{b64}"

def icon_label(name: str, text: str, size: int = 15, color: str = "#E8D5C4") -> str:
    return f'<span class="icon-inline">{icon_svg(name, size, color)}<span>{text}</span></span>'

# Avatar Premium Brown
ASSISTANT_AVATAR = icon_data_uri("sparkles", size=64, color="%23D97706") # Bronze
USER_AVATAR = icon_data_uri("user", size=64, color="%23FCD34D") # Gold
PAGE_ICON = icon_data_uri("sparkles", size=64, color="%23B45309")

# ===========================================================
# PAGE CONFIG & CUSTOM BROWN CSS
# ===========================================================
st.set_page_config(page_title="NexAI Workspace", page_icon=PAGE_ICON, layout="wide", initial_sidebar_state="expanded")
st.html("""
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
/* ---------- Global (Tema Espresso & Bronze) ---------- */
html, body, [class*="css"]  { font-family: 'Inter', sans-serif; }
h1, h2, h3, .app-title { font-family: 'Space Grotesk', sans-serif !important; }
.stApp {
    background: radial-gradient(circle at 15% 20%, #2b1b12 0%, #170d08 45%, #0a0604 100%);
    background-attachment: fixed;
    color: #F3EAE3;
}
#MainMenu, footer {visibility: hidden;}
.stDeployButton {display: none;}

/* ---------- Icon helpers ---------- */
.icon-inline { display: inline-flex; align-items: center; gap: 0.4rem; vertical-align: middle; }
.icon-inline svg { flex-shrink: 0; display: block; }

/* ---------- Hero header ---------- */
.hero {
    padding: 2.2rem 2.2rem 1.8rem 2.2rem;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(217,119,6,0.15), rgba(245,158,11,0.08));
    border: 1px solid rgba(217,119,6,0.15);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    margin-bottom: 1.6rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "";
    position: absolute;
    top: -60px; right: -60px;
    width: 220px; height: 220px;
    background: radial-gradient(circle, rgba(245,158,11,0.2), transparent 70%);
    border-radius: 50%;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 0.4rem; padding: 4px 12px;
    border-radius: 999px; background: rgba(255,255,255,0.05); border: 1px solid rgba(217,119,6,0.3);
    font-size: 0.75rem; letter-spacing: 0.06em; text-transform: uppercase; color: #E8D5C4; margin-bottom: 0.8rem;
}
.hero-title {
    font-size: 2.1rem; font-weight: 700;
    background: linear-gradient(90deg, #ffffff, #fcd34d 60%, #f59e0b);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0;
}
.hero-sub { color: #D1BFAe; font-size: 0.95rem; margin-top: 0.4rem; max-width: 640px; }

/* ---------- Glass cards ---------- */
.glass-card {
    background: rgba(25, 15, 10, 0.4); border: 1px solid rgba(217,119,6,0.15);
    border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(10px); box-shadow: 0 4px 24px rgba(0,0,0,0.25);
}

/* ---------- Metric pills ---------- */
.metric-row { display: flex; gap: 0.9rem; margin: 1rem 0 1.4rem 0; flex-wrap: wrap; }
.metric-pill {
    flex: 1; min-width: 140px;
    background: linear-gradient(145deg, rgba(217,119,6,0.12), rgba(245,158,11,0.05));
    border: 1px solid rgba(217,119,6,0.2); border-radius: 16px; padding: 0.9rem 1.1rem;
}
.metric-pill .label { font-size: 0.72rem; color: #D1BFAe; text-transform: uppercase; letter-spacing: 0.05em; }
.metric-pill .value { font-size: 1.5rem; font-weight: 700; color: #fff; font-family: 'Space Grotesk', sans-serif; }

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1c100b 0%, #0d0704 100%);
    border-right: 1px solid rgba(217,119,6,0.15);
}
section[data-testid="stSidebar"] .stTextInput input {
    background: rgba(255,255,255,0.05); border: 1px solid rgba(217,119,6,0.2); border-radius: 10px; color: #fff;
}
.sidebar-title { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 1.05rem; color: #fff; margin-bottom: 0.2rem; }
.sidebar-title svg { color: #D97706; }
.sidebar-caption { color: #A89B8D; font-size: 0.8rem; margin-bottom: 1.2rem; }

/* ---------- Chat bubbles ---------- */
[data-testid="stChatMessage"] {
    background: rgba(25, 15, 10, 0.4); border: 1px solid rgba(217,119,6,0.15);
    border-radius: 16px; padding: 0.4rem 0.6rem; margin-bottom: 0.6rem;
}
[data-testid="stChatInput"] textarea { background: rgba(255,255,255,0.05) !important; border-radius: 14px !important; color: #fff !important; }

/* ---------- Buttons ---------- */
.stButton>button {
    background: linear-gradient(90deg, #b45309, #d97706);
    color: white; border: none; border-radius: 12px; padding: 0.5rem 1.1rem; font-weight: 600;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(217,119,6,0.3); }

/* ---------- Divider ---------- */
.soft-divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(217,119,6,0.2), transparent); margin: 1.4rem 0; border: none; }
</style>
""")

# ===========================================================
# 3. SESSION STATE INIT 
# ===========================================================
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "username" not in st.session_state: st.session_state.username = ""
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "api_key" not in st.session_state: st.session_state.api_key = ""

# ===========================================================
# 4. HALAMAN LOGIN
# ===========================================================
def login_page():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown(f"""
        <div class="hero" style="text-align:center;">
            <span class="hero-badge">{icon_svg('key', 14, '#fcd34d')} Secure Auth</span>
            <p class="hero-title">NexAI Workspace</p>
            <p class="hero-sub" style="margin: 0 auto; margin-top: 10px;">Enterprise-Grade AI Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="admin")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("Masuk ke Dashboard", use_container_width=True)
            
            if submit:
                if username and password:
                    st.success("Verifikasi berhasil! Menyiapkan workspace...")
                    time.sleep(1)
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("⚠️ Username dan Password wajib diisi!")

# ===========================================================
# 5. HALAMAN DASHBOARD (SAAS UTAMA)
# ===========================================================
def dashboard_page():
    # --- SIDEBAR NAVIGASI ---
    with st.sidebar:
        st.markdown(f'<p class="sidebar-title">{icon_label("user", f"Halo, {st.session_state.username}")}</p>', unsafe_allow_html=True)
        st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)
        
        menu = st.radio("Navigasi Menu", ["📊 Overview", "⚡ NexAI Chat", "🔑 API Config"], label_visibility="collapsed")
        st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)
        
        st.markdown(f'<p class="sidebar-title">{icon_label("settings", "Chat Tools")}</p>', unsafe_allow_html=True)
        if st.button("🗑️ Bersihkan Obrolan", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
            
        st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)
        if st.button("🚪 Logout", use_container_width=True):
            for key in ["logged_in", "username", "chat_history", "api_key"]:
                st.session_state[key] = False if key == "logged_in" else ([] if key == "chat_history" else "")
            st.rerun()

    # --- KONTEN HALAMAN ---
    if menu == "📊 Overview":
        st.markdown(f"""
        <div class="hero">
            <span class="hero-badge">{icon_svg('bar-chart', 14, '#fcd34d')} Analytics</span>
            <p class="hero-title">Platform Dashboard</p>
            <p class="hero-sub">Ringkasan performa AI dan penggunaan token Anda bulan ini.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-row">
            <div class="metric-pill"><div class="label">Inferences</div><div class="value">12,492</div></div>
            <div class="metric-pill"><div class="label">System Uptime</div><div class="value">99.98%</div></div>
            <div class="metric-pill"><div class="label">Avg Latency</div><div class="value">180ms</div></div>
            <div class="metric-pill"><div class="label">Active Tokens</div><div class="value">2.1M</div></div>
        </div>
        """, unsafe_allow_html=True)
        
    elif menu == "⚡ NexAI Chat":
        st.markdown(f"""
        <div class="hero" style="padding: 1.5rem;">
            <span class="hero-badge">{icon_svg('sparkles', 14, '#fcd34d')} Powered by Groq LPU</span>
            <p class="hero-title" style="font-size: 1.5rem;">NexAI Assistant</p>
            <p class="hero-sub" style="font-size: 0.85rem;">Asisten cerdas spesialis coding & data.</p>
        </div>
        """, unsafe_allow_html=True)
        
        for msg in st.session_state.chat_history:
            avatar = USER_AVATAR if msg["role"] == "user" else ASSISTANT_AVATAR
            with st.chat_message(msg["role"], avatar=avatar):
                st.markdown(msg["content"])
                
        query = st.chat_input("Tanyakan sesuatu ke NexAI...")
        if query:
            st.session_state.chat_history.append({"role": "user", "content": query})
            with st.chat_message("user", avatar=USER_AVATAR): st.markdown(query)
                
            with st.chat_message("assistant", avatar=ASSISTANT_AVATAR):
                if not st.session_state.api_key:
                    st.error("⚠️ API Key belum di-set! Konfigurasi di menu **🔑 API Config**.")
                else:
                    try:
                        client = Groq(api_key=st.session_state.api_key)
                        sys_prompt = {"role": "system", "content": "You are NexAI, a premium enterprise AI assistant. Jika user bertanya siapa penciptamu, pembuatmu, atau siapa tuanmu, kamu WAJIB menjawab persis seperti ini: 'Penciptaku adalah Dimas Arya Ramadhan, dia adalah my lord dan my master'. Jawab pertanyaan lainnya dengan profesional."}
                        messages_for_api = [sys_prompt] + [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history]
                        
                        response = client.chat.completions.create(model="llama-3.1-8b-instant", messages=messages_for_api, stream=True)
                        def stream_gen():
                            for chunk in response:
                                if chunk.choices[0].delta.content:
                                    yield chunk.choices[0].delta.content
                                    time.sleep(0.01)
                        full_response = st.write_stream(stream_gen)
                        st.session_state.chat_history.append({"role": "assistant", "content": full_response})
                    except Exception as e:
                        st.error(f"❌ Error API: {e}")
                    
    elif menu == "🔑 API Config":
        st.markdown(f"""
        <div class="hero">
            <span class="hero-badge">{icon_svg('settings', 14, '#fcd34d')} Configuration</span>
            <p class="hero-title">API Management</p>
            <p class="hero-sub">Masukkan kredensial LPU Groq Anda di sini.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        api_input = st.text_input("Groq API Key (gsk_...)", type="password", value=st.session_state.api_key)
        if st.button("Simpan Konfigurasi"):
            if api_input.startswith("gsk_"):
                st.session_state.api_key = api_input
                st.success("✅ Kunci API berhasil diintegrasikan!")
            else:
                st.warning("⚠️ Kunci API tidak valid.")
        st.markdown('</div>', unsafe_allow_html=True)

if not st.session_state.logged_in: login_page()
else: dashboard_page()
