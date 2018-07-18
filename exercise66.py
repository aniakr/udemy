temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

# file_temp=open ("file_temp.txt",'w')
# for t in temperatures:
#    if type(c_to_f(t))==float:
#        file_temp.write((str(c_to_f(t))+"\n"))
# file_temp.close()


with open("file_temp.txt","w") as myfile:
    for t in temperatures:
        if type(c_to_f(t)) == float:
            myfile.write((str(c_to_f(t)) + "\n"))