from functools import reduce

multiples = []

for i in range(1, 20):
    total = i

    for multiple in multiples:
        if total % multiple == 0:
            total = total / multiple

    if total != 1:
        multiples.append(total)

product = reduce((lambda aggregator, multiple: aggregator * multiple), multiples)
print(product)
