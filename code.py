#Wheat and chessboard

#The formula follows, take a chessboard of 64 squares, place 1 grain of wheat on the first square, 2 on the second, 4 on the third 8 on the fourth and so on.

#64 squares
#wheat calculated in 2 to the power of the number on the square.

i = 0
squares = 64
total = 0

#In range command starts actually gives the numbers from 0, which is ideal 
for i in range(squares):
    wheat = 2**i
    print("square: " + str(i) + " " + "wheat: " + str(wheat))
    total += wheat
print("total amount of wheat: " + str(total)) # can be represented as (2**64) -1