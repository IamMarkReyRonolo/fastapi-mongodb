import random
import string

def generate_random_sentence(length: int) -> str:
    words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua']
    sentence = ' '.join(random.choice(words) for _ in range(length))
    return sentence.capitalize() + '.'

def generate_random_string(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

random_string = generate_random_string(1000)
print(random_string)


# random_sentence = generate_random_sentence(1000)
# print(random_sentence)