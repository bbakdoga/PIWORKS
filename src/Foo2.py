def solution(n, b):
    #print(n)
    #print(b)
    tempN = n

    found = False
    listt = []
    listt.append(tempN)
    while(found == False):

        k = len(tempN)
        nArray = [int(x) for x in str(tempN)]

        AscN = sorted(nArray)
        desN = sorted(nArray, reverse=True)

        y = int(''.join(map(str,AscN)))

        x = int(''.join(map(str,desN)))

        cycledX = converter(str(x), b)
        cycledY = converter(str(y),b)
        print(cycledX)
        print(cycledY)

        cycledZ = cycledX - cycledY
        
        #print(x)
        #print(cycled)
        reverseZ = ternary(cycledZ,b)
        #print(reverseZ)
        #z = x - y 
        tempN = str(reverseZ)
        while( len(tempN) < k):
            tempN = "0" + tempN
        
        listt.append(tempN)
        #print(tempN)

        if(find_repeat(listt) != None):
            found = True
       
        #print( x, "  ", y)
         #print(y)
    print(listt)
    lastNum = listt[len(listt) - 1]
    counter = 1
    i = len(listt) - 2
    while(i >= 0):
        if(lastNum == listt[i]):
            return counter
        counter += 1
        i -= 1
  
def converter(s,t):
    if (t == 10):
            return int(s)
    
    n = len(s) 
    total = 0
    for xs in range(n):
        n = n - 1
        temp =  int(s[xs]) 
        
        temp =  temp * (t ** n)
        #print(temp)
        total = total + temp
    return total

def solve(s, t):
        if (t == 10):
            return int(s)
        ans = 0
        for c in map(int, s):
            ans = t * ans + c
        return ans
        
def ternary(n,t):
    if(t == 10):
        return n
    e = n//t
    q = n%t
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return ternary(e,t) + str(q)
def find_repeat(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)

print(solution('1211', 10))

listt = [1,2,3,4,5]

if (find_repeat(listt) == None):
    print("hello there")

print(converter("1211", 10))
print(solution("210022", 3))
