f = open("file.txt")
print(f.read())
f.close()

# the same can be written using 'with' statement like this:
with open("File.txt") as f:
    print(f.read())

# you don't have to explicity close the file