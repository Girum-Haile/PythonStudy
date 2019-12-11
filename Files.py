# open file
newFile = open("file.txt", 'w')
# write to file
newFile.write("hello i am Girum ")
newFile.write("i am learning python ")
newFile.close()
# append
newFile = open("file.txt", 'a')
newFile.write("i love Pyhton")
newFile.close()
# read from file
newFile = open("file.txt", 'r+')
txt = newFile.read(100)
print(txt)
