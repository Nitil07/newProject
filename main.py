def password(string):
    
    myList=string.split()
    res=""
    for i in range(len(myList)):
        if len(myList[i]) is 2:
          res =res+'*'
        res=res+myList[i][0]
    return res

    
string =" I love programming because of it's endless applications "
newPassword=password(string)
print(newPassword)