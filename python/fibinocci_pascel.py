def generate_pascals_triangle(rows):
    triangle = [[1] * (row + 1) for row in range(rows)]
    
    for i in range(2, rows):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
    return triangle

def fibonacci_from_pascals_triangle(triangle):
    fibonacci_sequence = [sum(diagonal) for diagonal in triangle]
    return fibonacci_sequence

# Example usage to generate Fibonacci numbers using Pascal's Triangle
rows = 10
pascals_triangle = generate_pascals_triangle(rows)
fibonacci_sequence = fibonacci_from_pascals_triangle(pascals_triangle)

print("Pascal's Triangle:")
for row in pascals_triangle:
    print(row)

print("\nFibonacci Sequence:")
print(fibonacci_sequence)
