f = open("word.txt", "w")
f.write("Zdravo, to je besedilo, ki ga bom zapisal v datoteko.")
f.close()

with open("word.txt", "r") as f:
    content = f.read()
    print(content)


with open("word.txt", "a") as f:
    f.write("\nTo je dodano besedilo na koncu datoteke.")


with open("word.txt", "r") as f:
    content = f.read()
    print(content)


with open("word.txt", "r") as f:
    lines = f.readlines()
    print(lines)
