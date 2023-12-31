def combinations_k_elements(chosen, remaining, k):
    if k == 0:
        print(chosen)
        return
    if not remaining or len(remaining) < k:
        return
    
    first = remaining[0]
    combinations_k_elements(chosen + [first], remaining[1:], k - 1)
    combinations_k_elements(chosen, remaining[1:], k)

def generate_combinations(n, k):
    elements = list(range(1, n + 1))
    combinations_k_elements([], elements, k)

# Example usage:
n = 3
k = 2
generate_combinations(n, k)
