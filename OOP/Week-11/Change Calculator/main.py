# main.py
# Main program to use ChangeMaker class

from change_maker import ChangeMaker

def main():
    # Example denominations (Pakistani currency)
    denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

    charged = int(input("Enter amount charged: "))
    given = int(input("Enter amount given: "))

    cm = ChangeMaker(denominations)
    cm.make_change(charged, given)
    cm.show_change()

if __name__ == "__main__":
    main()

"""................................................................."""
# from change_maker import ChangeMaker



# if __name__ == "__main__":
#     charged = int(input("Enter amount charged: "))
#     given = int(input("Enter amount given: "))

#     changer = ChangeMaker(charged, given)  # object created
#     changer.calculate_change()
#     changer.display_change()
