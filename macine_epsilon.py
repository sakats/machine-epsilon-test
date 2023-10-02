def main():
    import sys
    print(sys.float_info.epsilon)
    print(type(sys.float_info.epsilon))

    x = 1.0
    y = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
    print(is_same_number(x, y))

def is_same_number(x:float, y:float) -> bool:
    import sys
    return x - y <= sys.float_info.epsilon

if __name__ == "__main__":
    main()
