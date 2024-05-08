import time

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

def perform_operations(stack, num_operations):
    for i in range(num_operations):
        stack.push(i)
    for _ in range(num_operations):
        stack.pop()

stack = Stack()

num_operations = 100000

start_time = time.time()
perform_operations(stack, num_operations)
end_time = time.time()

total_time = end_time - start_time
average_time_per_operation = total_time / (num_operations * 2)

print(f"Total time for {num_operations * 2} operations: {round(total_time, 5)} seconds")
print(f"Average time per operation: {round(average_time_per_operation, 5)} seconds")
