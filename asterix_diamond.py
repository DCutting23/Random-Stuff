number_of_layers = 30

start = 0
end = number_of_layers
goingup = 0
goingdown = number_of_layers

while (goingup < end+1):
    if (goingup < end/2):
        print((" "*goingdown) + "*" + (" "*goingup * 2) + "*")
    else:
        print((" "*goingup) + "*" + (" "*goingdown * 2) + "*")
    goingup += 1
    goingdown -= 1