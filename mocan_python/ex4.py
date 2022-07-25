file_name = "eunuexist.txt"

try:
    file = open(file_name, "r")
    file.read()
except FileNotFoundError:
    print("error reading file " + file_name)
else:
    print("closing file " + file_name)
    file.close()
finally:
    print("file closed")
