# Вопрос 6. Линейные структуры данных. Стек. Задача о правильной скобочной последовательности.
# Задача. Пусть нам дана последовательность из трёх видов скобок: (), [], {}. Необходимо
# проверить, является ли она правильной. Правильной является последовательность, которая
# может возникнуть при записи некоторого арифметического выражения.
# Пример правильной последовательности: ()[]

# To check whether a given sequence of brackets is valid or not, we can use a stack data structure. The idea is to traverse the given sequence of brackets from left to right. If we encounter an opening bracket, we push it onto the stack. If we encounter a closing bracket, we pop an opening bracket from the stack and compare it with the closing bracket. If they match, we continue. If they do not match, the sequence is not valid.

# Here's an example implementation in Python:

def is_valid_sequence(s):
    stack = []
    mappings = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mappings:
            top_element = stack.pop() if stack else '#'
            if mappings[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
  
#   In this implementation, we use a dictionary mappings to store the mapping between closing and opening brackets. We traverse the given string s character by character, and for each closing bracket, we check if the top element of the stack matches the corresponding opening bracket. If they match, we continue. If they do not match, the sequence is not valid. At the end, if the stack is empty, the sequence is valid. Otherwise, it is not valid.

# You can call this function with a string argument like this:
is_valid_sequence('([]()){}')
# This will return `True` because the given sequence is a valid bracket sequence.
