import turtle as t 
import colorgram


def fetch_colors(image,number_of_colors):
    colors = colorgram.extract(image, number_of_colors)
    colors_list = []
    for i in range(number_of_colors):
        colors_list.append(colors[i])

    return colors_list


fetch_colors("painting.jpeg", 6)

