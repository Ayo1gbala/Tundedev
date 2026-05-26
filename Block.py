def main():
    print_cube(3)

def print_cube(width):
    for n in range(width):
        print_row(width)

def print_row(width):
    print("#" * width)

main()
