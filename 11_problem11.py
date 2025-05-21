with open("anu.txt") as f:
    content = f.read()

with open("renamed.txt", "w") as f:
    f.write(content)

