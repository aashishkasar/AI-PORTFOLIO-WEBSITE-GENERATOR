import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import zipfile
import io

# ---------------- Page Config ----------------
st.set_page_config(page_title="AI Portfolio Generator", page_icon="💼")
st.title("AI Portfolio Website Generator")
st.write("Describe yourself and get a complete portfolio website (HTML + CSS + JS).")

# ---------------- Load API Key ----------------
load_dotenv()
api_key = os.getenv("GEM")

if not api_key:
    st.error("❌ Google API key not found. Please set GEM in .env file.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = api_key

# ---------------- User Input ----------------
user_prompt = st.text_area(
    "Describe yourself (name, role, experience, skills, projects, achievements):",
    height=220,
    placeholder="Example: I am a Data Scientist with 5+ years of experience in ML, NLP, Python..."
)

# ---------------- Model ----------------
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# ---------------- Prompt ----------------
system_prompt = """
You are a senior frontend developer and UI/UX designer.

Generate a COMPLETE, MODERN, PROFESSIONAL PORTFOLIO WEBSITE.

MANDATORY SECTIONS:
Hero, About, Skills, Experience, Projects, Achievements, Contact

IMPORTANT:
HTML MUST include:
<link rel="stylesheet" href="style.css">
<script src="script.js"></script>

STRICT OUTPUT FORMAT:

--html--
[HTML ONLY]
--html--

--css--
[CSS ONLY]
--css--

--js--
[JAVASCRIPT ONLY]
--js--

❌ No explanations
"""

# ---------------- Helpers ----------------
def extract_section(text, start, end):
    try:
        return text.split(start)[1].split(end)[0].strip()
    except Exception:
        return ""

def fix_html_links(html):
    if '<link rel="stylesheet"' not in html:
        html = html.replace(
            "</head>",
            '  <link rel="stylesheet" href="style.css">\n</head>'
        )

    if '<script src="script.js"' not in html:
        html = html.replace(
            "</body>",
            '  <script src="script.js"></script>\n</body>'
        )

    return html

# ---------------- Generate Website ----------------
if st.button("Generate Portfolio Website"):

    if not user_prompt.strip():
        st.error("❌ Please enter your details.")
        st.stop()

    with st.spinner("⏳ Generating your portfolio website..."):

        response = model.invoke([
            ("system", system_prompt),
            ("user", user_prompt)
        ]).content

        html_code = extract_section(response, "--html--", "--html--")
        css_code = extract_section(response, "--css--", "--css--")
        js_code = extract_section(response, "--js--", "--js--")

        if not html_code:
            st.error("❌ Failed to generate website.")
            st.code(response)
            st.stop()

        # ✅ Force correct file linking
        html_code = fix_html_links(html_code)

        # ---------------- Create ZIP in Memory ----------------
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr("index.html", html_code)
            zipf.writestr("style.css", css_code)
            zipf.writestr("script.js", js_code)

        zip_buffer.seek(0)

        # ---------------- Download ----------------
        st.download_button(
            label="⬇️ Download Portfolio Website",
            data=zip_buffer,
            file_name="portfolio_website.zip",
            mime="application/zip"
        )

    st.success("✅ Portfolio website generated successfully!")
    st.info("Unzip the files and open index.html in your browser.")
