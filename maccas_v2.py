import easygui

# Combos
Value = {
    "Beef Burger": 5.69,
    "Fries": 1.00,
    "Fizzy Drink": 1.00}
Cheezy = {
    "CheeseBurger": 6.69,
    "Fries": 1.00,
    "Fizzy Drink": 1.00}
Super = {
    "CheeseBurger": 6.69,
    "Large Fries": 2.00,
    "Smoothie": 2.00}

Combos = [Value, Cheezy, Super]
print(Combos)


add_or_edit = easygui.buttonbox("Do You Want To Add Or Edit An Existing Menu?", choices=["Add", "Edit"])

if add_or_edit == "Edit":
    edit = easygui.buttonbox("What Combo Do You Want To Edit?", choices=["Value", "Cheezy", "Super"])
    if edit == "Value":
       Valueedit = easygui.codebox(Value)

    elif edit == "Cheezy":
        print("d")

    elif edit == "Super":
        print("e")

print(Value)