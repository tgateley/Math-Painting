from classes import Rectangle, Canvas, Square

# get the canvas width and height from the user
canvas_height = int(input("How many pixels tall do you want your canvas: "))
canvas_width = int(input("How many pixels wide do you want your canvas: "))
answer = input("Do you want to customize the color of the canvas, Yes or No: ")

match answer:
    case "Yes":
        # Gets Canvas data from the user
        canvas_red = int(input("Enter the number for Red (0-255): "))
        canvas_green = int(input("Enter the number for Green (0-255): "))
        canvas_blue = int(input("Enter the number for Blue (0-255): "))

        # creates the canvas object
        canvas = Canvas(height=canvas_height, width=canvas_width,
                        color=(canvas_red, canvas_green, canvas_blue))

    case "No":
        # Creates a white canvas object
        canvas = Canvas(height=canvas_height, width=canvas_width, color=(255, 255, 255))

while True:
    shape = input("Do you want to draw a rectangle or a square or quit? ")

    match shape:
        case "rectangle":
            # Gets the rectangle data from the user
            x = int(input('Give the X-Coordinate of the rectangle: '))
            y = int(input("Give the Y-Coordinate of the rectangle: "))
            rect_width = int(input("How many pixels wide is the rectangle: "))
            rect_height = int(input("How many pixels high is the rectangle: "))
            rect_red = int(input("Enter the number for Red (0-255): "))
            rect_green = int(input("Enter the number for Green (0-255): "))
            rect_blue = int(input("Enter the number for Blue (0-255): "))

            # Create the rectangle
            r1 = Rectangle(x=x, y=y, height=rect_height, width=rect_width,
                           color=(rect_red, rect_green, rect_blue))
            r1.draw(canvas)

        case "square":
            # Gets the square data from the user
            x = int(input('Give the X-Coordinate of the square: '))
            y = int(input("Give the Y-Coordinate of the square: "))
            side = int(input("How many pixels is the side of the square: "))
            square_red = int(input("Enter the number for Red (0-255): "))
            square_green = int(input("Enter the number for Green (0-255): "))
            square_blue = int(input("Enter the number for Blue (0-255): "))

            # Create the square
            s1 = Square(x=x, y=y, side=side, color=(square_red, square_green, square_blue))
            s1.draw(canvas)

        case "quit":
            # User inputs image name
            image_name = input("Give your picture a name(no spaces): ")
            # Creates image
            canvas.make(f'{image_name}.png')
            break



