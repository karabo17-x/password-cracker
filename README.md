# 🔐 Password Cracker CLI

A modular Python CLI tool that simulates how real-world attacks crack passwords using:

- 📖 Dictionary attacks  
- 🔁 Brute-force attacks  
- ⚡ Hybrid attacks (smart mutations)

Built for **learning, experimentation, and cybersecurity practice**.

---

## 🚀 Features

- 🔍 **Hash Support**
  - MD5
  - SHA1
  - SHA256
  - SHA512
  - bcrypt
  - Auto-detection

- ⚔️ **Attack Modes**
  - Dictionary (fast & efficient)
  - Brute-force (guaranteed but slower)
  - Hybrid (realistic cracking)

- 🛠️ **Utilities**
  - Wordlist generator
  - Progress tracking
  - Clean CLI output with stats

---

## 📁 Project Structure
password_cracker/
│
├── crack.py # Main CLI entry point
│
├── core/
│ └── hasher.py # Hashing + auto-detection
│
├── attacks/
│ ├── dictionary.py # Wordlist-based attack
│ ├── brute_force.py # itertools-based brute force
│ └── hybrid.py # Mutations (leet, digits, symbols)
│
├── utils/
│ ├── display.py # Progress bar & results UI
│ └── wordlist_gen.py # Custom wordlist generator
│
└── wordlists/
└── common.txt # Starter passwords


---

## ⚙️ Requirements

- Python **3.10+**

### Built-in Libraries Used:
hashlib, itertools, threading, argparse, json, os, time, sys


No external dependencies required ✅

---

## 🧪 Usage

### 🔑 1. Generate a Hash

```
python crack.py hash -p "dragon" -a sha256

```

### 📖 2. Dictionary Attack (FASTEST)
```
python crack.py attack -t <HASH> -m dict -w wordlists/common.txt -a sha256
```
### 🔁 3. Brute-Force Attack
```
python crack.py attack -t <HASH> -m brute -c alpha -l 4 -a md5
```
### ⚡ 4. Hybrid Attack (SMART CRACKING)
```
python crack.py attack -t <HASH> -m hybrid -w wordlists/common.txt -a sha256
```
### 🛠️ 5. Generate Custom Wordlist
```
python crack.py wordlist -o wordlists/custom.txt --type leet --min 6 --max 10
```
### 📊 Example Output
[+] Target Hash Detected: SHA256
[+] Attack Mode: Dictionary
[+] Trying passwords...

[✓] Password Found: dragon
[⏱] Time Elapsed: 0.02s
[📈] Attempts: 152


