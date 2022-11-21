supermer = {}

while True:
    name = input("Ingresa producto: ")
    if name == '':
        break

    score = int(input("Ingresa precio de producto '(0-score)':  "))
    if score  in range(0,score ):
	    break

    if name in supermer:
        supermer[name] += (score,)
    else:
        supermer[name] = (score,)

for name in sorted(supermer.keys()):
    adding = 0
    counter = 0
    for score in supermer[name]:
        adding += score
        counter += 1
    print(name, ":", adding + counter)