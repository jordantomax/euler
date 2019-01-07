sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)


# Playing with recurring function
# But run time was just as slow as above
# And it is less elegant
def recur_three(sum=0, num=0):
    num = num + 3
    sum += num
    if num <= 1000:
        return recur_three(sum, num)
    else:
        print(sum)
