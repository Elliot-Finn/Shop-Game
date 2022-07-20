inventory = {"broadsword": {"Cost": 650, "Quantity": 1, "Description": "This high-quality and finely crafted broadsword is the go-to weapon for any experienced fighter. Its immense weight can only be handled by the most skilled swordsmen, but its power and might is in a class of its own. The gemstones that decorate its hilt were raided from the stash of a black dragon."}, "Emblazoned Shield": {"Cost": 300, "Quantity": 3, "Description": "This strong and sturdy metal shield sports an expertly painted head of Medusa so realistic it will stun your enemies in horror."}, "Spear of Moonlight": {"Cost": 400, "Quantity": 2, "Description": "This beautiful spear boasts a point crafted from a rare silver metal that glows with the light of the moon. This metal can only be found inside of asteroids that have fallen to earth in the light of a full moon."}, "Party Balloon Bulk Pack (100pcs)": {"Cost": 50, "Quantity": 10, "Description": "Exactly what it sounds like. Don't ask - we've gotta turn a profit somehow."}}
items = ["broadsword", "emblazoned shield", "spear of moonlight", "party balloons bulk pack (100pcs)"]
def menu():
  print("Virtual Items Inventory")
  print("A- Add an item")
  print("R- Remove an item")
  print("E- Edit an item")
  print("L- List all items")
  print("D- List details of items")
  print("Q- Quit")
  print()
c = 0
while(c!="q" or c!="Q"):
  menu()
  c = input("Enter a command: ").lower()
  if (c=="q"):
    break
  if(c == "a"):
    print()
    item_name = input("Enter item name: ").lower()
    exist = False
    for key, value in inventory.items():
      if (item_name in items):
        exist = True
    if(exist):
      print("We already have that in stock. But if you're so desperate to sell it to us, you can buy our stock and then return it! We'd be glad for the business.")
      print()
    else:
      item_value = float(input("Enter item value: "))
      item_quantity = float(input("Enter item quantity: "))
      item_description = str(input("Enter item description: "))
      inventory[item_name]={}
      inventory[item_name]["value"] = item_value
      inventory[item_name]["quantity"] = item_quantity
      inventory[item_name]["description"] = item_description
      items.append(item_name)
      print("Thank you for the business! Here's your money.")
      print("[You have recieved " + str(item_value*item_quantity) + " gold coins]")
      print()
      print(items)
  elif (c == "e"):
    name = input("Enter item name: ").lower()
    if (name in items):
      item_name = input("Enter item name: ")
      item_value = float(input("Enter item value: "))
      item_quantity = float(input("Enter item quantity: "))
      item_description = input("Enter item description: ")
      del inventory[name]
      items.remove(name)
      inventory[item_name]={}
      inventory[item_name]["value"] = item_value
      inventory[item_name]["quantity"] = item_quantity
      inventory[item_name]["description"] = item_description
      items.append(item_name)
      print("The " + name + " has been successfully edited.")
      print()
    else:
      print("Sorry, we don't have any " + str(name) + "s in stock.")
  elif (c == "r"):
    remove = input("Which item would you like to remove?")
    del inventory[remove]
    items.remove(remove)
    print("The " + str(remove) + " has been successfully removed.")
    print(items)
    print()
  elif(c == "d"):
    print()
    for k, v in inventory.items():
      print("Item: ", k)
      for k in v:
        print(k + ':', v[k])
      print()
  elif(c == "l"):
    for k, v in inventory.items():
      print("Item: ", k)
    print()