from collections import deque

# Функція для перевірки, чи є рядок паліндромом
def is_palindrome(s):
    # Видалити пробіли та привести до нижнього регістру
    s = ''.join(s.split()).lower()
    # Створити deque з символів рядка
    char_deque = deque(s)
    
    while len(char_deque) > 1:
        # Порівнюємо символи з початку та кінця
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади використання функції
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Hello"))                        # False
print(is_palindrome("racecar"))                      # True
print(is_palindrome("Was it a car or a cat I saw"))  # True