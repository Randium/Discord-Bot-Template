import config
import sqlite3

conn = sqlite3.connect(config.database)
c = conn.cursor()

def reset(skip = False):
    if skip == False:
        confirm = input("Are you sure you want to reset the data? Any current game progress will be deleted.\nType 'Yes' to proceed. ")
        if confirm != 'Yes':
            print('Resetting canceled.')
            return

    # Reset the game table.
    print('\nDeleting any old progress...')

    if skip == False:
        print('Progress deleted!\n')
        print('Creating space for a new game....')

    print('Formatting completed! The bot is now ready for a new game!\n')

    if skip == False:
        input("Press any button to exit this program.")

if __name__ == "__main__":
    reset()
