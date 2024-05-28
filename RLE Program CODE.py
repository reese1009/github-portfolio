from console_gfx import ConsoleGfx

print('Welcome to the RLE image encoder!\n')
print('Displaying Spectrum Image:')
ConsoleGfx.display_image(ConsoleGfx.test_rainbow)



image_data = None

while True: # 1st iteration option 1 read the image file, 2nd iteration option 6 display the image in the image file
    print('\nRLE Menu')
    print('-' * 8)
    # menu title
    print('0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String')
    print('4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image')
    print('7. Display RLE String\n8. Display Hex RLE Data\n9. Display HEX Flat Data')
    # set up of menu options
    choice = int(input('\nSelect a Menu Option:'))

    if choice == 1: # load image data from file
        filename = input('Enter name of file to load:')
        image_data = ConsoleGfx.load_file(filename) # read the image data from file into filename
        # assign ConsoleGfx.load_file(filename) to the image_data # filename is user input testfiles/fsu.gfx
        # store the image data in the image_data variable
    elif choice == 2: # load image data from test_image
        # assign the ConsoleGfx.test_image to image_data
        image_data = ConsoleGfx.test_image
    elif choice == 6:
        # display image
        ConsoleGfx.display_image(image_data)






