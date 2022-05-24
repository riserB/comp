with open("myfile.txt","r")as f:
    data= f.readlines()
with open("myfile.txt","w")as f :
    for line in data:
             if line.strip("\n")!="Age : 20" :
                f.write(line)
