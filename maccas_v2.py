import easygui

# Combos
Value = {
    "Beef Burger: 5.69\n",
    "Fries 1.00\n",
    "Fizzy Drink 1.00\n"}
Cheezy = {
    "CheeseBurger: 6.69\n",
    "Fries 1.00\n",
    "Fizzy Drink: 1.00\n"}
Super = {
    "CheeseBurger: 6.69\n",
    "Large Fries: 2.00\n",
    "Smoothie: 2.00\n"}

Combos = [Value, Cheezy, Super]
print(easygui.msgbox(Combos))


add_or_edit = easygui.buttonbox("Do You Want To Add Or Edit An Existing Menu?", choices=["Add", "Edit"])

if add_or_edit == "Edit":
    print("e")

print(Value)
