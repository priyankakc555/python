a="\" Python + is + an + awesome +language\""
b=a.split("+")
print(b)

c=("").join(b)
print (c)

#2
a=str(input("enter the word:"))
b=list(a)
print(b)
c=list(enumerate(b))
print(c)

#4
a=input("enter the word :")
b=input("enter the second word :")
if sorted(a)==sorted(b):
    print("the words are anagram")
else:
    print("the words are not anagram")

 #5
    a=(input ("enter a 3 digit number:"))
    if sorted(a)==sorted(a,reverse=True):
        print('the numbners are palindrome')
    else:
        print("the numbers are not palindrome")

   
