'''
# Reverse eace word in a string

st = 'My Name is Jessa'
s = st.split()

# one way
ll = list()
print('string is:',st)
print('after reversing each word:')
for i in range(len(s)):
    ll = s[i]
    print(ll[::-1], end=' ')

#------------------------
#other way using list comprension
print('string is:',st)    
ll = [ll[::-1] for ll in s]
print('After reversing each word: ',' '.join(ll))
#------------------------------------

# wherever string has a number(n) it should be replaced by nth char after prior char to number 


# i/p = 'a4k3b2'
# expected o/p = 'aeknbd'
s = 'a4k3b2'
sl = []
for i in range(len(s)):

    if s[i].isalpha():
        sl.append(s[i])
    else:
        o = ord(s[i-1]) + int(s[i])
        sl.append(chr(o))

ok = ''.join(sl)
print(ok)

# ----------------------------------------------------

# convert alphanumeric string into a string having char then numbers 
a ='a12b6c634'
# expected o/p: abc126634
s = []
s1 = []
for i in a:
    if i.isalpha():
        s.append(i)
    elif i.isnumeric():
        s1.append(i)
    else:
        continue


s2 = s+s1
k = ''.join(s2)
print(k)
# ---------------------------------------------
'''
