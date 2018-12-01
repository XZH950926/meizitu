lst=[{"name":"zhangsan","age":17},{"name":"lisi","age":18},{"name":"zhaoliu","age":11},{"name":"wangsan","age":27}]
def sort(lst,key,reverse=False):
   for i in range(len(lst)-1):
       for j in range(len(lst)-1):
           preVal=key(lst[j])
           nextVal=key(lst[j+1])
           if (preVal<nextVal if reverse else preVal>nextVal):
               preVal,nextVal,nextVal,preVal
sort(lst,lambda item:item["age"],reverse=True)



