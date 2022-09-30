strings = []
while True:
    strings.append(input("Enter a string: "))
    if strings[len(strings)-1] =="STOP" or strings[len(strings)-1]=="stop":
        break
    for i in range(len(strings)-1,0,-1):
        if len(strings[i]) > len(strings[i-1]):
            strings[i],strings[i-1] = strings[i-1],strings[i]
print(f"{strings[0]} {strings[len(strings)-2]}")