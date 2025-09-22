from change_maker import ChangeMaker

if __name__ == "__main__":
    charged = int(input("Enter amount charged: "))
    given = int(input("Enter amount given: "))

    changer = ChangeMaker(charged, given)  # object created
    changer.calculate_change()
    changer.display_change()
