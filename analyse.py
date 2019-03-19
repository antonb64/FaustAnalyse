f = open("Faust.txt", "r")
o = open("output3.txt", "w")
d = {"Zueignung:":0}
r = f.readlines()

last_Charakter = "Zueignung:"

for line in r:
    line = line.strip()
    if line == "":
        pass
    elif(line.isupper()):
        if(line in d):
            last_Charakter = line
            pass
        else:
            d.update({line:0})
            last_Charakter = line
    else:
        d[last_Charakter] += 1

counter = 0
for element in d:
    counter += d[element]

o.write("Insgesamt: " + str(counter)+ "\n")

for element in d:
    prozent = d[element] / counter
    prozent = prozent * 100
    prozent = round(prozent, 2)
    o.write(element + " " + str(d[element]) + " - " + str(prozent) + "%" "\n" )
print(d)
