f = open("Faust.txt", "r")
o = open("output_final.txt", "w")


d = {"Zueignung:":0}
r = f.readlines()

last_Charakter = "Zueignung:"

for line in r:
    line = line.strip()
    line2 = line.split()
    if line == "":
        pass
    elif(line2[0].isupper() and len(line2[0])> 1):
        if(line in d):
            last_Charakter = line
            pass
        else:
            d.update({line:0})
            last_Charakter = line
    else:
        d[last_Charakter] += 1
d2 = {}

for element in d:
    element2 = element.split()
    if element2[0][-1] == ":":
        keyname = element2[0]
    else:
        keyname = element2[0] + ":"
        
    if keyname in d2:
        d2[keyname] += d[element]
    else:
        d2.update({keyname:d[element]})



counter = 0
for element in d:
    counter += d[element]

o.write("Insgesamt: " + str(counter)+ "\n")

for element in d2:
    prozent = d2[element] / counter
    prozent = prozent * 100
    prozent = round(prozent, 2)
    o.write(element + " " + str(d2[element]) + " - " + str(prozent) + "%" "\n" )

