while True:
        print("Choices: [0] User Path [1] Main Path: ")
        pick = int(input(" Choose :"))

        if pick == 0:
            import user
            break

        elif pick == 1:
            import ter
            break

        else:
            print("Access Denied")