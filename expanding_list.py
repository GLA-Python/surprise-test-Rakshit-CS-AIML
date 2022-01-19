a=list(map(int,input().split()))
def expanding(a):
    difference=[]
    d=0
    for i in range(len(a)-1):
        d=a[i]-a[i+1]
        difference.append(abs(d))
    return(sorted(set(difference))==sorted(difference))
    
print(expanding(a))    
    
