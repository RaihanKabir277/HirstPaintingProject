
import colorgram

colors = colorgram.extract('image.jpg',30)

# for color in colors:
#     print(color.rgb)   #its a one way 


rgb_colors = []

for color in colors:
    actions_tuple = (color.rgb.r,color.rgb.g,color.rgb.b) 
    rgb_colors.append(actions_tuple)

    #   below line one give us the all Rgb color rest 3 line is for separetly retrive the r , g and b color for each portion...
    # rgb_colors.append(color.rgb)
    # rgb_colors.append(color.rgb.r)
    # rgb_colors.append(color.rgb.g)
    # rgb_colors.append(color.rgb.b)

print(rgb_colors)

