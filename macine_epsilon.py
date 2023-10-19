def main():
    import sys
    print(sys.float_info.epsilon)
    print(type(sys.float_info.epsilon))
    print_epsilon()

    x = 1.0
    y = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1

    print(x == y)

    print(f"x is {x}")
    print(f"y is {y}")

    print(is_same_number(x, y))

def is_same_number(x:float, y:float) -> bool:
    import sys
    return abs(x - y) <= sys.float_info.epsilon * max(abs(x),abs(y))

def print_epsilon() -> None:
    my_epsilon = 1
    while my_epsilon + 1 != 1 :
        my_epsilon /= 2
    print(my_epsilon*2)

if __name__ == "__main__":
    main()
