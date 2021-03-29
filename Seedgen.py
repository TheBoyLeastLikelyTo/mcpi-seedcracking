import mcpi.minecraft as minecraft
#mc = minecraft.Minecraft.create()
print("Minecraft Seed/World Generator")
print("By 'TheBoyLeastLikelyTo'")
print("Main Menu Options")
print("Option 1 - Generate up from Seed")
print("Option 2 - Generate down from Seed")
def choice():
  choice = input("Select Choice: ").strip()
  if choice == "1":
    print("Choice 1 Selected")
    val1 = input("Enter Starting Seed: ")
    print("Starting Seed Confirmed")
  elif choice == "2":
    print("Choice 2 Selected")
    val2 = input("Enter Starting Seed: ")
    print("Starting Seed Confirmed")
  else:
    print("Incorrect Selection")
choice()
