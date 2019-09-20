def merge(num1, num2):
    
    if(len(num1)<1):
        s.extend(num2)
        return
    if(len(num2)<1):
        s.extend(num1)
        return
    if(num1[0]< num2[0]):
        s.append(num1[0])
        merge(num1[1:],num2)
    else:
        s.append(num2[0]) 
        merge(num1, num2[1:])


s= []

num1 = [1,6,8,10]
num2 = [2,3,5,7]

merge(num1,num2)
print(s)