# **YouTube Subscription Transfer Tool** 🚀  
Easily transfer YouTube subscriptions from one account to another using the **YouTube Data API v3** and **Google OAuth 2.0**.  

## **📌 Features**  
✅ Fetch all subscriptions from a **source YouTube account**  
✅ Subscribe to the same channels on a **target YouTube account**  
✅ Uses **Google OAuth 2.0** for authentication  
✅ Handles API rate limits and errors  
✅ Fully **automated** process  

---


## **📌 Installation**  
1️⃣ Install the Required Tools
✅ Install Python (if you haven’t already)
Download Python from the official website: https://www.python.org/downloads/

Install it, making sure to check the box "Add Python to environment variables" during installation.
<img src="https://github.com/user-attachments/assets/a0c2d411-55ad-4dff-953c-9c0388fb2e28" width="400">

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

---

2️⃣ Get Google API Credentials
✅ Create API Credentials on Google Cloud
1. Go to Google Cloud Console (https://console.cloud.google.com)
2. Click "Select A Project" at the top-left corner
3. Name your project anything that you want Ex: YouTube Subscription Transfer Tool (Note: DO NOT CHANGE ANYTHING ON THE LOCATION)
4. After creating your project, make sure to select it
5. Open the Navigation Bar at the top-left corner and open APIs & Services > Enabled APIs & Services
6. Click the + icon with the label "Enable APIs & Services" and search "Youtube Data API v3" (If you can't find it: https://console.cloud.google.com/apis/library/youtube.googleapis.com)
7. Enable the YouTube Data API v3
8. After Enabling it, open OAuth Consent Screen > Clients
9. Click "Get Started" and fill in the informations
10. Choose External and add your Contact Info Email and click Finish
11. On Metrics, Click "Create OAuth Client" > Choose "Desktop App" > Name it with anything that you like and Click "Create"
12. Now, navigate to "Audience" and Add Users with your Source Account Email and Target Account Email to gain permissioon
13. Download OAuth Client and name it "client_secrets.json" 
14. Move this file into the YouTube-Subscription-Transfer folder

---

3️⃣ Run the YouTube Subscription Transfer Script
1. Open Command Prompt (cmd) / PowerShell
2. Navigate to the Project Folder:
```sh
cd path\to\your\YouTube-Subscription-Transfer
```
3. Run the Script:
```sh
python transfer_subscriptions.py
```

---


4️⃣ Authenticate the YouTube Accounts

✅ Step 1: Authenticate Source Account
1. The script will open a browser window asking you to log into the source YouTube account (the one with subscriptions).
2. Grant the necessary permissions.
The script will fetch all subscriptions.

✅ Step 2: Authenticate Target Account
1. Once the source account is authenticated, the script will ask you to log into the target YouTube account.
2. Grant the permissions again.
3. The script will start subscribing to the same channels automatically.


---


5️⃣ Wait for Completion & Verify
The script will show progress messages:
```sh
🔵 Authenticating Source Account...
📥 Fetching subscriptions...
🔴 Authenticate Target Account...
📤 Subscribing to channels...
✅ Transfer Complete!
```
Once done, open YouTube on the target account and check the subscriptions.
🎯 Done! Your YouTube subscriptions have now been successfully transferred to the new account. 🎉
