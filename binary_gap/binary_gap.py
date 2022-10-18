def solution(N):
    binary = []
    binary_gap = 0
    max_binary_gap = 0
    while N >= 1:
        binary.append(N%2)
        N = N//2
        print(binary)
    for i in range(len(binary), 0, -1):
        if binary[i-1] == 0:
            binary_gap = binary_gap + 1
            print(i)
        else:
            if (binary_gap > max_binary_gap):
                max_binary_gap = binary_gap
            binary_gap = 0
        print(binary_gap, "gap")
    print("end: ", max_binary_gap)
    pass

N = input("N: ")
solution(int(N))
