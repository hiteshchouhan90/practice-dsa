memo: dict = {}

def fib_number(n: int) -> int:
    if n in memo.keys():
        return memo[n]
    
    if (n <= 2):
        return 1
    
    memo[n] = fib_number(n - 1) + fib_number(n - 2)
    return memo[n]

print(fib_number(5))
print(fib_number(6))
print(fib_number(8))
print(fib_number(50))

# Per call memoisation

def fib_number(n: int, memo=None) -> int:
    """Per-call memoization without a global dict."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_number(n - 1, memo) + fib_number(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    print(fib_number(5))
    print(fib_number(6))
    print(fib_number(8))
    print(fib_number(50))