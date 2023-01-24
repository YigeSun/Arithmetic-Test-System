import random

def featureSelection(request):
    if request == "A":
        name = input("Please Enter Your Name:")
        nameLen = len(name)
        ft = open("/Users/yigesun/Desktop/Python_FinalProject/Record.txt", "r")
        ID = '100000'
        intID = 100000
        test = False
        for line in ft.readlines():
            #if line[6+nameLen+1] == ",":
            same = True
            for i in range(7, 7+nameLen):
                if len(line) > i:
                    if line[i] == name[i-7]:
                       pass
                    else:
                        same = False
                else:
                    same = False
            curID = line[0] + line[1] + line[2] + line[3] + line[4] + line[5]
            intCurID = eval(curID)
            if intCurID > intID:
                intID = intCurID
            if same:
                test = True
                break
        ft.close()
        
        #ID = eval(ID)
        if test == False:            
            intID+=1
        score = arithmetic()
        recordStr = "{}{}{}{}{}".format(intID, "," , name, ",", score)
        ft = open("/Users/yigesun/Desktop/Python_FinalProject/Record.txt", "a")
        ft.write(recordStr)
        ft.write("\n")
        ft.close()

    if request == "B":
        choice = input("Please Enter Your Name or Your ID:")
        if choice.isdigit():
            score = findAllThroughID(choice)
        else:
            score = findAllThroughName(choice)
        print("Your average score is:", score)
    if request == "C":
        calculateAverage()

def calculateAverage():
    ft = open("/Users/yigesun/Desktop/Python_FinalProject/Record.txt", "r")
    
    for line in ft.readlines():
        fts = open("/Users/yigesun/Desktop/Python_FinalProject/everyAve.txt", "a")
        id = line[0:6]
        name = getName(line)
        #查看是否已经被sort。如果没有返回-1
        #对于第一次出现的记录，找到它的所有同id分数条，算平均数，存入sort.txt
        num = getNum(id)
        if num == -1:
            averageScore = findAllThroughID(id)
            aSstring = '%f'%averageScore
            fts.write(id)
            fts.write(",")
            fts.write(name)
            fts.write(",")
            fts.write(aSstring)
            fts.write("\n")
            fts.close()
    ft.close()
    sort(11,1)

def sort(max,rank):
    fts2 = open("/Users/yigesun/Desktop/Python_FinalProject/everyAve.txt", "r")
    curMax = 0
    for line in fts2:
        nameLen = len(getName(line))
        strScore = line[8+nameLen: 12+nameLen]
        score = eval(strScore)
        if score < max and score >= curMax:
            curMax = score
    fts2.close()
    fts2 = open("/Users/yigesun/Desktop/Python_FinalProject/everyAve.txt", "r")
    for line in fts2:
        nameLen = len(getName(line))
        strScore = line[8+nameLen: 12+nameLen]
        score = eval(strScore)
        if score == curMax:
            print(line[:12+nameLen], "第", rank, "名")
    fts2.close()
    rank += 1
    min = 10
    fts2 = open("/Users/yigesun/Desktop/Python_FinalProject/everyAve.txt", "r")
    for line in fts2:
        nameLen = len(getName(line))
        strScore = line[8+nameLen: 12+nameLen]
        score = eval(strScore)
        if score < min:
            min = score
    fts2.close()
    if curMax > score:
        sort(curMax, rank)
    

def getName(line):
    nameLen = 7
    for ele in line[7:]:
        if ele != ",":
            nameLen += 1
        else:
            break
    name = line[7: nameLen]
    return name


def getNum(id):
    fts = open("/Users/yigesun/Desktop/Python_FinalProject/everyAve.txt", "r")
    num = -1
    for line in fts:
        if line[0:6] == id:
            fts.close()
            return 1
    fts.close()
    return num



def findAllThroughID(choice):
    ft = open("/Users/yigesun/Desktop/Python_FinalProject/Record.txt", "r")
    totalScore = 0
    time = 0
    for line in ft.readlines():
        testID = line[0:6]
        if testID == choice:
            time += 1
            if line[-3] == ',':
                totalScore += eval(line[-2])
            else:
                totalScore += eval(line[-3: -1])
    ft.close()
    if time != 0:
        score = round(totalScore/time, 2)
    else:
        score = 0
    return score

def findAllThroughName(choice):
    ft = open("/Users/yigesun/Desktop/Python_FinalProject/Record.txt", "r")
    nameLen = len(choice)
    #print(nameLen)
    totalScore = 0
    time = 0
    for line in ft.readlines():
        #print(line[7: 7+nameLen])
        if line[7: 7+nameLen] == choice:
            time += 1
            #print(line[-3])
            if line[-3] == ',':
                #print(eval(line[-2]))
                totalScore += eval(line[-2])
            else:
                #print(eval(line[-3: -1]))
                totalScore += eval(line[-3: -1])
    ft.close()
    if time != 0:
        #print("total score:",totalScore)
        #print("time:",time)
        score = round(totalScore/time, 2)
    else:
        score = 0
    return score




#functions about A
def arithmetic():
    score = 0;
    for i in range(0, 10):
        #print(i)
        ans =int(createArith())
        print("Answer:", ans)
        stuAns = int(input("Your Answer:"))
        if ans == stuAns:
            score += 1
            #print(score)
    return score

def createArith():
    equaList = getEqua()
    #print(equaList)
    equation = "{0}{1}{2}".format(equaList[0], equaList[2],equaList[1])
    print(equation)
    ans = calculate(equaList[0], equaList[1], equaList[2])
    return ans

def getEqua():
    #得到random两个数字和运算符，但全在列表里
    num1L = random.sample(range(0, 101), 1)
    num2L = random.sample(range(0, 101), 1)
    operatorL = random.sample(["+", "-", "*", "/"], 1)
    #列表转成string
    num1 = num1L[0]
    num2 = num2L[0]
    operator = operatorL[0]
    equaList = [num1, num2, operator]
    #print(type(num1))
    #print(equaList)
    if operator == "/":
        num1L = random.sample(range(0, 100), 1)
        num2L = random.sample(range(1, 100), 1)
        while num1L[0] * num2L[0] > 100:
            num1L = random.sample(range(0, 100), 1)
            num2L = random.sample(range(1, 100), 1)
        num1 = num1L[0] * num2L[0]
        num2 = num2L[0]
        equaList = [num1, num2, "/"]
    if operator == "*":
        while calculate(equaList[0], equaList[1], equaList[2]) >= 100:
            equaList = getNewEqua() + [equaList[2]]
    if operator == "+":
        while calculate(equaList[0], equaList[1], equaList[2]) >= 100:
            equaList = getNewEqua() + [equaList[2]]
    if operator == "-":
        while calculate(equaList[0], equaList[1], equaList[2]) < 0:
            equaList = getNewEqua() + [equaList[2]]
    return equaList

def getNewEqua():
    #得到random两个数字和运算符，但全在列表里
    num1L = random.sample(range(0, 101), 1)
    num2L = random.sample(range(0, 101), 1)
    #operatorL = random.sample(["+", "-", "*", "/"], 1)
    #列表转成string
    num1 = num1L[0]
    num2 = num2L[0]
    #operator = operatorL[0]
    equaList = [num1, num2]
    return equaList



#进来的必须是string
def calculate(num1, num2, operator):
    equation = "{0}{1}{2}".format(num1, operator, num2)
    ans = eval(equation)
    return ans




# A: New Test
# B: Score History Query
# C: Grade Sorting
request = input("Feature Selection:")
featureSelection(request)
