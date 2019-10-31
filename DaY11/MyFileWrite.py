f_obj = open("test.txt", "w")

f_obj.write("Hello world ")
f_obj.write("This is a new text file ")
f_obj.write("Another line for checking ")
f_obj.write("Why ? becuase we can write ")

f_obj.write("Hello world \n")
f_obj.write("This is a new text file \n")
f_obj.write("Another line for checking \n")
f_obj.write("Why ? becuase we can write \n")

f_obj.close()