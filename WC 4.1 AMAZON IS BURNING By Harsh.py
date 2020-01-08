array = list(input("Please Enter A List : "))
arrayCount = []
countOfAnimalInPairList = []
typeOfAnimalInPairList = []
for i in range(1, 21):
    if array.__contains__(str(i)):
        arrayCount.append((array.count(str(i)), i))
for j in range(0, len(arrayCount)):
    arrayPair = arrayCount[j]
    countOfAnimalInPair = arrayPair[0]
    typeOfAnimalInPair = arrayPair[1]
    countOfAnimalInPairList.append(countOfAnimalInPair)
    typeOfAnimalInPairList.append(typeOfAnimalInPair)
maximumInList = max(countOfAnimalInPairList)
indexOfMaximumInList = countOfAnimalInPairList.index(maximumInList)
print("Type : ", typeOfAnimalInPairList[indexOfMaximumInList])