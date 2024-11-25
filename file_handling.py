fp=open("abc.txt","r")
# print(fp.read(15))
# print(fp.readline())
while True:
    s1=fp.readline()
    if s1=="":
        break
    print(s1,end="")




fp.close()