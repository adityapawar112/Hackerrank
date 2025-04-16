stud = [] 
n = int(input())
for _ in range(n):
    name = input()
    score = float(input())
    stud.append([name, score])
        
def sco(val):
    return val[1]
    
stud.sort(key=sco)

nam = [x for x in stud if x[1] != stud[0][1] ]
nam1 = [x[0] for x in nam if x[1] == nam[0][1] ]
nam1.sort()
for names in nam1:
    print(names)
