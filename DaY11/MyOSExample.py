import os
#os.rmdir("fff")

#os.mkdir ("d:\\tempdir")
#os.chdir("d:\\tempdir")
#print(os.getcwd())
#print(os.listdir("D:\\Imam"))
#os.rmdir("d:\\tempdir")

if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("there is no file")

import sys
print(sys.path)