file = open("Input.txt")
string = file.read()
file.close()
decodeString = ""
decodeStringFrequency = []
for character in string:
    if not character in decodeString:
        decodeString += character
        decodeStringFrequency += [1]
    else:
        decodeStringFrequency[decodeString.index(character)] += 1


newStrArr = list(decodeString)
while not decodeStringFrequency == sorted(decodeStringFrequency):
    for i in range(len(decodeStringFrequency) - 1):
        if decodeStringFrequency[i] > decodeStringFrequency[i + 1]:
            decodeStringFrequency[i], decodeStringFrequency[i+1] = decodeStringFrequency[i+1], decodeStringFrequency[i]
            newStrArr[i], newStrArr[i+1] = newStrArr[i+1], newStrArr[i]

newStrArr.reverse()
decodeString = "".join(newStrArr)


i = 1
array = []
for character in string:
    array += [decodeString.index(character)]

Message = 0
for Power in range(len(array)):
    Message += array[Power] * (len(decodeString) ** Power)

print(f"{decodeString}\n{Message}")
file = open("DecodeString.txt", "w")
file.write(decodeString)
file.close()
file = open("Message.txt", "w")
file.write(str(Message))
file.close()
input()