def main():
    try:
        a = int(input("hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am inside a finally")

main()