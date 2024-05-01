from collections import deque

def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    # Створюємо двосторонню чергу та додаємо всі символи рядка до неї
    char_queue = deque()
    for char in input_string:
        char_queue.append(char)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False  
    return True

# Приклади використання
input_str1 = "12321"
input_str2 = "Toyota"
input_str3 = "Python"
input_str4 = "F1 F1"
input_str5 = "F11f"


print(is_palindrome(input_str1))  
print(is_palindrome(input_str2))  
print(is_palindrome(input_str3))  
print(is_palindrome(input_str4))
print(is_palindrome(input_str5))    
