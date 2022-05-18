#function:
def fapp(str):
    f=open("ashu.txt",'a+')
    f.write("ashu")
    f.seek(0,0)
    str=f.read()
    print(str)
    f.close()

#main:
fapp(str)
