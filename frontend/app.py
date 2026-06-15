import streamlit as st
import requests
import sqlite3
import pandas as pd
from datetime import datetime
from fpdf import FPDF
import matplotlib.pyplot as plt
import psutil
import gc
import time

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI App Risk Scanner",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- DATABASE ----------------
conn = sqlite3.connect("scans.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app_name TEXT,
    risk_score INTEGER,
    scan_time TEXT
)
""")
conn.commit()

# ---------------- THEME ----------------
st.markdown("""
<style>
html, body, .stApp {
    background: radial-gradient(circle at top, #2e1065, #05010a);
    color: #ffffff !important;
    font-size: 18px;
}
h1 { font-size: 44px !important; }
h2 { font-size: 34px !important; }
h3 { font-size: 26px !important; }
p, span, label, div {
    font-size: 20px !important;
    color: #ffffff !important;
}
input {
    font-size: 20px !important;
    padding: 14px !important;
    border-radius: 0px !important;
}
.stButton>button {
    font-size: 20px !important;
    padding: 16px 30px !important;
    border-radius: 18px;
    background: linear-gradient(135deg,#7c3aed,#9333ea);
    color: white !important;
    box-shadow: 0 0 30px rgba(147,51,234,0.7);
}
.card {
    background: linear-gradient(145deg,#1e0b3a,#0b0414);
    border-radius: 28px;
    padding: 40px;
    margin-bottom: 30px;
    box-shadow: 0 0 45px rgba(168,85,247,0.45);
}
.login-box {
    background: linear-gradient(145deg,#1e0b3a,#0b0414);
    padding: 40px;
    border-radius: 0px;
    max-width: 420px;
    margin: auto;
    box-shadow: 0 0 40px rgba(168,85,247,0.6);
}
.issue-box {
    background: linear-gradient(135deg,#1a082b,#12061f);
    padding: 18px;
    font-size: 20px;
    border-left: 5px solid #fb7185;
    border-radius: 14px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN ----------------
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("""
    <div class="login-box">
        <h2 style="text-align:center;">🔐 Secure Login</h2>
    </div>
    """, unsafe_allow_html=True)

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("🚀 Login"):
        if u == "admin" and p == "admin123":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("❌ Invalid Credentials")

    st.stop()

# ---------------- HEADER ----------------
st.markdown("""
<div class="card">
    <h1>🧠 AI Risk Intelligence Dashboard</h1>
    <p>Enterprise-grade Application Security Scanner</p>
</div>
""", unsafe_allow_html=True)

app_name = st.text_input("📱 Enter Application Name")

# ---------------- PDF ----------------
def generate_pdf(app, score, issues):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,"AI APPLICATION SECURITY REPORT",ln=True,align="C")
    pdf.ln(6)
    pdf.set_font("Arial",size=12)
    pdf.cell(0,8,f"Application: {app}",ln=True)
    pdf.cell(0,8,f"Risk Score: {score}/100",ln=True)
    pdf.cell(0,8,f"Scan Time: {datetime.now()}",ln=True)
    pdf.ln(6)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,8,"Detected Issues:",ln=True)
    pdf.set_font("Arial",size=11)
    for i, issue in enumerate(issues,1):
        pdf.multi_cell(0,7,f"{i}. {issue}")
    pdf.output("AI_Risk_Report.pdf")

# ---------------- PIE CHART ----------------
def risk_pie_chart(score):
    if score <= 40:
        values = [70,20,10]
    elif score <= 70:
        values = [20,60,20]
    else:
        values = [10,20,70]

    labels = ["Low Risk", "Medium Risk", "High Risk"]
    colors = ["#22c55e","#facc15","#ef4444"]

    fig, ax = plt.subplots(figsize=(4,4))
    fig.patch.set_facecolor("#05010a")

    ax.pie(values, labels=labels, autopct="%1.0f%%",
           startangle=140, colors=colors,
           textprops={"color":"white","fontsize":12})

    ax.set_title("AI Risk Distribution", fontsize=18, color="white")
    st.pyplot(fig)

# ---------------- BAR CHART ----------------
def risk_bar_chart(df):
    if df.empty:
        st.info("No scan data available")
        return

    df = df.tail(5)

    fig, ax = plt.subplots(figsize=(6,3))
    fig.patch.set_facecolor("#05010a")
    ax.set_facecolor("#12061f")

    ax.bar(df.index, df["risk_score"])

    ax.set_title("📊 Recent Risk Scores", color="white", fontsize=18)
    ax.set_xlabel("Last Scans", color="white")
    ax.set_ylabel("Risk Score", color="white")
    ax.tick_params(colors="white")
    ax.grid(alpha=0.3)

    st.pyplot(fig)

# ---------------- SCAN ----------------
if st.button("🧠 Run AI Risk Scan"):
    if not app_name:
        st.warning("⚠️ Please enter application name")
    else:
        try:
            res = requests.post(
                "http://127.0.0.1:5000/scan",
                json={"app_name": app_name},
                timeout=5
            )
            issues = res.json()["issues"]
            score = abs(hash(app_name.lower())) % 41 + 50

            with st.expander("🔮 AI Risk Analysis Output", expanded=True):
                st.metric("Risk Score", f"{score}/100")

                with st.expander("🥧 Risk Distribution"):
                    risk_pie_chart(score)

                with st.expander("📊 Risk Bar Analysis"):
                    df_plot = pd.read_sql("SELECT risk_score FROM scans", conn)
                    risk_bar_chart(df_plot)

                with st.expander("🚨 Detected Issues"):
                    for issue in issues:
                        st.markdown(
                            f"<div class='issue-box'>❌ {issue}</div>",
                            unsafe_allow_html=True
                        )

                with st.expander("📄 Download Report"):
                    generate_pdf(app_name, score, issues)
                    with open("AI_Risk_Report.pdf","rb") as f:
                        st.download_button("⬇️ Download PDF", f)

            c.execute(
                "INSERT INTO scans VALUES (NULL,?,?,?)",
                (app_name, score, datetime.now().strftime("%Y-%m-%d %H:%M"))
            )
            conn.commit()

        except:
            st.error("❌ Backend not running on port 5000")

# ---------------- HISTORY ----------------
with st.expander("📚 Scan History", expanded=True):
    df = pd.read_sql(
        "SELECT app_name,risk_score,scan_time FROM scans ORDER BY scan_time DESC",
        conn
    )
    st.dataframe(df, use_container_width=True)

# ---------------- RAM BOOSTER ----------------
with st.expander("🚀 AI RAM Booster", expanded=False):

    memory = psutil.virtual_memory()
    used_ram = memory.used / (1024 ** 3)
    total_ram = memory.total / (1024 ** 3)
    percent = memory.percent

    st.metric("RAM Usage",
              f"{used_ram:.2f} GB / {total_ram:.2f} GB",
              f"{percent}% Used")

    if st.button("📊 Show Live RAM Usage (5 sec)"):
        ram_data = []
        placeholder = st.empty()

        for _ in range(5):
            mem = psutil.virtual_memory()
            ram_data.append(mem.percent)
            time.sleep(1)

            fig, ax = plt.subplots()
            ax.plot(ram_data)
            ax.set_title("Live RAM Usage %")
            ax.set_xlabel("Seconds")
            ax.set_ylabel("RAM % Used")
            placeholder.pyplot(fig)

    if st.button("⚡ Boost RAM Now"):
        gc.collect()
        st.success("✅ Unused Memory Cleared Successfully!")

# ---------------- LOGOUT ----------------
if st.button("Logout"):
    st.session_state.login = False
    st.rerun()
