import random

def hire_assistant(n):
    candidates = list(range(1, n + 1))
    random.shuffle(candidates)

    best_c = candidates[0]
    for index, c in enumerate(candidates):
        if c >= best_c:
            best_index = index
            best_c = c
    
    return best_index, candidates, best_c

n = 100
best_index, candidates, best_c = hire_assistant(n)
print(f"All candidates: {candidates}\nHired Candidate: {best_c}(index: {best_index})")