from collections import deque

def is_palindrome(input_str):
    cleaned = ''.join(ch.lower() for ch in input_str if not ch.isspace())
    char_queue = deque(cleaned)
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

if __name__ == "__main__":
    input_str = input("Введіть рядок для перевірки на паліндром: ")
    if is_palindrome(input_str):
        print("Ваш рядок є паліндромом.")
    else:
        print("Ваш рядок не є паліндромом.")
