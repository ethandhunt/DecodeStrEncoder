import math

file = open("DecodeString.txt")
string = file.read()
file.close()

file = open("Message.txt")
Message = int(file.read())
file.close()

def digitsequence(a, b):
    results = ""
    while True:
        results += string[(a % b)]
        if a < b: break
        a //= b
    return results

print(digitsequence(Message, len(string)))
input()