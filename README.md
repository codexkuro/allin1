<p align="center">
  <img src="https://img.shields.io/badge/Author-codexkuro-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
</p>

# allin1 - Command Memory Tool for Cyber Security

**allin1** is a lightweight CLI tool designed to solve the common problem of forgetting complex cybersecurity commands (like `nmap`, `msfvenom`, etc.). Instead of scrolling through `history`, just save it once and run it anytime!

## ✨ Key Features
- **CRUD Operations**: Save, List, Search, and Delete commands easily.
- **Variables Support**: Save commands like `nmap <target>` and the tool will prompt for the value.
- **Secure Execution**: Built-in protection against command injection using `subprocess`.
- **Interactive UI**: Clean and colorful terminal interface.

## ⚙️ Installation

```bash
```
1. **Clone the repo**
   git clone [https://github.com/codexkuro/allin1.git](https://github.com/codexkuro/allin1.git)
   cd allin1

2. Setup Virtual Environment
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the App
   python src/main.py

Made with ❤️ by codexkuro
