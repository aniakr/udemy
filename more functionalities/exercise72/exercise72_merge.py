from datetime import datetime
filename=datetime.now()
filename=filename.strftime("%Y-%m-%d-%H-%M")

with open(filename+".txt","w") as merge:
    for file in range(1,4):
        with open("file"+str(file)+".txt","r") as myfile:
            merge.write(myfile.read()+"\n")



# import glob2
# from datetime import datetime
#
# filenames = glob2.glob("*.txt")
# with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as file:
#     for filename in filenames:
#         with open(filename, "r") as f:
#             file.write(f.read() + "\n")