# 🚀 Manual GitHub Deployment Guide for Ashish2143

## Your GitHub Account
- **Username:** Ashish2143
- **Email:** ashisharsad9307@gmail.com
- **Repository:** https://github.com/Ashish2143/ai-code-review

---

## ⚠️ Git Not Available - Here's What To Do

### Option 1: Download Git Installer (Recommended)
1. Go to: https://git-scm.com/download/win
2. Download the latest Git for Windows
3. Run the installer and accept defaults
4. **Restart PowerShell** after installation
5. Then run the commands below

### Option 2: Use GitHub Desktop
1. Download: https://desktop.github.com/
2. Sign in with your GitHub account (Ashish2143)
3. Clone or create repository
4. Drag your project files into it
5. Commit and push

### Option 3: Use Visual Studio Code
1. Open VS Code
2. Install "GitHub Pull Requests and Issues" extension
3. Open your project folder
4. Use Source Control panel to commit and push

---

## Commands To Run (After Git Install)

### In PowerShell:
```powershell
cd d:\PROJECT\ai-code-review

git init

git config --global user.name "Ashish2143"
git config --global user.email "ashisharsad9307@gmail.com"

git add .

git commit -m "Initial commit: AI Code Review System with 10-language support, dark mode, and real-time analysis"

git remote add origin https://github.com/Ashish2143/ai-code-review.git

git branch -M main

git push -u origin main
```

When prompted for credentials:
- **Username:** Ashish2143
- **Password:** Use Personal Access Token
  - Create at: https://github.com/settings/tokens
  - Scope: repo, workflow
  - Copy token and paste as password

---

## Step-by-Step Process

### 1. Create Repository on GitHub
- Go to: https://github.com/new
- Name: `ai-code-review`
- Description: `AI Code Review System - Multi-Language Code Analyzer`
- Public
- Create without README

### 2. Install Git
- Download from: https://git-scm.com/download/win
- Run installer
- Restart PowerShell

### 3. Run Commands Above
- Copy all commands
- Paste into PowerShell
- Follow prompts

### 4. Verify
- Go to: https://github.com/Ashish2143/ai-code-review
- Check all files are there
- Done! ✅

---

## Files Being Uploaded (~30 files)

✅ Frontend: index.html (900+ lines)
✅ Backend: main.py, analyzer.py, multilang_analyzer.py, model.py
✅ ML: train.py
✅ Docs: README.md, DEPLOY.md, other guides
✅ Config: requirements.txt

❌ Not uploaded (Git ignores):
- __pycache__/
- .venv/
- .env
- *.pyc

---

## Need Help?

**Git Installation Issues:**
- https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- Try GitHub Desktop instead: https://desktop.github.com/

**GitHub Help:**
- https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories

**Token Help:**
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

---

## Quick Checklist

- [ ] GitHub account created (done - Ashish2143)
- [ ] Repository created on GitHub
- [ ] Git installed and working
- [ ] Configured with your name and email
- [ ] All files added (git add .)
- [ ] Commit created with message
- [ ] Remote added (git remote add origin)
- [ ] Branch renamed to main
- [ ] Pushed to GitHub (git push -u origin main)
- [ ] Verified on GitHub website

---

**Once Git is installed, come back and run the commands above! 🚀**
