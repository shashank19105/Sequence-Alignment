print("Welcome to Global sequence alignment!")
A = input("Enter the first sequence (A,T,G,C): ")
B = input("Enter the second sequence (A,T,G,C): ")
sizeOfA = len(A)
sizeOfB = len(B)

dpTable = [[0 for x in range(sizeOfA+2)] for y in range(sizeOfB + 2)]
dpTable[0][0] = " "
dpTable[0][1] = " "
dpTable[1][0] = " "
for x in range(2,sizeOfA+2):
    dpTable[0][x] = A[x-2]
for x in range(2,sizeOfB+2):
    dpTable[x][0] = B[x-2]

 # table has been created and the index 1,1 stores the first integer 0

match = 2
mismatch = -1
gap = -2

for x in range(2,len(dpTable[1])):
    dpTable[1][x] = dpTable[1][x-1] + gap
for x in range(2,sizeOfB+2):
    dpTable[x][1] = dpTable[x-1][1] + gap

# initialised the first row and first column of integers with gap penalties

for x in range(2,sizeOfB+2):
    for y in range(2,sizeOfA+2):
        left = dpTable[x][y-1] + gap
        above = dpTable[x-1][y] + gap
        if dpTable[0][y] == dpTable[x][0]:
            diagonal = dpTable[x-1][y-1] + match
        else:
            diagonal = dpTable[x-1][y-1] + mismatch
        max = left
        if above>max:
            max = above
        if diagonal>max:
            max = diagonal
        dpTable[x][y] = max

for i in range(sizeOfB+2):
    for j in range(sizeOfA+2):
        print(dpTable[i][j], end='\t' )
    print("")

s1 = ""
s2 = ""
count = 1
maxScore = dpTable[sizeOfB+1][sizeOfA+1]
def reverseString(s):
    return s[::-1]

def scoreThis(s1,s2): #finding score by comparing the two strings
    score = 0
    for i in range(len(s1)):
        if s1[i] == "_" or s2[i] == "_":
            score += gap
        elif s1[i] != s2[i]:
            score += mismatch
        elif s1[i] == s2[i]:
            score += match
    return score

def recurs(x, y, s1, s2): #recursion to backtrack to find the alignments
    global count, maxScore
    if x == 1 and y == 1:
        reversedS1 = reverseString(s1)
        reversedS2 = reverseString(s2)
        score = scoreThis(s1, s2)
        #print(score)
        if score == maxScore:
            print(count, end="")
            print("th such global alignment is:")
            count += 1
            print(reversedS1)
            print(reversedS2)
            print("Score:", end=" ")
            print(score)

    elif x == 1 and y != 1:
        recurs(x, y - 1, s1 + dpTable[0][y], s2 + "_")
    elif y == 1 and x != 1:
        recurs(x - 1, y, s1 + "_", s2 + dpTable[x][0])
    else:
        if dpTable[x][y-1] == dpTable[x][y] - gap:
            recurs(x, y-1, s1 + dpTable[0][y], s2 + "_")
        if dpTable[x-1][y] == dpTable[x][y] - gap:
            recurs(x-1, y, s1 + "_", s2 + dpTable[x][0])
        if dpTable[x-1][y-1] == dpTable[x][y] - match:
            recurs(x-1, y-1, s1 + dpTable[0][y], s2 + dpTable[x][0])
        if dpTable[x-1][y-1] == dpTable[x][y] - mismatch:
            recurs(x-1, y-1, s1 + dpTable[0][y], s2 + dpTable[x][0])

recurs(sizeOfB+1,sizeOfA+1,s1,s2) #we start from the bottom right most element