#List of positive numbers from a given list of integers
list1 = [1,-2,3,-4,5,6,-7,8,-9,10]
print("list 1",list1)
print("positive numbers:")
for num in list1:
    if num>=0:
        print(num)

#Square of numbers
list2 =[1,2,3,4,5,34,6,78,4,8]
print("list2 : ",list2)
print("Square of list 2:")
for n in list2:
    print(n**2)

#Form a list of vowels selected from a given word
V=['a','e','i','o','u']
word=input("Enter the word")
word=word.lower()
S=[i for i in word if i in V]
print(S)

#List ordinal value of each element in a word
word=input("Enter the word")
j=[ord(x) for x in word]
print(j)

