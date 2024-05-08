def actual_cost(number):
    result = number ^ number-1
    return bin(result).count('1')

n = int(input('enter increments: '))
print("Operation | Counter State | Actual Cost | Potential | Amortized Cost")
for i in range(n):
    print(f"{i + 1:9} | {bin(i+1)[2:]:13} | {actual_cost(i+1):11} | {bin(i+1).count('1'):9} | {2:14}")