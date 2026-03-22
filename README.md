## password-cracker
 A modular python CLI tool that stimulates how attacks crack passwords, using dictionary attacks and brute forces. 

 ## Project Layout...password_cracker/
├── crack.py              ← Main CLI (all commands live here)
├── core/
│   └── hasher.py         ← MD5, SHA1, SHA256, SHA512, bcrypt + auto-detect
├── attacks/
│   ├── dictionary.py     ← Wordlist line-by-line attack
│   ├── brute_force.py    ← Exhaustive itertools.product generator
│   └── hybrid.py         ← Dict + leet/digits/symbols/case mutations
├── utils/
│   ├── display.py        ← Progress bar, result banner, stats table
│   └── wordlist_gen.py   ← Generate common/numeric/leet wordlists
└── wordlists/
    └── common.txt        ← ~100 bundled passwords to start with

 ## Requirements...
 # Python 3.10+ is required (uses `str | None` union type syntax)
#
# CORE (stdlib only — no install needed):
#   hashlib, itertools, threading, argparse, json, os, time, sys, re

 ## How TO Run...
 # 1. Hash a password to get your target
python crack.py hash -p "dragon" -a sha256

# 2. Dictionary attack (fastest – hits common passwords in ms)
python crack.py attack -t <HASH> -m dict -w wordlists/common.txt -a sha256

# 3. Brute-force (guaranteed, but slow past length 5)
python crack.py attack -t <HASH> -m brute -c alpha -l 4 -a md5

# 4. Hybrid (dict + leet/digits/symbols – cracks "p4ssw0rd!" style)
python crack.py attack -t <HASH> -m hybrid -w wordlists/common.txt -a sha256

# 5. Generate a custom wordlist
python crack.py wordlist -o wordlists/custom.txt --type leet --min 6 --max 10

 
 


 
 
