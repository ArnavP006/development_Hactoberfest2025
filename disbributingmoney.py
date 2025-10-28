def distributingMoney(x,y,z,k) : 

    total = x + y + z + k
    if total % 3 != 0:
        return(0)

    else:
        a = total // 3
        if a >= x and a >= y and a >= z:
            return(1)
        else:
            return(0)    




x,y,z,k= map(int,input().split());
print (int(distributingMoney(x,y,z,k)))
