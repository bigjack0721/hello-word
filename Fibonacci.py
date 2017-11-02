fibonacci = [1, 2]
def next_number(x):
    number1 = fibonacci[len(fibonacci)-1]
    number2 = fibonacci[len(fibonacci)-2]
    number = number1 + number2
    fibonacci.append(number)
    return fibonacci
while fibonacci[len(fibonacci)-1] < 4000000:
    next_number(fibonacci)
result = 0
for i in fibonacci:
    if i % 2 == 0:
        result = result + i
print(result)
