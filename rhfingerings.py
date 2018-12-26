import sys
sys.stdout = open("coins.lp", "w")
s = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 3,
    6: 2,
    7: 1,
    8: 2,
}
b = {}
for i in range(1,len(s)+1):
    if s[i]<=3:
        b[i] = 1
    else:
        b[i] = 0
print("Minimize")
for i in range(1,len(s)+1): # objective function
    print("\t0 F" + str(i) + " +")
for i in range(1,len(s)+1): # objective function
    if i != len(s):
        print("\tPBC"+str(i)+" + PT"+str(i)+" + .5 PF"+str(i)+ " + PB" + str(i) + " +")
    else:
        print("\tPBC"+str(i)+" + PT"+str(i)+" + .5 PF"+str(i)+ " + PB" + str(i))
print("Subject To")
for i in range(1,len(s)+1):
    if b[i] == 1:
        print("\tF"+str(i)+" + PT"+str(i)+" <= 3")
for i in range(1,len(s)+1):
    print("\tF"+str(i)+" - " +str(s[i]) + " - 100 T" + str(i) + " - PF" + str(i) + " <= 0")
for i in range(1,len(s)+1):
    print("\t" + str(s[i]) + " - F"+str(i) + " - 100 T" + str(i) + " - PF" + str(i) + " <= 0")
for i in range(1,len(s)+1):
    print("\tF"+str(i)+" - T" + str(i)+ " <= 3")
for i in range(1,len(s)+1):
    print("\t4 T"+str(i)+" - F"+str(i)+" <= 0")
for i in range(1,len(s)):
    d = s[i] - s[i+1]
    print("\t"+str(-d) + " F" + str(i) + " + " + str(d) + " F" + str(i+1) + " - 100 PBC" + str(i) + " <= 0")
for i in range(1,len(s)):
    print("\tF" + str(i) + " - F" + str(i+1) + " - 100 Y" + str(i) + " <= -.5")
for i in range(1,len(s)):
    print("\tF" + str(i) + " - F" + str(i+1) + " - 100 Y" + str(i) + " >= -99.5")
for i in range(1,len(s)-2):
    print("\tF" + str(i) + " + F" + str(i+1) + " + F" + str(i+2) + " >= 5")
for i in range(1,len(s)+1):
    if s[i] == 6:
        print("\tF"+str(i)+" - PB" + str(i) + " >= 4")
for i in range(1,len(s)+1):
    if s[i] == 5:
        print("\tF"+str(i)+" - PB" + str(i) + " >= 4")
print("Bounds")
for i in range(1,len(s)+1):
    print("\t1 <= F" + str(i) + " <= 4")
for i in range(1,len(s)+1):
    print("\t0 <= T" + str(i) + " <= 1")
for i in range(1,len(s)+1):
    print("\t0 <= PBC" + str(i) + " <= 1")
for i in range(1,len(s)+1):
    print("\t0 <= PT" + str(i) + " <= 1")
for i in range(1,len(s)+1):
    print("\t0 <= PB" + str(i) + " <= 1")
for i in range(1,len(s)+1):
    print("\t0 <= PF" + str(i) + " <= 5")
for i in range(1,len(s)+1):
    print("\t0 <= Y" + str(i) + " <= 1")
print("Integers")
for i in range(1,len(s)+1):
    print("\tF" + str(i))
for i in range(1,len(s)+1):
    print("\tT" + str(i))
for i in range(1,len(s)+1):
    print("\tPBC" + str(i))
for i in range(1,len(s)+1):
    print("\tPB" + str(i))
for i in range(1,len(s)+1):
    print("\tPT" + str(i))
for i in range(1,len(s)+1):
    print("\tPF" + str(i))
for i in range(1,len(s)+1):
    print("\tY" + str(i))
print("End")