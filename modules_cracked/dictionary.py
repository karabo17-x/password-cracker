import time
from hasher import verify_hash
from display import progress_bar

def dictionary_attack(
  target_hash: str,
  wordlist_path: str,
  algorithm: str,
  verbose: bool = False,
  delay: float = 0.0
) -> tuplet[str | None, int]:
  print(f"\n \033[94m[*]\033[0m Starting dictionary attack...")
  print(f"  \033[94m[*]\033[0m Wordlist : {wordlist_path}")
  print(f"  \033[94m[*]\033[0m Algorithm: {algorithm.upper()}\n")
  
  try:
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
      words = [line.strip() for line in f if line.strip()]
  except FileNotFoundError:
    print(f" \033[91m[!] Wordlist not found: {wordlist_path}\033[0m\n")
    return None, 0

  total = len(words)
  attempts = 0

  for i, word in enumerate(words):
      attempts += 1
      if verbose:
        print(f" \033m[90m[~] Trying: {word}\033[0m")
      elif i % max(1, total // 50) == 0:
        progress_bar(i, total, prefix=" Progress")
      if delay > 0:
        time.sleep(delay / 1000)
      if verify_hash(word, target_hash, algorithm):
        progress_bar(total, total, prefix=" Progress")
        return word, attempts

  progress_bar(total, total, prefix=" Progress")
  return None, attempts

      
    
   
    


      




