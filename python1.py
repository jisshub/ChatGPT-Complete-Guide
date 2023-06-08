# Given coordinates of a point (x,y) in 2D plane, find in which quadrant does this point lie.
# Input format
# First line contains 2 space separated real numbers - x coordinate, y coordinate.

# Output format
# Print 1, 2, 3 or 4 depending on in which quadrant does the point lie.

# Sample Input 1
# -5.5 2

# Sample Output 1
# 2

def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

print(quadrant(-5.5, 2))


# 
