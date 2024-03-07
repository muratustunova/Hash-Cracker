import hashlib
import time

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def brute_force_attack(target_hash):
    characters = [chr(i) for i in range(32, 127)]  # ASCII'deki yazdırılabilir karakterler aralığı
    word_length = 1
    start_time = time.time()
    
    while True:
        for char_combination in generate_combinations(characters, word_length):
            word = ''.join(char_combination)
            hashed_word = sha256_hash(word)
            if hashed_word == target_hash:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Match found! Word: {word}")
                print(f"Time elapsed: {elapsed_time:.2f} seconds")
                return
        word_length += 1

def generate_combinations(characters, word_length):
    if word_length == 0:
        yield []
        return
    for char in characters:
        for suffix in generate_combinations(characters, word_length - 1):
            yield [char] + suffix

if __name__ == "__main__":
    target_hash = input("Enter the target SHA256 hash: ")
    print("Starting brute force attack...")
    brute_force_attack(target_hash)


