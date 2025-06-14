import random

key = []
abc = list("abcdefghijklmnopqrstuvwxyz")
randm = random.sample(abc, 5)
text = "".join(randm)
key.append(text)

numeros = [1,2,3,4,5,6,7,8,9,10]
numbersrandom = random.sample(numeros, 3)
number = "".join([str(n) for n in numbersrandom])
key.append(number)

ab = "".join(key)