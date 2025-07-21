#this is my first python program
def greet(name):

    name= input("Enter your name: ")

    return f"Hello, {name}"     

if __name__ == "__main__":
    print(greet("name"))