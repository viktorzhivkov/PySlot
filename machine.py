import random

class SlotMachine:
    def __init__(self):
        self.symbols = {
            "Cherry": 2,
            "Lemon": 3,
            "Orange": 4,
            "Plum": 5,
            "Bell": 10,
            "Bar": 20,
            "Seven": 50,
        }
        self.reel_probabilities = {
            "Cherry": 0.2,
            "Lemon": 0.2,
            "Orange": 0.2,
            "Plum": 0.15,
            "Bell": 0.1,
            "Bar": 0.05,
            "Seven": 0.05,
        }
        self.payout_frequency = 0.3
        self.payout_ratio = 0.85

    def spin(self):
        reel1 = random.choices(list(self.reel_probabilities.keys()), list(self.reel_probabilities.values()))[0]
        reel2 = random.choices(list(self.reel_probabilities.keys()), list(self.reel_probabilities.values()))[0]
        reel3 = random.choices(list(self.reel_probabilities.keys()), list(self.reel_probabilities.values()))[0]
        payout = 0
        
        if reel1 == reel2 == reel3:
            payout = self.symbols[reel1] * 10
        elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
            payout = self.symbols[reel1] * 2
        elif reel1 == "Cherry" or reel2 == "Cherry" or reel3 == "Cherry":
            payout = self.symbols["Cherry"]
            
        return payout
    
    def play(self):
        player_balance = 100
        
        while True:
            choice = input("Press 'q' to quit or any other key to play: ")
            if choice.lower() == "q":
                break
                
            if random.random() < self.payout_frequency:
                max_payout = player_balance * self.payout_ratio
                payout_total = 0
                
                while payout_total < max_payout:
                    payout = self.spin()
                    player_balance += payout
                    
                    if player_balance <= 0:
                        print("Game over.")
                        return
                        
                    payout_total += payout
            else:
                payout = self.spin()
                player_balance += payout
                
                if player_balance <= 0:
                    print("Game over.")
                    return

machine = SlotMachine()
machine.play()