def implies(a,b):
    if a==1 and b==0 : return 0
    else : return 1
def org(a,b):
    if a==0 and b==0 : return 0
    else : return 1
def andg(a,b):
    if a==1 and b==1 : return 1
    else : return 0     
def notg(a):
    if a==1 : return 0
    else : return 1    
p=0
q=0 
r=0
P=[1,1,1,1,0,0,0,0]
Q=[1,0,1,0,1,1,0,0]
R=[1,1,0,0,1,0,1,0]
val=[]
vals=[]
count=0
satisfies=False
F=[implies(p,q),implies((notg(q)),(notg(r)))]#,implies(r,q),(r),andg(p,q),org(p,q)]
si=p
for j in range(0,8):
    p=P[j]
    q=Q[j]
    r=R[j]
    for i in range(0,len(F)):
        if F[i]==F[0]:
            count+=1
            vals.append(i)
    val.append(j)    
    if count==len(F):
        satisfies=True   
    count=0     
#for i in range(0,len(vals)/2):
#    A=vals[i:i+2]
#    for i in range(0,len(A)):
#        
print(satisfies,vals,val)        