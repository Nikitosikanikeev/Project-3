
with open('/Users/Huawei/Desktop/lesson.txt', "r", encoding="utf8") as file:
    for line in file:
        line = line.lstrip()
        line = line.rstrip()
        print(line)
file.close()
