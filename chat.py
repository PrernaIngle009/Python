responses=["Hello,My name is Robot","How may i help you?","Thank You","Bye-Bye",
           "Sorry,I dont Know this","But Next time i will surely do for you"]
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def powe(a,b):
    return a**b
def end():
    print(responses[2])
    print(responses[3])
def extract_num(text):
    l1=[]
    for w in text.split():
        try:
            l1.append(float(w))
        except:
            pass
    return l1
def ajay():
    print("Ajay is student of Coding Seekho,And he is in 2nd year")
    
operations={"ADDITION":add,"ADD":add,"SUM":add,"PLUS":add,"SUB":sub,"MINUS":sub,"POWER":powe}
commands={"AJAY":ajay,"BYE":end,"BYE BYE":end,"EXIT":end,"STOP":end}
