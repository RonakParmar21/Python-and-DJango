weekIndex = int(input("Enter index of week : "))
match weekIndex:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case _:
        print("not")