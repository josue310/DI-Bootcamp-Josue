import random
class Game:
    def __init__(self):
        pass
    def get_user_item(self):
        option = input("(r)ock, (p)aper, (s)cissors: ")
        while option not in ('r','p','s'):
            option = input("please write the first letter of your choice").lower
        return option

    def get_computer_item(self):
        value = random.choice(('r','p','s'))
        return value

    def get_game_result(self, user_item, computer_item):
        self.user_item = user_item
        self.computer_item = computer_item
        if (self.user_item == 'r' and self.computer_item == 's') or (self.user_item == 'p' and self.computer_item == 'r') or (self.user_item=='s' and self.computer_item == 'p'):
            return "win"
        elif self.user_item == self.computer_item:
            return "draw"
        else:
            return "loss"
            
    def play(self):
        user_item_v = self.get_user_item()
        random_item_v = self.get_computer_item()
        result = self.get_game_result(user_item_v, random_item_v)
        if result == "win":
            print(f"You selected {user_item_v}. The computer selected {random_item_v}. You win!")
        elif result == "draw":
            print(f"You selected {user_item_v}. The computer selected {random_item_v}. You drew!")
        else:
            print("You selected {user_item_v}. The computer selected {random_item_v}. You lose!")
        return result
        
