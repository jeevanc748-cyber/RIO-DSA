square = [1,4,16,25]
print(square)
square = [2,4,6,8]
print(square[1])
square = [1,3,5,6,7]
square[1] = 100
print(square)
square = [1,4,8,9]
print(square[:-3])
print(square[-3:])
square = [2,4,6,8,10]
square = square + [12,14,16,18,20]
print(square)
cubes = [1,8,27,65,125]
cubes[3] = 64
print(cubes) 
cubes = [1,8,27,65,125]
cubes.append(64)
print(cubes)
rgb = ["red","blue","green"]
rgba = rgb
rgba.append("yellow")
print(rgba)