def grid_traveller(m: int, n: int, memo: dict = None) -> int:
    #Base cases
    if memo is None:
        memo: dict[str, int] = {}
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    key = f"{m},{n}" 
    if key in memo:
        return memo[key]
    memo[key] = grid_traveller(m - 1, n, memo ) + grid_traveller(m , n - 1, memo)
    return memo[key]


print(grid_traveller(3,3))
print(grid_traveller(30,15))