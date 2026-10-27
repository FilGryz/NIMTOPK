from functions import is_palindrome, fibonacci, count_vowels, calculate_discount, flatten_list, word_frequencies, is_prime

def test_is_palindrom():
    assert is_palindrome("kajak") == True
    assert is_palindrome("TEster") == False
    assert is_palindrome("Kobyła ma mały bok") == True
    assert is_palindrome("python") == False
    assert is_palindrome("") == True
    assert is_palindrome("A") == True

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55

def test_count_vowels():
    assert count_vowels("Python") == 2
    assert count_vowels("AEIOUY") == 6
    assert count_vowels("bcd") == 0
    assert count_vowels("") == 0
    assert count_vowels("Próba żółwia") == 5

def test_calculate_discount():
    assert calculate_discount(100, 20) == 80.0
    assert calculate_discount(50, 0) == 50.0
    assert calculate_discount(200, 100) == 0.0
    try:
        calculate_discount(100, -10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative discount"
    
    try:
        calculate_discount(100, 150)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for discount greater than 100"

def test_flatten_list():
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert flatten_list([]) == []
    assert flatten_list([[[1]]]) == [1]
    assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


def test_word_frequencies():
    assert word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}
    assert word_frequencies("Hello, hello!") == {"hello": 2}
    assert word_frequencies("") == {}
    assert word_frequencies("Python Python python") == {"python": 3}
    assert word_frequencies("Ala ma kota, a kot ma Ale.") == {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1, "ale": 1}

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(29) == True
    assert is_prime(30) == False
