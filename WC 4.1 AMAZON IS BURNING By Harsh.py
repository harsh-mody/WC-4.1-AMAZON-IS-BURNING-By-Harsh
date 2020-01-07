array = list(input("Please Enter A List : "))
arrayCount = []
typeNumber = 0
for i in range(1, 20):
    if array.__contains__(str(i)):
        arrayCount.append(array.count(str(i)))
for j in range(0, len(arrayCount)):
    if arrayCount.count(j) >= 2:
        typeNumber = arrayCount.count(j)
print("Type : ", typeNumber)