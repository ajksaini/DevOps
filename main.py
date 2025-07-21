# this is my first python program

def greet(name: str) -> str:
    if not name:
        return "Hello, Stranger!"
    return f"Hello, {name}"


# Simple test function
def test_greet():
    assert greet("Alice") == "Hello, Alice"
    assert greet("") == "Hello, Stranger!"
    print("All tests passed.")


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    test_greet()