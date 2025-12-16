# 🤖 AI Portfolio Website Generator

### (Streamlit + LangChain + Google Gemini)

This project is a **Streamlit-based Generative AI application** that creates a **complete professional portfolio website** (HTML, CSS, JavaScript) using **Google Gemini via LangChain**, based on a user’s self-description.

The generated website is automatically packaged into a **ZIP file**, making it easy to download, deploy, or host.

---

## 🚀 Features

* 🧠 AI-generated portfolio using **Google Gemini**
* 🎨 Modern, professional frontend structure
* 📁 Generates **HTML + CSS + JavaScript**
* 📦 Auto-generated **ZIP download**
* ⚡ Simple & interactive **Streamlit UI**
* 🔐 Secure API key handling using **dotenv**
* 💼 Interview-ready GenAI project

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Google Gemini**
* **python-dotenv**
* **zipfile**
* **io**

---

## 📂 Project Structure

```
ai-portfolio-generator/
│
├── app.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🔐 Environment Variables (dotenv)

### What is `dotenv`?

`python-dotenv` allows you to store **sensitive information** (like API keys) in a `.env` file instead of hard-coding them into your source code.

---

### Why do we use `dotenv`?

* ✅ Keeps API keys **secure**
* ✅ Prevents accidental exposure on GitHub
* ✅ Makes environment configuration easy
* ✅ Industry best practice

---

### `.env` File Example

```
GEM=your_google_gemini_api_key_here
```

---

### Code Usage

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEM")
```

---

## 🚫 Why We Use `.gitignore`

`.gitignore` tells Git **which files should NOT be pushed to GitHub**.

### Why is it important?

* ❌ Prevents API key leakage
* ❌ Avoids pushing virtual environments
* ❌ Keeps the repository clean and professional

### Example `.gitignore`

```
.env
hug/
__pycache__/
*.pyc
```

---

## 🧩 Libraries Used – Step-by-Step Explanation

### 1️⃣ Streamlit

```python
import streamlit as st
```

**Why Streamlit?**

* Build web apps using only Python
* No frontend knowledge required
* Ideal for ML & GenAI applications

**Used for:**

* User input (text area)
* Buttons & messages
* Spinner during AI generation
* Download button for ZIP file

---

### 2️⃣ LangChain + Google Gemini

```python
from langchain_google_genai import ChatGoogleGenerativeAI
```

**Why LangChain?**

* Acts as a **client** for LLMs
* Simplifies prompt handling
* Standard interface for different LLM providers

**Why Google Gemini?**

* Closed-source, powerful LLM
* Excellent at structured code generation

```python
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)
```

---

### 3️⃣ System Prompt (Very Important)

```python
system_prompt = """
You are a senior frontend developer and UI/UX designer.
Generate a COMPLETE portfolio website.
STRICT OUTPUT FORMAT:
--html-- ... --html--
--css-- ... --css--
--js-- ... --js--
"""
```

**Purpose:**

* Controls AI behavior
* Forces structured output
* Prevents explanations or extra text
* Ensures clean file separation

---

### 4️⃣ Extracting HTML, CSS & JavaScript

```python
def extract_section(text, start, end):
    return text.split(start)[1].split(end)[0].strip()
```

**Why this is required?**

* Gemini returns everything in one response
* We extract each section to create separate files

---

### 5️⃣ Fixing HTML File Links

```python
def fix_html_links(html):
    if '<link rel="stylesheet"' not in html:
        html = html.replace("</head>",
            '<link rel="stylesheet" href="style.css"></head>'
        )
```

**Why this step?**

* AI may forget linking CSS or JS
* Ensures `style.css` and `script.js` load correctly

---

### 6️⃣ `zipfile` – Creating ZIP Files

```python
import zipfile
```

**Why `zipfile`?**

* Packages all website files into one ZIP
* Makes download and deployment easy

```python
with zipfile.ZipFile(zip_buffer, "w") as zipf:
    zipf.writestr("index.html", html_code)
```

---

### 7️⃣ `io.BytesIO` – In-Memory File Handling

```python
import io
```

**Why `io`?**

* Creates files in memory
* No need to save files on disk
* Faster and cleaner approach

```python
zip_buffer = io.BytesIO()
```

---

### 8️⃣ Download Button

```python
st.download_button(
    label="⬇️ Download Portfolio Website",
    data=zip_buffer,
    file_name="portfolio_website.zip",
    mime="application/zip"
)
```

Allows users to download the generated website instantly.

---

## ▶️ Application Flow (How It Works)

1. User enters personal details
2. Prompt is sent to Gemini via LangChain
3. AI generates HTML, CSS & JS
4. Code is extracted and validated
5. Files are zipped in memory
6. ZIP file is downloaded by the user

---

## 🐍 How to Create a Python Virtual Environment

Virtual environments isolate project dependencies and avoid version conflicts.

### 🔹 Step 1: Create Virtual Environment

```bash
python -m venv hug
```

* `venv` → Python virtual environment tool
* `hug` → Environment folder name

---

### 🔹 Step 2: Activate Virtual Environment (Windows)

```bash
cd hug
cd Scripts
activate
```

You should see:

```
(hug) C:\project>
```

---

### 🔹 Step 3: Install Required Libraries

```bash
pip install -r req.txt
```

* Installs all dependencies
* Ensures same versions for all developers

---

## 🧾 Why Virtual Environment Is Important?

* Prevents dependency conflicts
* Keeps global Python clean
* Makes deployment easier
* Industry best practice

---

## 🧑‍💻 Git Configuration (One-Time Setup)

```bash
git config --global user.name "Virat"
git config --global user.email "your_email@gmail.com"
```

This information appears in commit history.

---

## 📁 Track Hidden Files

```bash
ls -a
```

Shows hidden files like `.git`, `.env`, `.gitignore`.

---

## 🧠 Initialize Git Repository

```bash
git init
```

* Creates hidden `.git` folder
* Converts project into a Git repository

---

## 📤 How to Push Code to GitHub

### 🔹 Step 1: Add Files

```bash
git add .
```

---

### 🔹 Step 2: Commit Changes

```bash
git commit -m "Created AI portfolio generator"
```

If new changes appear, repeat:

```bash
git add .
git commit -m "Updated code"
```

---

### 🔹 Step 3: Add Remote Repository

```bash
git remote add origin <repository_link>
```

Example:

```bash
git remote add origin https://github.com/username/project-name.git
```

---

### 🔹 Step 4: Push Code

```bash
git push origin main
```

---

## 📦 Installation & Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎯 Use Cases

* Portfolio website generation
* Resume websites
* GenAI frontend automation
* LangChain + Gemini demos
* Interview & capstone projects

---

Perfect 👍
Below is a **clean, standard MIT License section** you can **directly append at the end of your `README.md`**, plus the **separate `LICENSE` file content** (industry best practice).

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to:

* ✔️ Use the code for personal or commercial projects
* ✔️ Modify and distribute the code
* ✔️ Include it in private or public repositories

**Condition:**
You must include the original copyright and license notice.

---


```text
MIT License

Copyright (c) 2025 Aashish K

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---



