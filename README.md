<p align="center">
  <img src="https://github.com/Scorpian-my/Time-Profile/raw/main/assets/banner.gif" alt="Time Profile Banner" width="700"/>
</p>

<h1 align="center">⏰ Time-Profile</h1>

<p align="center">
  <b>Dynamic Telegram Profile Updater</b>  
  <br>
  <i>Automatically updates your profile picture and bio with the current time</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/telethon-1.30+-blueviolet?logo=telegram">
  <img src="https://img.shields.io/github/stars/Scorpian-my/Time-Profile?style=social">
</p>

---

## ✨ Features

- 🖼 Dynamic **profile picture** with current time
- 🧠 Updates **bio** with styled time every minute
- 🎨 Beautiful image backgrounds & custom fonts
- 🌐 Localized to **Asia/Tehran timezone**
- 💻 Fully customizable and open-source

---

## 🖥 Demo

<p align="center">
  <img src="https://github.com/Scorpian-my/Time-Profile/data/sample1.jpg" width="500"/>
</p>

---

## ⚙️ Requirements

```bash
pip install telethon pillow pytz
```

---

## 🚀 Getting Started

1. Get your **API ID** and **API Hash** from [my.telegram.org](https://my.telegram.org).

2. Open the script and insert them:

```python
api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"
```

3. Run the bot:

```bash
python Time-Profile.py
```

> On first run, Telegram will ask for your phone number and login code.

---

## 🖌 Customization

- Change background images in the `photos/` folder  
- Replace font with your own in `data/3.ttf`  
- Edit the base bio here:

```python
bio = "Desires do not die before God | Time:"
```

---

## 📂 Project Structure

```
Time-Profile/
├── photos/         ← Background images
├── data/
│   ├── 3.ttf       ← Font file
│   └── Time.jpg    ← Generated profile image
├── Time-Profile.py
└── README.md
```

---

## 🙋‍♂️ Author

Made with ❤️ by [@Dev_Scorpian](https://t.me/Dev_Scorpian)

> Telegram bot dev? Let's connect and build cool stuff!

---

## ⚠️ Disclaimer

This script uses official Telegram API via Telethon.  
Avoid using it with spammy accounts. Run responsibly.

---

## ⭐️ Show Some Love

If you like it, give it a ⭐️ on GitHub and share it with others!

