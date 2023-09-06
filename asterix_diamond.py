number_of_layers = int(input("number of lines: "))

start = 0
end = number_of_layers-1
goingup = 0
goingdown = number_of_layers-1

#diamond
while (goingup < end+1):
    if (goingup < end/2):
        print((" "*goingdown) + "*" + ("*"*goingup * 2) + "*")
    else:
        print((" "*goingup) + "*" + ("*"*goingdown * 2) + "*")
    goingup += 1
    goingdown -= 1

#square
for i in range (number_of_layers):
    print("*"*number_of_layers)

#triangle
start2 = 0
end2 = number_of_layers-1
goingup2 = 0
goingdown2 = number_of_layers-1

while (goingup2 < end2+1):
    print((" "*goingdown2) + "*" + ("*"*goingup2 * 2) + "*")
    goingup2 += 1
    goingdown2 -= 1