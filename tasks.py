import random

def mod(n: int, u: int):
    return n%u
    
def euler(n: int):
    res = n
    i = 2
    while i**2 < n:
        while n % i == 0:
            n /= i
            res -= res / i
        i += 1
    if n > 1: 
        res -= res / n
    return int(res)

def prime_num(start: int, stop: int):
    prime_numbers=[]
    for i in range(start, stop):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers

a = int(input("Input `a` value: "))
b = int(input("Input `b` value: "))
m = int(input("Input `m` value: "))

task_2 = mod(a, m)
task_3 = mod(a**b, m)
task_4 = mod(b*a**(euler(m)-1), m)
task_5 = random.choice(prime_num(a, b))

print(f'Task 2: {a} mod {m} = {task_2}')
print(f'Task 3: {a}^{b} mod {m} = {task_3}')
print(f'Task 4: {b}*{a}^(Ф({m})-1) mod {m} = {task_4}')
print(f'Task 5: Random prime number from {a} to {b} = {task_5}')
