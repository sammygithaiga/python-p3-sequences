def print_fibonacci(length):
    
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibonacci_sequence = [0, 1] 
        for i in range(2, length):
            next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_fibonacci)
        print(fibonacci_sequence)
