myfile = open("my_new_text_file.text", "w")
for i in range(10):
    myfile.write(str(i))
    myfile.write("\n")

myfile.close()
