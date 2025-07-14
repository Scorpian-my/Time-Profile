# ⏰ Time-Profile

**Time-Profile** is a Telegram automation script built with [Telethon](https://github.com/LonamiWebs/Telethon). It updates your **Telegram profile photo** and **bio** every minute with the current time, beautifully rendered on a custom background image.

---

## 📌 Features

- Automatically updates your **profile photo** every minute with a time-based image.
- Updates your **bio** with the current time using special font characters.
- Customizable background images, fonts, and bio text.
- Lightweight and runs continuously.

---

## 📷 Example Output

> A centered image with the current time rendered over it  
> *(You can add your own sample image at `data/sample_output.jpg`)*

---

## ⚙️ Requirements

- Python 3.7+
- Install required libraries:

```bash
pip install telethon pillow pytz
```

---

## 🚀 Getting Started

1. Go to [my.telegram.org](https://my.telegram.org) and obtain your **API ID** and **API Hash**.
2. Open `Time-Profile.py` and fill in the following:

```python
api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"
```

3. Run the script:

```bash
python Time-Profile.py
```

- On the first run, it will ask for your phone number and verification code.
- After that, it updates your profile picture and bio every minute with the current time.

---

## 🖼 Customization

- Background images are located in the `photos/` folder. You can add or replace them with your own.
- The font used for drawing the time is located in `data/3.ttf`.
- The base bio text can be edited in this line:

```python
bio = "Desires do not die before God | Time:"
```

---

## 📁 Project Structure

```
Time-Profile/
├── photos/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
├── data/
│   ├── 3.ttf
│   └── Time.jpg (generated image)
├── Time-Profile.py
└── README.md
```

---

## 👤 Author

Created by [@Dev_Scorpian](https://t.me/Dev_Scorpian)

---

## ⚠️ Disclaimer

- Use this script responsibly.
- Telegram may restrict accounts that perform frequent automated actions. Use at your own risk.
- This script uses official Telegram API methods and does not send any messages.

---
