from pakudex import *

pakudex = Pakudex(capacity=20)  # needed to instantiate this class


class Pakuri_Program:
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    print('Enter max capacity of the Pakudex: ', end='')


try:
    capacity = int(input())
    if capacity < 1:  # if capacity is less than 0 it will prompt to try again + loop over to the start
        print('Please enter a valid size.')
        print('Enter max capacity of the Pakudex: ', end='')
        capacity = int(input())
    if capacity > 0:  # if capacity is in acceptable range it will go to while loop
        print(f'The Pakudex can hold {capacity} species of Pakuri.')
    game_continue = True
    while game_continue:
        print('\nPakudex Main Menu')
        print('-' * 17)
        print('1.  List Pakuri')
        print('2.  Show Pakuri')
        print('3.  Add Pakuri')
        print('4.  Evolve Pakuri')
        print('5.  Sort Pakuri')
        print('6.  Exit\n')
        print('What would you like to do? ', end='')
        choice = str(input())

        if choice == str(1):  # will list existing Pakuri in the list
            if pakudex.get_size() == 0:
                print('No Pakuri in Pakudex yet!')
            if pakudex.get_size() != 0:
                print('Pakuri In Pakudex:')
                for count, value in enumerate((pakudex.get_species_array()), start=1):
                    print(f'{count}. {value}')  # prints list of what is in pakudex

        if choice == str(2):  # will show chosen Pakuri statistics
            print('Enter the name of the species to display: ', end='')
            species = input()
            get_stats = pakudex.get_stats(species)
            if get_stats == None:  # if no species is in deck that matches input then 'error'
                print('Error: No such Pakuri!')
            else:
                print('Species:', species)
                print('Attack:', get_stats[0])
                print('Defense:', get_stats[1])
                print('Speed:', get_stats[2])

        if choice == str(3):  # will add new pakuri to the list
            size = pakudex.get_size()
            if capacity == size:  # if capacity == amount in deck = full
                # print('Enter the name of the species to add: ')
                 # species = input()
                print("Error: Pakudex is full!")
            else:
                print('Enter the name of the species to add: ', end='')
                species = input()
                pakudex.add_pakuri(species)

        if choice == str(4):  # will evolve the statistics of the species
            print('Enter the name of the species to evolve: ', end='')
            species = input()
            evolve = pakudex.evolve_species(species)
            if evolve:
                print(species + ' has evolved!')


        if choice == str(5):  # will sort the pakuri in the list
            print('Pakuri have been sorted!')
            pakudex.sort_pakuri()

        if choice == str(6):
            print('Thanks for using Pakudex! Bye!')
            break
        if choice < str(int(1)):
            print('Unrecognized menu selection!')
        if choice > str(int(6)):
            print('Unrecognized menu selection!')



except ValueError:  # oof
    print('Please enter a valid size.')
    print('Enter max capacity of the Pakudex: ', end='')
    capacity = int(input())

    if capacity < 1:  # if capacity is less than 0 it will prompt to try again + loop over to the start
        print('Please enter a valid size.')
        print('Enter max capacity of the Pakudex: ', end='')
        capacity = int(input())

    game_continue = True
    while game_continue:
        print('\nPakudex Main Menu')
        print('-' * 17)
        print('1.  List Pakuri')
        print('2.  Show Pakuri')
        print('3.  Add Pakuri')
        print('4.  Evolve Pakuri')
        print('5.  Sort Pakuri')
        print('6.  Exit\n')
        print('What would you like to do? ', end='')
        choice = str(input())

        if choice == str(1):  # will list existing Pakuri in the list
            if pakudex.get_size() == 0:
                print('No Pakuri in Pakudex yet!')
            if pakudex.get_size() != 0:
                print('Pakuri In Pakudex:')
                for count, value in enumerate((pakudex.get_species_array()), start=1):
                    print(f'{count}. {value}')  # prints list of what is in pakudex

        if choice == str(2):  # will show chosen Pakuri statistics
            print('Enter the name of the species to display: ', end='')
            species = input()
            get_stats = pakudex.get_stats(species)
            if get_stats == None:  # if no species is in deck that matches input then 'error'
                print('Error: No such Pakuri!')
            else:
                print('Species:', species)
                print('Attack:', get_stats[0])
                print('Defense:', get_stats[1])
                print('Speed:', get_stats[2])

        if choice == str(3):  # will add new pakuri to the list
            size = pakudex.get_size()
            if capacity == size:  # if capacity == amount in deck = full
                # print('Enter the name of the species to add: ')
                # species = input()
                print("Error: Pakudex is full!")
            else:
                print('Enter the name of the species to add: ', end='')
                species = input()
                pakudex.add_pakuri(species)

        if choice == str(4):  # will evolve the statistics of the species
            print('Enter the name of the species to evolve: ', end='')
            species = input()
            evolve = pakudex.evolve_species(species)
            if evolve:
                print(species + ' has evolved!')

        if choice == str(5):  # will sort the pakuri in the list
            print('Pakuri have been sorted!')
            pakudex.sort_pakuri()

        if choice == str(6):
            print('Thanks for using Pakudex! Bye!')
            break
        if choice < str(int(1)):
            print('Unrecognized menu selection!')
        if choice > str(int(6)):
            print('Unrecognized menu selection!')

# sort function does not sort when selecting option 1 after option 5
