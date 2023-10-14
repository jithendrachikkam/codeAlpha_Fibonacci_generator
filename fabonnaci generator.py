def fibonacci_generator(n):
    fib_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two terms
    if n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    else:
        for i in range(2, n):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]  # Compute the next Fibonacci number
            fib_sequence.append(next_fib)  # Append the next Fibonacci number to the sequence
        return fib_sequence

# Example usage
n = 25
fib_sequence = fibonacci_generator(n)
print(fib_sequence)
