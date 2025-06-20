def add_numbers(*args):
    """Function to add multiple numbers."""
    print(f"Arguments received: {args}")
    print(f"Type of args: {type(args)}")
    total = 0
    for num in args:
        total += num

    if total > 100:
        print("Total exceeds 100")
        return total

    print("Total is within the limit")
    return total
