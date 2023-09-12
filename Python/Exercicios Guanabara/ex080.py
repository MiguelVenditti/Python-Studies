list = []

for x in range(0, 5):
    num = int(input("Digite um valor: "))
    if x == 0 or num > list[-1]:
        list.append(num)
    else:
        y = 0
        while y < len((list)):
            list.insert(y, num)
            break
print()
print("Os valores digitados foram {}".format(list))