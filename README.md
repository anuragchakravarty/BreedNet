# 📁 How to Create a Folder in GitHub

Creating folders in GitHub is slightly different from your local system.  
GitHub does **not support empty folders**, so you must create at least one file inside the folder.

---

## 🚀 Method 1: Create Folder Directly on GitHub (Easy Way)

1. Open your repository on GitHub  
2. Click on **"Add file" → "Create new file"**  
3. In the filename field, type:

   folder-name/file-name

   👉 Example:  
   backend/main.py

4. Add some content (even a single line is enough)  
5. Scroll down and click **"Commit new file"**

✅ This will automatically create the folder with the file inside.

---

## 📤 Method 2: Upload Folder from Your System

1. Click on **"Add file" → "Upload files"**  
2. Drag and drop your folder from your computer  
3. Click **"Commit changes"**

✅ Your folder and all files inside it will be uploaded.

---

## 💻 Method 3: Using Git Commands (Recommended for Developers)

Create folder locally:

```bash
mkdir backend
cd backend
touch main.py
