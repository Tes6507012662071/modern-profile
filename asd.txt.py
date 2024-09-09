f = open("demo.txt","r")
print(f.read())

f.close()
    
    
    
    
    
for data in f:
     print(data.strip())

f.close()


f = open("demon.txt", "w")
f.write("555555")
f.write("6666666")
f.write("77777777\n")

f.close()


f = open("demo2.txt", "a")
f.write("this is a new file with mode w")
f.close ()

f.opem("demo3.txt", "a")
f.write("this is a new file with mode a")
f.close()

with open('demo4.txt','w') as f:
    f write("when we open file with open ()\m open ")