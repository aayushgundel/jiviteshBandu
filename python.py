def calculate_area(length, width):
    return length * width


if __name__ == "__main__":
    
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    
    area = calculate_area(length, width)

    
    print(f"The area of the rectangle with length {length} and width {width} is {area}")
