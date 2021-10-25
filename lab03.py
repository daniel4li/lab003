def multiply(x,y):
    if x== 0 or y== 0:
        return 0
    return x + multiply(x, y-1)

assert multiply(5,4) == 20
assert multiply(0,4) == 0
assert multiply(5,0) == 0
assert multiply(1,1) == 1

def collectOddValues(listofInt):
    a = listofInt
    if len(a) == 0: 
        return []
    if a[0] % 2 == 1:
        return [a[0]] + collectOddValues(a[1:])
    return collectOddValues(a[1:])


def countInts(listofInt, num):
    a = listofInt
    b = num
    if not a:
        return 0
    if a[0] == b:
        return 1 + countInts(a[1:],b)
    return countInts(a[1:], b)

assert countInts([], 2) == 0
assert countInts([2,2,2,2,2,2,2,2,2], 2) == 9
assert countInts([1,2,3,4,3,2,1], 5) == 0
assert countInts([18,2,3,4,3,2,1], 18 ) == 1

def reverseString(s):
    if len(s) == 0:
        return s
    return reverseString(s[1:]) + s[0]

assert reverseString("CMPSC9") == "9CSPMC" 
assert reverseString("") == ""
assert reverseString("rACecar") == "raceCAr"
assert reverseString("9.0") == "0.9"




def removeSubString(s, sub):
    if s == "" :
        return ""
    if sub == "":
        return s
    start = s.find(sub) 
    if start == -1:
        return s
    return s[:start] + removeSubString(s[(start + len(sub)):], sub)
   


assert removeSubString("Lolololol", "lol") == "Loo"
assert removeSubString("Lolololol", "") == "Lolololol"
assert removeSubString("", "lol") == ""
assert removeSubString("abc", "d") == "abc"
assert removeSubString("xyxyxyxyxyxyxyxyxyxyxyxyxy", "xy") == ""