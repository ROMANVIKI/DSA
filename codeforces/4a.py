def sol(num):
    if num == 2:
        return "NO"
    elif num % 2 == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    while True:
        try:
            user_input = int(input())
            print(sol(num=user_input))
        except EOFError:
            break
        except ValueError:
            print("Invalid input, please enter a integer.")
