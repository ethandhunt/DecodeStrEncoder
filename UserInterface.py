def encode(string):
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

def decode(decodeString, Message):
    string = decodeString
    Message = int(Message)

    def digitsequence(a, b):
        results = ""
        while True:
            results += string[(a % b)]
            if a < b: break
            a //= b
        return results

    print(digitsequence(Message, len(string)))

while True:
    userResponse = input("Encode or Decode: ")
    if userResponse == "Encode":
        encode(input("Enter Message: "))
    elif userResponse == "Decode":
        decode(input("Enter Decode String: "), input("Enter Message: "))
    else:
        print("That Wasn't a Valid Response")
