def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    elif n == 3:
        return [signature[0], signature[1], signature[2]]
    else:
        tribonacci_list = [signature[0], signature[1], signature[2]]
        for i in range(3, n):
            tribonacci_list.append(tribonacci_list[i-3] + tribonacci_list[i-2] + tribonacci_list[i-1])
        return tribonacci_list

print(tribonacci([1, 1, 1], 10))