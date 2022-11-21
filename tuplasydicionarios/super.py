supermer = {}

while True:
    name = input("Ingresa producto: ")
    if name == '':
        break

    score = int(input("Ingresa precio de producto:  "))
    if score not in range(0, 999999):
	    break

    if name in supermer:
        supermer[name] += (score,)
    else:
        supermer[name] = (score,)
suma=0

for name in sorted(supermer.keys()):

    counter = 0
    for score in supermer[name]:

        suma +=score
        print(name, ':',score)
print('total',  suma)