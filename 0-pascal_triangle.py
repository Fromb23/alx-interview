def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle
    else:
        triangle.append([1])
        for i in range(1, n):
            prev_row = triangle[i - 1]
            new_row = [1]

            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
                
            new_row.append(1)
            triangle.append(new_row)

    return triangle
