# 🚀 GitHub Deployment Guide

## 4 Simple Steps to Deploy Your AI Code Review System

### STEP 1: Create GitHub Repository (2 minutes)
1. Go to https://github.com/new
2. **Repository name:** `ai-code-review`
3. **Description:** AI Code Review System - Multi-Language Code Analyzer
4. Choose **Public**
5. **DO NOT** initialize with README
6. Click **Create repository**

After creation, GitHub will show you commands. Copy your repository URL:
```
https://github.com/YOUR-USERNAME/ai-code-review.git
```

---

### STEP 2: Configure Git (First Time Only)

Run these commands:
```powershell
git config --global user.name "Ashish P. Arsad"
git config --global user.email "your-email@example.com"
```

---

### STEP 3: Deploy Your Project

Copy and paste these commands in PowerShell:

```powershell
cd d:\PROJECT\ai-code-review

git init

git add .

git commit -m "Initial commit: AI Code Review System with 10-language support, dark mode, and real-time analysis"

git remote add origin https://github.com/YOUR-USERNAME/ai-code-review.git

git branch -M main

git push -u origin main
```

**Replace `YOUR-USERNAME` with your actual GitHub username!**

When prompted for password:
- Use your GitHub password, OR
- Use a Personal Access Token (create at: https://github.com/settings/tokens)

---

### STEP 4: Verify on GitHub (1 minute)

1. Go to: `https://github.com/YOUR-USERNAME/ai-code-review`
2. Check that all files are there
3. Verify README displays
4. Done! 🎉

---

## Quick Reference

**Project Structure:**
```
ai-code-review/
├── frontend/index.html          (UI)
├── backend/main.py              (Server)
├── backend/analyzer.py          (Analyzer)
├── backend/multilang_analyzer.py (10 languages)
├── backend/model.py             (ML)
├── ml/train.py                  (Training)
├── README.md                    (Docs)
└── requirements.txt             (Dependencies)
```

**What Gets Uploaded:** ~25-30 files (source code + docs)
**What Doesn't:** __pycache__, .venv, .env files (git ignores them)
**Total Time:** ~7 minutes

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Git not found | Install from https://git-scm.com |
| Auth failed | Use Personal Access Token instead of password |
| Wrong remote URL | Run: `git remote set-url origin [NEW-URL]` |

---

**Ready? Start with STEP 1 above! 🚀**
