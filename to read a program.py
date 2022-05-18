#function:
def fread(str):
    f=open("vishal.txt",'r')
    str=f.read()
    print(str)
    f.close()

#mains:
fread(str)
