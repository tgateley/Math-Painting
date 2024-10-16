from classes import Rectangle, Canvas, Square


canvas_height = int(input("How many pixels tall do you want your canvas: "))
canvas_width = int(input("How many pixels wide do you want your canvas: "))
answer = input("Do you want to customize the color of the canvas, Yes or No: ")

match answer:
    case "Yes":
        canvas_red =
        canvas_green = int(input("Enter the number for Red (0-255): "))


canvas = Canvas(height=canvas_height, width=canvas_width, color=(255, 255, 255))
r1 = Rectangle(x=1, y=6, height=7, width=18, color=(100, 200, 125))
r1.draw(canvas)
canvas.make('canvas.png')
