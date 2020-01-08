array = list(input("Please Enter A List : "))
arrayCount = []
for i in range(1, 21):
    if array.__contains__(str(i)):
        arrayCount.append((array.count(str(i)), i))
print(arrayCount)
