def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's Triangle

    for i in range(1, n):
        row = [1]  # First element of the row is always 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it in the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of the row is always 1
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    from 0-main import print_triangle
    print_triangle(pascal_triangle(5))
