from helper_functions import ask_player_input
from helper_functions import give_random_name
from helper_functions import title_screen
from player import Player
from player import Computer_Player
from deck import Deck
from hand import Hand
from dealer import Dealer

class BlackjackGame:
    round_number = 1

    @classmethod
    def start(self):
        BlackjackGame.opening_display()
        Deck.main_deck.shuffle()
        self.setup_players()
        while True:
            self.place_bets()
            self.initial_deal()
            self.run_player_turns()
            self.run_dealer_turn()
            self.resolve_round()
            self.eliminate_bankrupt_players()
            if not self.ask_continue():
                BlackjackGame.ending_display()
                break

            BlackjackGame.round_number += 1
            self.reset_for_next_round()            
            

    def setup_players():
        print()
        print(" Game Setup. ".center(100, "-"))
        print()
        print(" How many Computer Players would you like to play with?".center(100, " "))
        print()
        number_of_computer_players = int(ask_player_input("Please enter the # of Computer Players: (0 to 9 Players) ", "integer", "number_of_computer_players"))
        print()
        print(" What would you like to be called? ".center(100, " "))
        print()
        name_of_player = ask_player_input("Please enter your name:", "string")
        
        Player(name_of_player, 1000, 0)

        for computer_players in range(number_of_computer_players):
            Computer_Player(give_random_name(), 1000, 0)

        Dealer("Main_Dealer")

        print()
        print(" You will be playing with the following Players: ".center(100, " "))
        print()
        print("".center(40, "-").center(100, " "))
        print()
        
        for player in Player.all_players:
            print(f"{player.name}".center(100, " "))
        
        print()
        print("".center(40, "-").center(100, " "))
        print()
        ask_player_input("Press enter to continue:", "blank", "continue")

    def place_bets():
        print()
        print(f" + Round {BlackjackGame.round_number} + ".center(65,"=").center(100, "-"))

        if Player.all_players[0] == Player.all_players_immutable[0]:
            print()
            print(f"How much are you willing to bet for this round?".center(100, " "))
            print(f"Current Balance: $ {Player.all_players[0].balance}".center(100, " "))
            print()

        for player in Player.all_players:
            player.place_bet()

    def initial_deal():
        print()
        print("".center(100, "~"))
        print()
        print(f" Round {BlackjackGame.round_number} is starting.".center(100, " "))
        if Player.all_players[0] == Player.all_players_immutable[0]:
            print(f" Goodluck and Have Fun! ".center(100, " "))
        else:
            print(f" You are eliminated. Have fun watching! ".center(100, " "))
        print()
        ask_player_input("Press enter to continue:", "blank", "continue")

        for player in Player.all_players:
            player.hit(Deck.main_deck)
            player.hit(Deck.main_deck)
            player.hand.compute_total()
            player.hand.before_hit_total_value = player.hand.total_value

        Dealer.main_dealer.play_turn()
        Dealer.main_dealer.hand.compute_total()
        Dealer.main_dealer.hand.before_hit_total_value = Dealer.main_dealer.hand.total_value

        BlackjackGame.initial_deal_display()
        ask_player_input("Press enter to continue:", "blank", "continue")

    def run_player_turns():
        for player in Player.all_players:
            print()
            print(f" {player.name}'s Turn ".center(100, "-"))
            player.hand.compute_total()

            decision = 1
            while (decision == 1) and player.hand.total_value < 21:

                if player == Player.all_players[0]:
                    BlackjackGame.after_player_turn_display()
                        
                    decision = player.ask_turn_decision()

                    if decision == 1:

                        player.hand.before_hit_total_value = player.hand.total_value
                        player.hand.compute_total()
                        
                        print()
                        print(f"".center(100, "-"))
                        print()
                        print(f"{player.name} has decided to Hit. Added {player.hand.card_hand_string[-1]}. Hand Value: ({player.hand.before_hit_total_value}) -> ({player.hand.total_value})".center(100, " "))
                        print()
                        print(f"".center(100, "-"))
                        print()

                        player.round_status = "Hit."
                    if decision == 1:
                        ask_player_input("Press enter to continue:", "blank", "continue")
                    else:
                        pass


                elif decision == 1 and player != Player.all_players[0]:
                    
                    BlackjackGame.after_player_turn_display()
                    decision = player.ask_turn_decision()

                    if decision == 1:
                    
                        player.hand.before_hit_total_value = player.hand.total_value
                        player.hand.compute_total()

                        print(f"".center(100, "-"))
                        print()
                        print(f"{player.name} has decided to Hit. Added {player.hand.card_hand_string[-1]}. Hand Value: ({player.hand.before_hit_total_value}) -> ({player.hand.total_value})".center(100, " "))
                        print()
                        print(f"".center(100, "-"))
                        print()

                        ask_player_input("Press enter to continue:", "blank", "continue")

                        player.round_status = "Hit."

            
            if player.hand.is_bust():
                print()
                print(f"".center(100, "-"))
                print()
                print(f"{player.name} has busted. ({player.hand.total_value})".center(100, " "))
                print()
                print(f"".center(100, "-"))
                print()
                ask_player_input("Press enter to continue:", "blank", "continue")

            elif player.hand.is_blackjack():
                print()
                print(f"".center(100, "-"))
                print()
                print(f"{player.name} has blackjack. ({player.hand.total_value})".center(100, " "))
                print()
                print(f"".center(100, "-"))
                print()
                ask_player_input("Press enter to continue:", "blank", "continue")

            elif player.hand.total_value == 21:
                print()
                print(f"".center(100, "-"))
                print()
                print(f"{player.name} has Non-natural blackjack. ({player.hand.total_value})".center(100, " "))
                print()
                print(f"".center(100, "-"))
                print()
                ask_player_input("Press enter to continue:", "blank", "continue")

            else:
                print()
                print(f"".center(100, "-"))
                print()
                print(f"{player.name} has decided to stand. ({player.hand.total_value})".center(100, " "))
                print()
                print(f"".center(100, "-"))
                print()
                player.round_status = "Stand."

                ask_player_input("Press enter to continue:", "blank", "continue")

            print()
            print(f" Turn Summary for {player.name} ".center(100, "-"))
            BlackjackGame.after_player_turn_display()
            print(f" End of {player.name}'s Turn ".center(100, "-"))
            print()

            ask_player_input("Press enter to continue:", "blank", "continue")

    def run_dealer_turn():
        print()
        print(f" Dealer's Reveal. ".center(100, "-"))
        print()
        ask_player_input("Press enter to continue:", "blank", "continue")

        BlackjackGame.after_reveal_display()

        decision = 1
        while (decision == 1) and Dealer.main_dealer.hand.total_value < 17:
                
            decision = Dealer.main_dealer.hit_stand_after_reveal()
            ask_player_input("Press enter to continue:", "blank", "continue")


            if decision == 1:
            
                Dealer.main_dealer.hand.before_hit_total_value = Dealer.main_dealer.hand.total_value
                Dealer.main_dealer.hand.compute_total()
                
                print()
                print(f"".center(100, "-"))
                print()
                print(f"{Dealer.main_dealer.name} has to Hit. Added {Dealer.main_dealer.hand.card_hand_string[-1]}. Hand Value: {Dealer.main_dealer.hand.before_hit_total_value} -> {Dealer.main_dealer.hand.total_value}".center(100, " "))
                print()
                print(f"".center(100, "-"))
                
            BlackjackGame.after_reveal_display()


        print(f" End of Dealer's Turn ".center(100, "-"))
        print()
        
        ask_player_input("Press enter to continue:", "blank", "continue")

    def resolve_round():
        for player in Player.all_players:
            player.check_hands_player_dealer(Dealer.main_dealer)

        BlackjackGame.end_of_round_display()

    def eliminate_bankrupt_players():
        print(" Players' Balance Summary: ".center(40, "-").center(100, " "))
        print()

        to_be_removed_players = []

        for player in Player.all_players:
            if player.balance > 0:
                print(f"{player.name}".center(100, " "))
                print(f"(Balance left: $ {player.balance}).".center(100, " "))
                print()

            else:
                print(f"{player.name} will be eliminated for the next round.".center(100, " "))
                print(f"(Balance left: $ {player.balance}).".center(100, " "))
                print()
                to_be_removed_players.append(player)

        for player in to_be_removed_players:
            Player.all_players.remove(player)

            
        print("".center(40, "-").center(100, " "))
        print()
        ask_player_input("Press enter to continue:", "blank", "continue")
            
    def ask_continue():
        print()
        print("Do you want to continue to the next round?".center(100, " "))
        print()
        continue_decision = ask_player_input("Please enter Yes or No: (y/n) ","string", "yes_or_no")

        if continue_decision == "y":
            return True
        elif continue_decision == "n":
            return False
        else:
            print(continue_decision, len(continue_decision))
            return False

    def reset_for_next_round():
        for player in Player.all_players:
            player.hand.card_hand.clear()
            player.hand.card_hand_string.clear()
            player.bet = 0
            player.previous_round_balance = player.balance
            player.hand.before_hit_total_value = 0
            player.round_status = "To play."

        Dealer.main_dealer.hand.card_hand.clear()
        Dealer.main_dealer.hand.card_hand_string.clear()

        Deck.main_deck.shuffle()

    @staticmethod
    def opening_display():
        
        print()
        print("".center(80, "-").center(100, " "))
        print()
        title_screen()
        print()
        print(" Hit or Stand? Beat the dealer without going over 21. ".center(100, " "))
        print()
        print("".center(80, "-").center(100, " "))
        print()
        ask_player_input("(Press enter to continue)", "blank", "continue")

        print()
        print("Do you want to know the rules of Classic BlackJack? ".center(100, " "))
        print()
        how_to_play = ask_player_input("Please enter Yes or No: (y/n) ","string", "yes_or_no")

        if how_to_play == "y":
            # Inspired by "How to Play Blackjack" by wikiHow
            print()
            print(" How to Play Classic BlackJack. ".center(100, "="))
            print()
            print("The goal of Blackjack is having a hand that has a higher ".center(100, " "))
            print("total value then the dealer's, but does not exceed 21.".center(100, " "))
            print("If you're hand value is higher than 21, it is called a 'bust',".center(100, " "))
            print("which means you automatically lost the round.".center(100, " "))
            print()

            ask_player_input("(Press enter to continue)", "blank")

            print()
            print("Game flow:")
            print("    Initial Deal:")
            print("        The round starts with everyone setting their bets.")
            print("        After that, the dealer deals two cards to each player and to themselves.")
            print("        However, players would not be able to see the second card of the dealer.")
            print()

            ask_player_input("(Press enter to continue)", "blank")

            print()
            print("    Hand and Card Value:")
            print("        Cards 2 to 10 has face value. (Ex. 10 has a value of 10)")
            print("        Queens, Kings, and Jacks all have a value of 10.")
            print("        Aces can be either have a value of 1 or 11, depending on the more beneficial value for the hand.")
            print()
            
            ask_player_input("(Press enter to continue)", "blank")

            print()
            print("    BlackJack Hand:")
            print("        If you're two cards are equal to 21, you have a BlackJack, and automatically wins 1.5 times your bet, and your bet back (3:2).")
            print("        (Ex. Ace (A) of Hears, 10 of Spades | Hand Value: (21) | Bet: $ 50 -> Winnings: + $ 125)")
            print()
                        
            ask_player_input("(Press enter to continue)", "blank")

            print()
            print("    Non-BlackJack Hand:")
            print("        If the hand is not a BlackJack, you have two choices:")
            print("            Hit, to ask the dealer for another card.")
            print("                You can keep hitting, but once your hand value is higher than 21, you bust and lose for the round.")
            print("            Stand, to end your turn.")
            print()
                                    
            ask_player_input("(Press enter to continue)", "blank")

            print()
            print("    After Player Turns:")
            print("        After the turn of each player, the dealer reveals their hidden card.")
            print("        If their hand is less than 16, they have to hit, until their hand is 17 or greater.")
            print("        If their hand is 17 or greater, they have to stand.")
            print()
                        
            ask_player_input("(Press enter to continue)", "blank")

            print()
            print("    Winning Conditions:")
            print("        1. If the dealer busts, everyone who stood wins twice their bet (1:1).")
            print("        2. If dealer doesn't bust, players who has a hand value greater than the dealer's wins twice their bet (1:1).")
            print()
                        
            ask_player_input("(Press enter to continue)", "blank")

            print()
            print("    Round Ending:")
            print("        After Player and Dealer turns, winnings are given out.")
            print("        You have the option to continue playing or ending the game.")
            print()
                                    
            ask_player_input("(Press enter to continue)", "blank")

        elif how_to_play == "n":
            pass

        print()
        print("".center(100, "-"))
        print(" This is Classic BlackJack: CLI Edition. Good Luck and Have fun! ".center(100, " "))
        print("".center(100, "-"))
        
        print()
        ask_player_input("Press Enter to start playing Blackjack!", "blank", "continue")


    @staticmethod
    def ending_display():
        print()
        print("".center(100, "~"))
        print()
        print(f"Thank you for playing!".center(100, " "))
        print(f"You played {BlackjackGame.round_number} Round/s.".center(100, " "))
        print()
        print(f"Created by: JM Jasmin".center(100, " "))
        print()
        ask_player_input("(Press enter to Quit)", "blank", "continue")
        print()

    @staticmethod
    def initial_deal_display():

        print()

        print(f" Round {BlackjackGame.round_number}: Initial Deal. ".center(100, "-"))

        print()
        print(" DEALER: ".center(70, "=").center(100, " "))
        Dealer.main_dealer.hand.compute_total()
        print()
        print(f"Hand: {Dealer.main_dealer.hand.card_hand_string[0]}, ******** | Hand Value: ({Dealer.main_dealer.hand.card_hand[0].value} + ???)".center(100, " "))
        print()

        print(" PLAYERS: ".center(70, "=").center(100, " "))

        for player in Player.all_players:
            player.hand.compute_total()
            print()
            print(f" {player.name} ".center(50, "-").center(100, " "))
            print()
            print(f"Current Balance: $ {player.balance} | Bet: $ {player.bet} | Hand Value: ({player.hand.total_value})".center(100, " "))
            print()
            print(f"Hand: {", ".join(player.hand.card_hand_string)}".center(100, " "))
            print()
            print("".center(50, "-").center(100, " "))

        print()
        print(" PLAYERS' TURN STATUS: ".center(70, "=").center(100, " "))
        print()

        print("".center(60, "-").center(100, " "))
        for player in Player.all_players:
            print(f"{player.name}: {player.round_status} ".ljust(50, " ").center(100, " "))
        print("".center(60, "-").center(100, " "))
        
        print()

    @staticmethod
    def after_player_turn_display():

        print()
        print(" DEALER: ".center(70, "=").center(100, " "))
        Dealer.main_dealer.hand.compute_total()
        print()
        print(f"Hand: {Dealer.main_dealer.hand.card_hand_string[0]}, ******** | Hand Value: ({Dealer.main_dealer.hand.card_hand[0].value} + ???)".center(100, " "))
        print()

        print(" PLAYERS: ".center(70, "=").center(100, " "))
        for player in Player.all_players:
            player.hand.compute_total()
            print()
            print(f" {player.name} ".center(50, "-").center(100, " "))
            print(f"Current Balance: $ {player.balance} | Bet: $ {player.bet} | Hand Value: ({player.hand.total_value})".center(100, " "))
            print(f"Hand: {", ".join(player.hand.card_hand_string)}".center(100, " "))
            print("".center(50, "-").center(100, " "))

        print()

        print(" PLAYERS TURN STATUS: ".center(70, "=").center(100, " "))
        
        print()
        print("".center(60, "-").center(100, " "))
        for player in Player.all_players:
            if player.hand.is_blackjack():
                print(f"{player.name}: Hand is a Natural BlackJack!".ljust(50, " ").center(100, " "))
                print(f"{" "*len(player.name)}  ({", ".join(player.hand.card_hand_string)})".ljust(50, " ").center(100, " "))
            elif player.hand.total_value == 21:
                print(f"{player.name}: Hand is a Non-Natural BlackJack!".ljust(50, " ").center(100, " "))
                print(f"{" "*len(player.name)}  ({", ".join(player.hand.card_hand_string)})".ljust(50, " ").center(100, " "))
            elif player.hand.is_bust():
                print(f"{player.name}: Hand Busted! Hand Value: ({player.hand.total_value})".ljust(50, " ").center(100, " "))
            else:
                print(f"{player.name}: {player.round_status} Hand Value: ({player.hand.total_value})".ljust(50, " ").center(100, " "))
        print("".center(60, "-").center(100, " "))
        print()
    
    @staticmethod
    def after_reveal_display():

        print()
        print(" DEALER: ".center(70, "=").center(100, " "))
        Dealer.main_dealer.hand.compute_total()
        print()
        print(f"Hand: {", ".join(Dealer.main_dealer.hand.card_hand_string)} | Hand Value: {Dealer.main_dealer.hand.total_value}".center(100, " "))
        print()
        print("".center(70, "=").center(100, " "))
        print()

    @staticmethod
    def end_of_round_display():

        print()

        print(f" End of Round Summary. ".center(100, "-"))

        print()
        print(" DEALER: ".center(70, "=").center(100, " "))
        Dealer.main_dealer.hand.compute_total()
        print()
        print(f"Hand: {", ".join(Dealer.main_dealer.hand.card_hand_string)} | Hand Value: {Dealer.main_dealer.hand.total_value}".center(100, " "))
        print()


        print(" PLAYERS' CARD HANDS: ".center(70, "=").center(100, " "))
        for player in Player.all_players:
            player.hand.compute_total()
            print()
            print(f" {player.name} ".center(50, "-").center(100, " "))
            print(f"Hand Value: ({player.hand.total_value})".center(100, " "))
            print(f"Hand: {", ".join(player.hand.card_hand_string)}".center(100, " "))
            print("".center(50, "-").center(100, " "))

        print()

        ask_player_input("Press enter to continue:", "blank", "continue")

        print()

        print(" PLAYERS' ROUND STATUS: ".center(70, "=").center(100, " "))
        
        for player in Player.all_players:
            print()
            print(f" {player.name} ".center(60, "-").center(100, " "))
            print()
            
            if Dealer.main_dealer.hand.is_blackjack() and player.hand.is_blackjack():
                print(f"Tie. Both BlackJacks!! ".center(100, " "))
                print(f"(Bet: $ {player.bet} -> Winnings: $ 0)".center(100, " "))
                print(f"(Previous Balance: $ {player.previous_round_balance} -> Current Balance: $ {player.balance})".center(100, " "))

            elif Dealer.main_dealer.hand.is_blackjack() and not player.hand.is_blackjack():
                print(f"Lost. Player Hand Value ({player.hand.total_value}) less than Dealer Hand Value ({Dealer.main_dealer.hand.total_value}) ".center(100, " "))
                print(f"(Bet: $ {player.bet} -> Winnings: - $ {player.bet})".center(100, " "))
                print(f"(Previous Balance: $ {player.previous_round_balance} -> Current Balance: $ {player.balance})".center(100, " "))

            elif player.hand.is_blackjack() and not Dealer.main_dealer.hand.is_blackjack():
                print(f"Won. Player Hand is a Natural BlackJack! ({player.hand.total_value})".center(100, " "))
                print(f"(Bet: $ {player.bet} -> Winnings: $ + {player.bet * 1.5})".center(100, " "))
                print(f"(Previous Balance: $ {player.previous_round_balance} -> Current Balance: $ {player.balance})".center(100, " "))

            elif player.hand.is_bust():
                print(f"Lost. Player Hand is busted! ({player.hand.total_value})".center(100, " "))
                print(f"(Bet: $ {player.bet} -> Winnings: - $ {player.bet})".center(100, " "))
                print(f"(Previous Balance: $ {player.previous_round_balance} -> Current Balance: $ {player.balance})".center(100, " "))

            elif Dealer.main_dealer.hand.is_bust() and not player.hand.is_bust():
                print(f"Won. Player Stood, Dealer Hand is Busted! ({Dealer.main_dealer.hand.total_value})".center(100, " "))
                print(f"(Bet: $ {player.bet} -> Winnings: + $ {player.bet})".center(100, " "))
                print(f"(Previous Balance: $ {player.previous_round_balance} -> Current Balance: $ {player.balance})".center(100, " "))

            elif player.hand.total_value > Dealer.main_dealer.hand.total_value:
                print(f"Won. Player Hand Value ({player.hand.total_value}) greater than Dealer Hand Value ({Dealer.main_dealer.hand.total_value})".center(100, " "))
                print(f"(Bet: $ {player.bet} -> Winnings: + $ {player.bet})".center(100, " "))
                print(f"(Previous Balance: $ {player.previous_round_balance} -> Current Balance: $ {player.balance})".center(100, " "))

            elif Dealer.main_dealer.hand.total_value > player.hand.total_value:
                print(f"Lost. Player Hand Value ({player.hand.total_value}) less than Dealer Hand Value ({Dealer.main_dealer.hand.total_value}) ".center(100, " "))
                print(f"(Bet: $ {player.bet} -> Winnings: - $ {player.bet})".center(100, " "))
                print(f"(Previous Balance: $ {player.previous_round_balance} -> Current Balance: $ {player.balance})".center(100, " "))

            elif Dealer.main_dealer.hand.total_value == player.hand.total_value:
                print(f"Tie. Both Hands are equal!! ({player.hand.total_value})".center(100, " "))
                print(f"(Bet: $ {player.bet} -> Winnings: $ 0)".center(100, " "))
                print(f"(Previous Balance: $ {player.previous_round_balance} -> Current Balance: $ {player.balance})".center(100, " "))

            print()
            print("".center(60, "-").center(100, " "))

        print()
        ask_player_input("Press enter to continue:", "blank", "continue")
        print()