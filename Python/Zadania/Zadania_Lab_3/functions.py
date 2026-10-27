def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def count_vowels(text: str) -> int:
    vowels = "aeiouyąęóAEIOUYĄĘÓ"
    return sum(1 for char in text if char in vowels)

def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount / 100)

def flatten_list(nested_list: list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def word_frequencies(text: str) -> dict:


    import re
    from collections import Counter

    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned_text.split()
    
    return dict(Counter(words))

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True