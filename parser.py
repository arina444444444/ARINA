
file = open("textfile.txt")

with file as file_open:
    for line in file_open:
        for part in line.split():
            if "Error" in part:
                