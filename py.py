# k1=[11,22,33,44,55]
# i1=iter(k1)
# print(next(i1))
# def fibo(n):
#     a=-1
#     b=1
#     count=0
#     while True:
#         if count>n:
#             return
#         c=a+b
#         yield c
#         a=b
#         b=c
#         count+=1
        
       
# i=fibo(5)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# def displ(a,b):
#     yield a
#     yield b
# i=displ(10,20)
# print(next(i))


# import random
# def computer(x):
#     low=1
#     high=x
#     feedback=""
#     while feedback!='c':
#         if low!=high:
#             guess=random.randint(low,high)
#         else:
#             guess=low
#         feedback=input(f"Is {guess} too high .Or too low . Or Correct")
            
#         if feedback=='h':
#             high=guess-1
#         elif feedback=='l':
#             low=guess+ 1
#     print(f"Computer guessed it right {guess}")
            
            
# computer








