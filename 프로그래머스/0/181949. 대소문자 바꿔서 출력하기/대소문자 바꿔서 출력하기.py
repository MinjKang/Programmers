str = input()

results = ''

for i in str:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    results += i

print(results)