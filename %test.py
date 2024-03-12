import turtle

def draw_square(t, width, selected=False):
    if selected:
        t.fillcolor("darkgreen")
    else:
        t.fillcolor("white")
    t.begin_fill()
    for _ in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()

def printSquares(num_squares, squares_per_row, square_width_mm, square_height_mm):
    selected_square = None

    def click_handler(x, y):
        nonlocal selected_square
        turtle.setheading(0)
        turtle.penup()
        row = int(-y // square_height_mm)
        col = int(x // square_width_mm)
        index = row * squares_per_row + col
        if index >= 0 and index < num_squares:
            if selected_square is not None:
                draw_square(turtle, square_width_mm, selected=False)
            selected_square = index
            draw_square(turtle, square_width_mm, selected=True)

    turtle.speed(0)  # Set the drawing speed to the fastest
    turtle.penup()   # Lift the pen to avoid drawing lines while positioning
    turtle.setheading(270)  # Set the initial direction downward
    turtle.goto(0, 0)  # Move to the starting position
    turtle.pendown()  # Put the pen down to start drawing

    turtle.Screen().onclick(click_handler)

    for i in range(num_squares):
        row = i // squares_per_row
        col = i % squares_per_row
        x = col * square_width_mm
        y = -row * square_height_mm  # Negative since turtle's coordinate system is flipped
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        draw_square(turtle, square_width_mm)

    turtle.hideturtle()  # Hide the turtle cursor
    turtle.done()

# Call the function with the specified parameters
printSquares(16, 5, 25, 25)
