studentsname = ["Betasa", "Esata", "Sata", "Ata", "ta"]

ask = input("Who do you want to find:")

found = False
for stu in studentsname:
    if stu == ask:
        found = True
        break

if found:
    print(ask, "found in the list")
else:
    print(ask, "not found in the list")