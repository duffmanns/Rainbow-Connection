# This is the main script to run.
# This program demonstrates how a color is identified from an image.

from PIL import Image
import closestcolorname


def color_scan(img):
    """
    Calculate top 2 occurring colors.
    @param img: Actual RGB image
    @return int[]: RGB values of 2 highest occurring colors
    """

    width, height = img.size
    r_list = []
    g_list = []
    b_list = []
    totals = []
    final_r = []
    final_g = []
    final_b = []

    # Create array with every pixel in the image.
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_list.append(r)
            g_list.append(g)
            b_list.append(b)

    # Makeshift queue. Always get the first RGB combo. Check for other similar colored pixels
    while len(r_list) != 0:
        pointer = 0
        count = 0
        final_r.append(r_list[pointer])
        final_g.append(g_list[pointer])
        final_b.append(b_list[pointer])
        # Iterate list. If I find a similar pixel, count it and delete it. Else leave it
        while pointer != len(r_list):
            if abs(final_r[len(final_r)-1] - r_list[pointer]) < 11 and \
            abs(final_g[len(final_g)-1] - g_list[pointer]) < 11 and \
            abs(final_b[len(final_b)-1] - b_list[pointer]) < 11:
                count+=1
                del r_list[pointer]
                del g_list[pointer]
                del b_list[pointer]
            else:
                pointer+=1
        totals.append(count)

    # Get the RGB combo with the highest count in the list. Delete it run again to get the secondary color
    first = final_r[totals.index(max(totals))], final_g[totals.index(max(totals))], final_b[totals.index(max(totals))]
    del final_r[totals.index(max(totals))], final_g[totals.index(max(totals))], final_b[totals.index(max(totals))]
    second = final_r[totals.index(max(totals))], final_g[totals.index(max(totals))], final_b[totals.index(max(totals))]
    return first[0], first[1], first[2], second[0], second[1], second[2]


def closest_color(most_color):
    """
    Find closest derived color names.
    @param most_color: 
    @return first_color_name:
    @return second_color_name:
    """
    r1 = int(most_color[0])
    g1 = int(most_color[1])
    b1 = int(most_color[2])
    r2 = int(most_color[3])
    g2 = int(most_color[4])
    b2 = int(most_color[5])
    first = (r1, g1, b1)
    second = (r2, g2, b2)
    print "Colors in RGB:", first, "and", second
    first_color_name = closestcolorname.get_colour_name(first)
    second_color_name = closestcolorname.get_colour_name(second)

    return first_color_name, second_color_name


def get_comp(c_color):
    """
    Finding complimentary colors
    @param c_color:
    @return colors:
    """
    colors = [255-c_color[0], 255-c_color[1], 255-c_color[2], 255-c_color[3], 255-c_color[4], 255-c_color[5]]

    return colors


def commute_result(img):
    """
    Converting image of any form to RGB image get 2 highest used colors and print result.
    @param img: 
    """
    img = img.convert('RGB')
    most_color = color_scan(img)
    color_names = closest_color(most_color)
    print "The primary colors in your image are", color_names[0], "and", color_names[1]

    c_color = get_comp(most_color)
    color_names = closest_color(c_color)
    print "The complimentary colors in your image are", color_names[0], "and", color_names[1]


# The blue_white_dot.png image is a blue field with a little white and red in it
# It comes in the package as a demo file to input
# commute_result(img)

my_file = raw_input("Enter Image to be scanned: ")
print(my_file)

img = Image.open(my_file)
commute_result(img)
