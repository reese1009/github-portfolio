from p1_random import P1Random

rng = P1Random()

game_continue = True
# game stats
game_num = 0
player_games_won = 0
dealer_games_won = 0
num_ties = 0
no_winners = True

while game_continue:
    # 1. set up initial message
    game_num += 1
    print(f'START GAME #{game_num}\n')
    player_hand = 0
    dealer_hand = 0

    # 2. deal a card to the player
    card = rng.next_int(13) + 1  # 11, 1
    # use if/else/else chain
    if card == 1:
        print('Your card is a ACE!')
        player_hand += card
        print('Your hand is:', player_hand)
    elif 2 <= card <= 10:
        print(f'Your card is a {card}!')
        player_hand += card
        print('Your hand is:', player_hand)
    elif card == 11:
        print('Your card is a JACK!')
        card = 10
        player_hand += card
        print('Your hand is:', player_hand)
    elif card == 12:
        print('Your card is a QUEEN!')
        card = 10
        player_hand += card
        print('Your hand is:', player_hand)
    elif card == 13:
        print('Your card is a KING!')
        card = 10
        player_hand += card
        print('Your hand is:', player_hand)
    # print hand value information

    # 3. keep asking users to choose the menu
    no_winners = True

    while no_winners:
        print('\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit')
        # ask player to enter choice
        choice = int(input('\nChoose an option: '))
        if choice == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                print('\nYour card is a ACE!')
                player_hand += card
                print('Your hand is:', player_hand)
            elif 2 <= card <= 10:
                print(f'\nYour card is a {card}!')
                player_hand += card
                print('Your hand is:', player_hand)
            elif card == 11:
                print('\nYour card is a JACK!')
                card = 10
                player_hand += card
                print('Your hand is:', player_hand)

            elif card == 12:
                print('\nYour card is a QUEEN!')
                card = 10
                player_hand += card
                print('Your hand is:', player_hand)

            elif card == 13:
                print('\nYour card is a KING!')
                card = 10
                player_hand += card
                print('Your hand is:', player_hand)
            if player_hand == 21:
                no_winners = False
                print('\nBLACKJACK! You win!\n')
                player_games_won += 1
            if dealer_hand == 21:
                print('\nDealer wins!\n')
                dealer_games_won += 1
                no_winners = False
            if player_hand > 21:
                print('\nYou exceeded 21! You lose.\n')
                dealer_games_won += 1
                no_winners = False
            if dealer_hand > 21:
                print('\nYou win!\n')
                player_games_won += 1
                no_winners = False
            if dealer_hand == player_hand:
                print('\nIt\'s a tie! No one wins!\n')
                num_ties += 1
                no_winners = False

            # deal a new card to the player
            # add the new card value
            # if player_hand is equal to 21
            # set no_winners to be False
            # print winning message
            # track the number of games the player wins (set up a variable for it)
            # else if player_hand is greater than 21
            # do something similar in the if

        elif choice == 2:
            dealer_hand = rng.next_int(11) + 16
            print(f'\nDealer\'s hand: {dealer_hand}')
            print(f'Your hand is: {player_hand}')
            if player_hand == 21:
                print('\nBLACKJACK! You win!\n')
                player_games_won += 1
                no_winners = False
            if dealer_hand == 21:
                print('\nDealer wins!\n')
                dealer_games_won += 1
                no_winners = False
            if player_hand > 21:
                print('\nYou exceeded 21! You lose.\n')
                dealer_games_won += 1
                no_winners = False
            if dealer_hand < player_hand < 21:
                print('\nYou win!\n')
                player_games_won += 1
                no_winners = False
            if dealer_hand > 21:
                print('\nYou win!\n')
                player_games_won += 1
                no_winners = False
            if player_hand < dealer_hand < 21:
                print('\nDealer wins!\n')
                dealer_games_won += 1
                no_winners = False
            if dealer_hand == player_hand:
                print('\nIt\'s a tie! No one wins!\n')
                num_ties += 1
                no_winners = False
            # deal a card in [16, 26] to the dealer
            # compare dealer hand w/ player hand
            # determine the winner
            # do similar thing in choice 1

        elif choice == 3:
            print('\nNumber of Player wins:', player_games_won)
            print('Number of Dealer wins:', dealer_games_won)
            print('Number of tie games:', num_ties)
            print(f'Total # of games played is: {game_num - 1}')
            if game_num - 1 <= 0:
                print('Percentage of Player wins: 0.0%')
            else:
                print(f'Percentage of Player wins: {(player_games_won / (game_num - 1) * 100)}%')

        elif choice == 4:
            no_winners = False
            game_continue = False
        else:
            print('\nInvalid input!\nPlease enter an integer value between 1 and 4.')
            # print invalid message
        # end of no_winners outputs
    # end of no_winners loop
# end of program
