![2](https://github.com/user-attachments/assets/6e4f171e-a401-4b6d-8edd-a5d01698f75a)# **YouTube Subscription Transfer Tool** 🚀  
Easily transfer YouTube subscriptions from one account to another using the **YouTube Data API v3** and **Google OAuth 2.0**.  

## **📌 Features**  
✅ Fetch all subscriptions from a **source YouTube account**  
✅ Subscribe to the same channels on a **target YouTube account**  
✅ Uses **Google OAuth 2.0** for authentication  
✅ Handles API rate limits and errors  
✅ Fully **automated** process  

---

1️⃣ Install the Required Tools
✅ Install Python (if you haven’t already)
Download Python from the official website: https://www.python.org/downloads/
Install it, making sure to check the box "Add Python to PATH" during installation.
Open Command Prompt (cmd) or PowerShell and type:
```sh
python --version
```

✅ Install Required Python Libraries
1. Open Command Prompt (cmd) / PowerShell.
2. Navigate to the folder where the script is stored using cd (Change Directory):
```sh
cd path\to\your\YouTube-Subscription-Transfer
```
3. pip install -r requirements.txt
```sh
pip install -r requirements.txt
```

2️⃣ Get Google API Credentials
✅ Create API Credentials on Google Cloud
1. Go to Google Cloud Console (https://console.cloud.google.com)
2. Create a new project
   ![1](https://github.com/user-attachments/assets/da2832b7-5927-4fb3-a7ea-8d4ebd2ce2e5)
   ![2](https://github.com/user-attachments/assets/c7fe3bc8-6891-4686-b8cf-7831ff14b831)

   
   
4. Enable the YouTube Data API v3


5. Go to APIs & Services > Credentials
6. Click Create Credentials → Select OAuth Client ID
7. Choose Desktop App and create it
8. Download the client_secrets.json file
9. Move this file into the YouTube-Subscription-Transfer folder

