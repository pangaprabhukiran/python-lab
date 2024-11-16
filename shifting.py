import string
def shift(word,value):
    letters=string.ascii_uppercase
    new=' '
    for i in range(len(word)):
        if word[i] in letters:
            index=letters.index(word[i])
            new=new+letters[(index+value)%26]
        else:
            new=new+word[i]
    return new
word=input("enter your name")
print(shift(word,2))
