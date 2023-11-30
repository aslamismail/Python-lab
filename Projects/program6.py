#whether list are of same length
list1=[1,2,45,78,98]
list2=[3,6,87,9,12,5]
print("list 1 :",list1)
print("list 2 :",list2)
print("lenghth of list 1 = ",len(list1))
print("lenghth of list 2 = ",len(list2))
if len(list1)==len(list2):
    print("length of list are same")
else:
    print("not same length")

#whether list sums to same value
print("sum of list 1 = ",sum(list1))
print("sum of list 2 = ",sum(list2))
if sum(list1)==sum(list2):
    print("sum of two lists are same")
else:
    print("sum of lists not same")

#whether any value occur in both
check=any(item in list1 for item in list2)
print("any value occur in both: ",check)