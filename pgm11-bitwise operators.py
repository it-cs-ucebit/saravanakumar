x = 60            # 60 = 0011 1100 
y = 13            # 13 = 0000 1101 
z = 0

z = x & y;        # 12 = 0000 1100
print (" Bitwise AND ", z)

z = x | y;        # 61 = 0011 1101 
print (" Bitwise OR ", z)

z = x ^ y;        # 49 = 0011 0001
print (" Bitwise XOR ", z)

z = ~x;           # -61 = 1100 0011
print (" Bitwise Ones Complement ", z)

z = x << 2;       # 240 = 1111 0000
print (" Bitwise Left Shift Operator ", z)

z = x >> 2;       # 15 = 0000 1111
print (" Bitwise Right Shift Operator", z)
