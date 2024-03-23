
import random

def generate_random_code(length=10):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ""
    for _ in range(length):
        index = random.randint(0, len(characters) - 1)
        code += characters[index]
    return code

random_code = generate_random_code()
print(f"随机生成的代码：{random_code}")
``` 
