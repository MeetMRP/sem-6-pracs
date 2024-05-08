class StackSimulator:
    def __init__(self):
        self.items = []
        self.amortised_cost = 0
        self.potential = 0

    def is_empty(self):
        return len(self.items) == 0

    def potential_function(self, operation):
        if operation == 'push':
            self.potential += 1
            return 1
        elif operation == 'pop':
            self.potential -= 1
            return -1
        else:
            print('Invalid operation')
            return 0

    def push(self, value):
        self.items.append(value)
        self.amortised_cost = self.amortised_cost + 1 + self.potential_function('push')
        print(f"Pushed ({value}): actual cost 1 plus the change in potential caused by the operation")
        self.print_stack()

    def pop(self):
        if self.is_empty():
            print('stack underflow')
        else:
            pop_value = self.items.pop()
            self.amortised_cost = self.amortised_cost + 1 + self.potential_function('pop')
            print(f"Popped ({pop_value}): actual cost 1 plus the change in potential caused by the operation")
            self.print_stack()

    def print_stack(self):
        print(f'Stack: {self.items}\nPotential: {self.potential}\n')


stack = StackSimulator()
stack.push(1)
stack.push(2)
stack.pop()
stack.pop()
stack.pop()
