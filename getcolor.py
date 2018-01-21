# This is the main script to run.
# This program demonstrates how a color is identified from an image.

from PIL import Image
import closestcolorname


def avg_img_color(img):
    """
    Calculate average of individual red, green and blue colors.
    @param img: Actual RGB image
    @return int, int, int: Three average integer values of red, green and blue pixels respectively.
    """

    # In progress: Calculate top 2 occurring colors
    # @param img: actual rgb image
    # @return object, object: 2 highest occurring colors

    width, height = img.size
    r_list = []
    g_list = []
    b_list = []
    totals = []
    final_r = []
    final_g = []
    final_b = []

    each_pixel = []
    pixel_list = []
    pixel_totals = []


    # Compute total count of red, green and blue color pixel.
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_list.append(r)
            g_list.append(g)
            b_list.append(b)
            each_pixel.append(img.getpixel((x,y)))

    while len(r_list) != 0:
        pointer = 0
        count = 0
        final_r.append(r_list[pointer])
        final_g.append(g_list[pointer])
        final_b.append(b_list[pointer])
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

    print("R List ", final_r)
    print("G List ", final_g)
    print("B List ", final_b)
    print("Counts ", totals)

    first = final_r[totals.index(max(totals))], final_g[totals.index(max(totals))], final_b[totals.index(max(totals))]
    print(first)
    del final_r[totals.index(max(totals))], final_g[totals.index(max(totals))], final_b[totals.index(max(totals))]
    second = final_r[totals.index(max(totals))], final_g[totals.index(max(totals))], final_b[totals.index(max(totals))]
    print(second)
    # Get a pixel from list. Count how often something like it shows up
    # while len(each_pixel) != 0:
    #     my_pixel = each_pixel[0]
    #     count = each_pixel.count(my_pixel)
    #     print("Current count", count)
    #     for x in range(0, count):
    #         del each_pixel[each_pixel.index(my_pixel)]
    #     pixel_list.append(my_pixel)
    #     pixel_totals.append(count)

        #r, g, b = my_pixel
        #for x in range(0, len(each_pixel)):
         #   this_r, this_g, this_b = each_pixel(x)

    # print(pixel_list)
    # print(pixel_totals)
    # comp = (255, 255, 255)
    # print(pixel_list.count(comp))
    return first[0], first[1], first[2], second[0], second[1], second[2]


def closest_color(most_color):
    """
    To find actual color name. If actual color name is unknown then derive closest one. 
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
    print "RGB ", first, " and ", second
    first_color_name = closestcolorname.get_colour_name(first)
    second_color_name = closestcolorname.get_colour_name(second)

    return first_color_name, second_color_name


def commute_result(img):
    """
    Converting image of any form to RGB image and print result.
    @param img: 
    """
    img = img.convert('RGB')
    most_color = avg_img_color(img)
    color_names = closest_color(most_color)
    print "The primary colors in your image are ", color_names[0]


# The redball.jpg image has a red colored ball with white background. Hence, closest color name is derived as
# lightcoral. light coral has approx 94% red, 50% green and 50% blue.
# img = Image.open("redball.jpg")
# commute_result(img)

# While the red.png is a fully red colored image. Hence, red color is derived.
img = Image.open("blue_white_dot.png")
commute_result(img)
