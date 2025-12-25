with open("clients.csv", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

with open("adult_clients.csv", "w", encoding="utf-8") as output_file:
    output_file.write("name,age\n")

    for line in lines[1:]:
        name, age = line.strip().split(",")

        if int(age) >= 18:
            output_file.write(f"{name},{age}\n")