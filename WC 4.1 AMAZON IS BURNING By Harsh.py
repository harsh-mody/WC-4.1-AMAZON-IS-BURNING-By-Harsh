array = list(map(int, input('Please Enter The List To Be Entered : ').split(",")))
print(array)
arrayCount = []
countOfAnimalInPairList = []
typeOfAnimalInPairList = []
for i in range(1, 21):
    arrayCount.append(((array.count(i)), i))
for j in range(0, len(arrayCount)):
    arrayPair = arrayCount[j]
    countOfAnimalInPair = arrayPair[0]
    typeOfAnimalInPair = arrayPair[1]
    countOfAnimalInPairList.append(countOfAnimalInPair)
    typeOfAnimalInPairList.append(typeOfAnimalInPair)
print(typeOfAnimalInPairList, countOfAnimalInPairList)
maximumInList = max(countOfAnimalInPairList)
indexOfMaximumInList = countOfAnimalInPairList.index(maximumInList)
type = typeOfAnimalInPairList[indexOfMaximumInList]
print("Type : ", typeOfAnimalInPairList[indexOfMaximumInList])