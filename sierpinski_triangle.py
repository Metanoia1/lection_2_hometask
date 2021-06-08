import turtle


def draw_triangle(order=1, step=50, angle=-60, turn=1):

    if order == 0:
        return

    if turn == 1:
        move = turtle.left

    if turn == -1:
        move = turtle.right

    draw_triangle(order - 1, step=step, angle=angle, turn=-turn)
    turtle.forward(step)
    move(angle)
    draw_triangle(order - 1, step=step, angle=-angle, turn=-turn)
    turtle.forward(step)
    move(angle)
    draw_triangle(order - 1, step=step, angle=angle, turn=-turn)


def draw_triangle_in_one_direction(order=1, step=50, angle=-60, turn=1):

    if order % 2 == 0:
        turtle.setheading(0)
    else:
        turtle.setheading(60)

    draw_triangle(order=order, step=step, angle=angle, turn=turn)


def main(order=1, step=250, angle=-60, turn=1, x=-250, y=-250):

    turtle.tracer(1, 0)
    step = step / (2 ** (order - 1))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_triangle_in_one_direction(order=order, step=step, angle=angle, turn=turn)
    turtle.forward(step)
    turtle.done()


if __name__ == "__main__":
    ORDER = 0

    while ORDER < 1 or ORDER > 10:
        ORDER = input("Enter the 'ORDER' value: ")

        if ORDER.isdigit():
            ORDER = int(ORDER)
        else:
            ORDER = 0

    main(order=ORDER)
