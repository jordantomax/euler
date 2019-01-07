sum = 0
sequence = [1, 2]

while sequence[-1] <= 4000000:
    sequence.append(sequence[-1] + sequence[-2])

for i in sequence:
    if i % 2 == 0:
        sum += i

print(sum)
