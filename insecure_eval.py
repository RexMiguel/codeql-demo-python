def calculator(expr: str):
    # VULNERABILITY: eval on untrusted input
    return eval(expr)


if __name__ == "__main__":
    expr = input("Enter math expression: ")
    print(calculator(expr))
