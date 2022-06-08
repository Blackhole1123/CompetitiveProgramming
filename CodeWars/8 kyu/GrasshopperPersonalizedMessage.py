def greet(name, owner):
    ans = lambda name, owner : "Hello boss" if name == owner else "Hello guest"
    return ans(name, owner)