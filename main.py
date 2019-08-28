import numpy as np
import cv2

# NOTE: cv2 uses BGR, not RGB!
# Load an color image in
# img = cv2.imread('lib/r_place.png')
img = cv2.imread('lib/test_1.png')
ny = np.shape(img)[0]
nx = np.shape(img)[1]

# Define colors
RED1 = np.array([   0,   0, 255 ])
GRN1 = np.array([   0, 255,   0 ])
BLU1 = np.array([ 255,   0,   0 ])
BLU2 = np.array([ 255, 255,   0 ])
WHT1 = np.array([ 255, 255, 255 ])
BLK1 = np.array([   0,   0,   0 ])


# List of bricks to use ordered by least to greatest area
B01 = np.array([ 1 , 1 ])
B02 = np.array([ 2 , 1 ])
B03 = np.array([ 1 , 2 ])
B04 = np.array([ 3 , 1 ])
B05 = np.array([ 1 , 3 ])
B06 = np.array([ 4 , 1 ])
B07 = np.array([ 1 , 4 ])
B08 = np.array([ 2 , 2 ])
B09 = np.array([ 2 , 3 ])
B10 = np.array([ 3 , 2 ])
B11 = np.array([ 2 , 4 ])
B12 = np.array([ 4 , 2 ])
B13 = np.array([ 2 , 6 ])
B14 = np.array([ 6 , 2 ])
B15 = np.array([ 2 , 8 ])
B16 = np.array([ 8 , 2 ])

REAL_BRICKS = [B16,B15,B14,B13,B12,B11,B10,B09,B08,B07,B06,B05,B04,B03,B02,B01]


bricks = np.zeros((ny,nx), dtype=int)
brick_idx = 1

for y in range(0,ny):
    print(y)
    for x in range(0,nx):
        if bricks[y][x] == 0:

            for BRICK in REAL_BRICKS :
                # Check brick 5
                target_count = BRICK[0]*BRICK[1]
                actual_count = 0

                if y+BRICK[0] > ny:
                    yy_lim = y
                else:
                    yy_lim = y+BRICK[0]

                if x+BRICK[1] > nx:
                    xx_lim = x
                else:
                    xx_lim = x+BRICK[1]

                for yy in range(y,yy_lim):
                    for xx in range(x,xx_lim):
                        if np.all(img[y][x] == img[yy][xx]) and bricks[yy][xx] == 0:
                            actual_count += 1

                # If the corner pixel supports the brick, assign a new brick index
                if actual_count == target_count:
                    for yy in range(y,yy_lim):
                        for xx in range(x,xx_lim):
                            bricks[yy][xx] = brick_idx
                    brick_idx += 1
                    break

print("\n\n")
for y in range(0,ny):
    for x in range(0,nx):
        if bricks[y][x] < 10:
            print("0",end="")
        print(bricks[y][x],end=" ")
    print("")

print("")
print(brick_idx-1)




#end
