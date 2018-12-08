from MyLibrary import MyLibrary

#print(dir(MyLibrary.reboot_AP))

#print(MyLibrary.reboot_AP.__code__)

for i in dir(MyLibrary):
    if "reboot" in i.lower():
        print(i)
        print(i,eval("MyLibrary."+i+".__code__"))