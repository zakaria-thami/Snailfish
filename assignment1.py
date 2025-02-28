#SNAILFISH CHALLENGE-assignment 1
#calculating the output of the snailfish numbers

#a snalifish number is an array of 2 elements

class Snailfish():
    #To Consider:
    #adding a depth attribute to the class
    #when creating a new snailfish check if the inputs are snailfish 
    #if it is snailfish then access the inputs depth and increase 
    #else just continue
    def __init__(self,a,b):
        self.left=a
        self.right=b
        self.depth=0
    def check(self):
        pass

    @staticmethod
    def addSnailfish(s1,s2):
        result=Snailfish(s1,s2)
        result.check()
        return result
    
    @staticmethod
    def increaseDepth(s):
        s.depth+=1

    
    def __str__(self):
        # Return a custom string representation of the object
        return f'[{self.left},{self.right}]'

# snailfish example: [[[[[9,8],1],2],3],4]
#[[6,[5,[4,[3,2]]]],1]
def readingInput(path):
    with open(path,'r') as f:
        output=[]
        numbersBuffer=[]
        isDigit=False
        while True:
            c=f.read(1)
            
            if(c.isdigit()):
                if(not isDigit):
                    numbersBuffer.append(int(c))
                else:
                    numbersBuffer[-1]=numbersBuffer[-1]*10 +int(c)
                isDigit=True
            else:
                isDigit=False
                if(c==']'):
                    sn=Snailfish(numbersBuffer[-2],numbersBuffer[-1])
                    numbersBuffer.pop()
                    numbersBuffer.pop()
                    numbersBuffer.append(sn)
                elif(c=='\n'):
                    #new line 
                    #new snailfish number
                    output.append(sn)
                    numbersBuffer.clear()
                elif(not c):
                    break
    return output


path1 = "input.txt"

#Parsing the inputs as a list test
result=readingInput(path1)
for s in result:
    print(s)
