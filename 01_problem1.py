f = open("poem.txt")
content = f.read()
if("johny" in content):
    print("The johny is present in the content.")
else:
    print("The johny is not present in the content.")

f.close()