def generate_complex_case(N, W):
    numbers = []
    current_num = 0
    for i in range(N):
        numbers.append(str(current_num))
        
        if i % 2 == 0:
            current_num += 1
        else:
            current_num += W + 1
    
    return numbers

N, W = 100000, 1000000
P  = generate_complex_case(N, W)
