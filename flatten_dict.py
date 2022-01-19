def flatten(org_dict,main_key):
    another_empty={}
    for key in org_dict:
        if type(org_dict.get(key))==int:
            another_empty[main_key+'.'+key]=org_dict.get(key)
        else:
            another_empty.update(flatten(org_dict.get(key),(main_key+'.')+key))                        
    return another_empty      
    
a=eval(input())
b=a.copy()
empty={}
for i in range(len(b)):
    for k in a :
        if type(a.get(k))==int:
            empty[k]=a.get(k)
        else:
            empty.update(flatten(a.get(k),k))                               
print(empty)