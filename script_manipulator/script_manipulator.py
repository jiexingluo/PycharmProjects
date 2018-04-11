import linecache
import glob
filename = glob.glob("*.txt")

with open(filename[0], "r+",encoding="utf-8") as f:
    i = 3
    j = 4
    lines = len(f.readlines())+1
#    print(lines)
#    print(linecache.getline("test.txt",3))
    sch_text = "\n"
    eng_text = "\n"
    while i <lines:
        ctext = linecache.getline(filename[0],i)
        #ctext = ctext.replace("\r\n","")
        #ctext = ctext.replace("\r", "")
        ctext = ctext.replace("\n", " ")
        sch_text += ctext
        i += 5
    print(sch_text)
    while j < lines:
        etext = linecache.getline(filename[0], j)
        # etext = etext.replace("\r\n","")
        # etext = etext.replace("\r", "")
        etext = etext.replace("\n", " ")
        eng_text += etext
        j += 5
    print(eng_text)
    f.write(sch_text)
    f.write(eng_text)
#    for line in f:
#        print(line= 1, end="")

#print(file.name)

#file.close()
