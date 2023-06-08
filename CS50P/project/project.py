from rectangles import Rectangle, Square
import re
import sys

def main():
    shapes = []

    while True:
        print()
        print("[USAGE -> w x h <- where 'w' and 'h' are integers greather than 2 and less than 10]")
        print("[USAGE -> only two digits are allowed <- 02 is ok, but no 002 or 010]\n")

        try:
            exp = input('Enter dimensions and press enter or press CTRL + D to quit >> ')
        except EOFError:
            print('\n')
            break

        if valid_input(exp):
            shapes.append(rect_or_square(*get_dimensions(exp)))
            if len(shapes) >= 4:
                print("[SHAPE BAG IS FULL]")
                print()
                break
        else:
            continue

    if len(shapes) == 0:
        sys.exit()

    while True:
        print('[CHOOSE A SHAPE TO DRAW -> press 1 to 4 and enter <- or press CTRL + D to quit]')
        geometry_info(*shapes)

        try:
            n = int(input('Shape number >> '))
            if n not in range(1, 5):
                raise ValueError
        except ValueError:
            continue
        except EOFError:
            print('\n')
            break

        print()
        try:
            shapes[n - 1].get_shape_image()
            print()
            print(shape_char(shapes[n - 1]))
            print()
        except IndexError:
            continue

def valid_input(sides):
        if x := re.search(r'^(\d?\d) x (\d?\d)$', sides):
            if int(x.group(1)) not in range(2, 11) or int(x.group(2)) not in range(2, 11):
                return False
            else:
                return True
        else:
            return False

def get_dimensions(exp):
    x = re.search(r'^(\d?\d) x (\d?\d)$', exp)
    return (int(x.group(1)), int(x.group(2)))

def rect_or_square(w, h):
    if w == h:
        print()
        print('----------> SQUARE <----------')
        return Square(w)
    else:
        print()
        print('----------> RECTANGLE <----------')
        return Rectangle(w, h)

def geometry_info(*args):
    for i, shape in enumerate(args):
        print(f'Shape {i + 1}: {shape}')
    print()

def shape_char(shape):
    return {'Area' : shape.get_area(), 'Perimeter' : shape.get_perimeter(), 'Diagonal' : shape.get_diagonal()}

if __name__ == "__main__":
    main()
