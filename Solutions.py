

# player = set()
# computer = set([2,4])

# print(computer)

# def getUserInput():
#     while True:
#         choice = int(input("adfgafdg"))
#         if (choice in player or choice in computer):
#             print("Choice is already taken")
#             continue
#         else:
#             player.add(choice)
#             break

# getUserInput()
# print(player, computer)
# getUserInput()
# print(player, computer)
# getUserInput()
# print(player, computer)
# getUserInput()

# potato solution 2

# choices = {
#     0: "blank",
#     1: "blank",
#     2: "computer",
#     3: "blank",
#     4: "computer",
#     5: "blank",
#     6: "blank",
#     7: "blank",
#     8: "blank",
#     9: "blank",
# }

# def getUserInput():
#     while True:
#         choice = int(input("adfgafdg"))
#         if (choices[choice] == "blank"):
#            choices[choice] = "player"
#            break
#         else:
#            print("Choice is already taken")

# getUserInput()
# print(choices)
# getUserInput()
# print(choices)
# getUserInput()
# print(choices)
# getUserInput()

# potato solution 3

arr = [0,1,3,5,6,7,8,9]
player = []
computer = [2, 4]

def getUserInput():
    while True:
        choice = int(input("adfgafdg"))
        if (choice in arr):
           arr.remove(choice)
           player.append(choice)
           break
        else:
           print("Choice is already taken")

getUserInput()
print(arr, player, computer)
getUserInput()
print(arr, player, computer)
getUserInput()
print(arr, player, computer)
getUserInput()