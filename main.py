from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from user
canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))

# Make a directory of color codes
colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input('Enter canvas color (black or white): ')

#Create a canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input('What do you like to draw? Enter quit to quit. ')
    while shape_type.lower() != 'rectangle' and shape_type.lower() != 'square' and shape_type.lower() != 'quit':
        shape_type = input('Please enter a valid shape(rectangle or square) or quit: ')

    #Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == 'rectangle':
        rec_x = int(input('Enter x of the rectangle: '))
        rec_y = int(input('Enter y of the rectangle: '))
        rec_width = int(input('Enter width of the rectangle: '))
        rec_height = int(input('Enter height of the rectangle: '))
        red = int(input('How much red should the rectangle have?  '))
        green = int(input('How much green should the rectangle have? '))
        blue = int(input('How much blue should the rectangle have? '))
        r1 = Rectangle(rec_x, rec_y, rec_height, rec_width, (red, green, blue))
        r1.draw(canvas)

    # Ask for square data and create rectangle if user entered 'square'
    if shape_type.lower() == 'square':
        sqr_x = int(input('Enter x of the square: '))
        sqr_y = int(input('Enter y of the square: '))
        sqr_side = int(input('Enter lenght of the square: '))
        red = int(input('How much red should the square have?  '))
        green = int(input('How much green should the square have? '))
        blue = int(input('How much blue should the square have? '))
        s1 = Square(sqr_x, sqr_y, sqr_side, (red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == 'quit':
        break

canvas.make('Image.png')