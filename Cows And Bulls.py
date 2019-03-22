import random
import sys
elo='n'
while(elo!='y'):
    final=""
    for i in range(1,5):
        number=random.randint(0,9)
        final=final+str(number)
    print(final)
    user=int(input("Give a 4-digit number: "))
    user=str(user)
    j=0
    for num in user:
        j=j+1
    if j!=4 or final==user:
        sys.exit()
    else:
        cow=0
        bull=0
        final=list(final)
        user=list(user)
        for a in user:
            if a==final[user.index(a)]:
                cow=cow+1
        for b in user:
            if b in final and b != final[user.index(b)] and final.count(b)>=1:
                bull=bull+1
    print("You've got %s cows and %s bulls" % (cow, bull))
    elo=input("chcesz zakonczyc (y)")
    
            
        
                
    
    
    
