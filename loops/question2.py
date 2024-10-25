def repeat_until_exit():
    while True:
        user_input = input("Enter a word (Enter 'exit' to stop): ")
        if user_input.lower() == "exit":
            break
        print(user_input)

repeat_until_exit()
