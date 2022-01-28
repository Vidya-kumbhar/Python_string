# 1Q convert a numeric words to numbers

n = input('enter a numeric word : ').lower()
a = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
b = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
n1=n.split()
s =set(n1)
if n in b.keys():
    print('word in numeric:', b[n])
elif s.issubset(set(b)):
    print('word in numeric:', end='')
    for i in n1:
        print(b[i], end='')
else:
    print('enter a correct word')
#---------------------------------------------------
# 2Q word location in string
s ='geeksforgeeks is best for geeks'
search_w = 'best'
print('location of',search_w,'is:',s.index('best'))
#----------------------------------------------

#4Q sort string list by k character frequency
test_lists=['geeksforgeeks', 'is', 'bessst', 'for', 'geeks']
k = 'e'
# o/p=['bessst','geeksforgeeks','geeks','is','for']
print(list(sorted(test_lists,key=lambda x:x.count(k),reverse=True)))