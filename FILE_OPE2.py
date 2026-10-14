file_read = open(r"C:\Users\LENOVO\OneDrive\Desktop\VS CODE\codingal.txt", "r")
print("file in read mode")
print(file_read.read())
file_read.close()

file_write = open(r"C:\Users\LENOVO\OneDrive\Desktop\VS CODE\codingal.txt", "w")
file_write.write("file in write mode")
file_write.write("hi i am pegunin i am 10000 years old")
file_write.close()

file_append = open(r"C:\Users\LENOVO\OneDrive\Desktop\VS CODE\codingal.txt", "a")
file_append.write("\n file in append mode..")
file_append.write("hi i am a old pengunie i am 1000000000 years old")
file_append.close()