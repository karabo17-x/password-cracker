import itertools
import os


COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "abc123", "monkey", "1234567",
    "letmein", "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine",
    "ashley", "bailey", "passw0rd", "shadow", "123123", "654321", "superman",
    "qazwsx", "michael", "football", "password1", "batman", "admin", "welcome",
    "login", "hello", "charlie", "donald", "password123", "qwerty123", "iloveyou1",
    "princess", "admin123", "rockyou", "secret", "abc", "test", "111111",
    "123456789", "1234", "1234567890", "0987654321", "password!",
]

LEET_MAP = str.maketrans("aeiost", "4310$+")


def _leet_variants(words):
    out = set(words)
    for w in words:
        out.add(w.translate(LEET_MAP))
    return sorted(out)


def generate_wordlist(output_path: str, min_len: int, max_len: int, wl_type: str) -> int:
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)

    words = set()

    if wl_type == "common":
        for w in COMMON_PASSWORDS:
            if min_len <= len(w) <= max_len:
                words.add(w)
                words.add(w.capitalize())
                words.add(w + "1")
                words.add(w + "!")
                words.add(w + "123")
        words.update(w for w in _leet_variants(list(words)) if min_len <= len(w) <= max_len)

    elif wl_type == "numeric":
        for length in range(min_len, max_len + 1):
            for combo in itertools.product("0123456789", repeat=length):
                words.add("".join(combo))
                if len(words) > 500_000:
                    break

    elif wl_type == "leet":
        base = [w for w in COMMON_PASSWORDS if min_len <= len(w) <= max_len]
        for w in _leet_variants(base):
            if min_len <= len(w) <= max_len:
                words.add(w)

    with open(output_path, "w", encoding="utf-8") as f:
        for word in sorted(words):
            f.write(word + "\n")

    return len(words)
