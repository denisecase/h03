input = open("d.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("    ")
    date, time,location, dept, amount, paymentType = datalist
    output.write(location + "\t" + amount + "\n")

input.close()
output.close()