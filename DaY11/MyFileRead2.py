file = open ("test.txt", "r")

'''s=file.readlines()
for line in s:
    print(line)'''
for line in file:
    print(line)
file.close()