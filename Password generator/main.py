import random
import string

size = int(input("How many letter would like in your password? "))
symbols = int(input("How many symbols? "))
numbers = int(input("How many numbers? "))


temp0 = [random.choice(string.punctuation) for x in range(0,symbols)]
temp1 = [random.choice(string.digits) for x in range(0,symbols)]
size_num = size-symbols-numbers
temp2 = [random.choice(string.ascii_letters) for x in range(0,size_num)]

final = temp0+temp1+temp2
random.shuffle(final)

output = "".join(final)
print(output)