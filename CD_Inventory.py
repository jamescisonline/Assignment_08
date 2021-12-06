#----------------------------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# James Crockett, 2021-Dec-04, Implemented classes, and main body code
# James Crockett, 2021-Dec-05, A. Implement methods for CD class to store data
#                              B. Tested and Refactored code in main body.
#                              C. Added Error handling.
#                              D. Updated doc strings.
#----------------------------------------------------------------#

#Objectives
# 1. Your task is to read and understand the pseudocode, then add code to 
#    [Done] make the application work. 
# 2. [Done] Make sure to include error handling!
# 3. Update docstrings 
# 4. add your involvement to the header.

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        
        cd_title: (string) with the title of the CD
        
        cd_artist: (string) with the artist of the CD
        
    methods:
        None.
    """
    # Done Add Code to the CD class
    #-- Fields --#
    cd_id = int()
    cd_title = ''
    cd_artist = ''
    #-- Constructor --#
    def __init__(self, i, t, a):
        # -- Attributes -- #
        self.__cd_id = i
        self.__cd_title = t
        self.__cd_artist = a
    # -- Properties --#
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self,value):
        if type(value) is str:
            raise Exception('CD_ID must be an integer')
        else:
            self.__cd_id = value
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self,value):
        if type(value) is int:
            raise Exception('CD_title must be a string')
        else:
            self.__cd_title = value
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self,value):
        if type(value) is int:
            raise Exception('CD_title must be a string')
        else:
            self.__cd_artist = value
    # -- Methods -- #



# -- PROCESSING -- #
class DataProcessor:
    @staticmethod
    def add_cd(val1, val2, val3):        
        """Add CD
                Accepts 3 arguments that are recorded into a dictionary row
                and saved into memory, a 2D table.

        Args:
                val1: used for ID value.
                val2: used for Title.
                val3: used for Artist.

        Returns: 
            None.

        """
        try:
            intID = int(val1)
        except ValueError:
            print('That is not an integer.')
        dicRow = {'ID': intID, 'Title': val2, 'Artist': val3}
        lstOfCDObjects.append(dicRow)
        
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # Done Add code to process data from a file
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        dictRow = {}
        try:
            objFile = open(strFileName, 'a+') #creates text file if it doesn't exist
            objFile.close()
        except FileNotFoundError:
            print('File not found.')
        except OSError:
            print('Error opening or closing file.')

        table.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r') #opens text file for reading
            print(objFile)
            for line in objFile:
                data = line.strip().split(',')
                dictRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dictRow)
            objFile.close()
        except FileNotFoundError:
            print('File not found.')
        except OSError:
            print('Error opening or closing file.')
        except Exception:
            print('Unknown error.')
        
    
    # Done Add code to process data to a file
    @staticmethod
    def write_file(file_name, table):
        """Saves CD list table from memory to text file.

        Args:
            file_name: contains file name value where data is to written.
            
            table: contains value of list table name to save data from.

        Returns: 
            None. 
        """
        # DONE: Add code here
        try:
            objFile = open(file_name, 'w+')#overwrite file to avoid duplicate saves
            for row in table:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        except FileNotFoundError:
            print('File not found.')
        except OSError:
            print('Error opening or closing File.')
        except Exception:
            print('Unknown error.')
    
    


# -- PRESENTATION (Input/Output) -- #
class IO:
    # Done add docstring
    """IO processes input and output data

    properties:
        None

    methods:
        Doc strings for static methods listed below for
        print_menu, menu_choice, show inventory, get_cd_input

    """
    # Done add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[a] Add CD\n[s] Save Inventory to file')
        print('[l] load Inventory from file\n[x] exit\n')
    # Done add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, s, l, x

        """
        choice = ' '
        while choice not in ['a','s','l','x']:
            choice = input('Which operation would you like to perform? [a, s, l or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # Done add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    # Done add code to get CD data from user
    @staticmethod
    def get_cd_input():        
        """Prompt user for three input values for new CD: ID, Title, Artist.

        Args:
            None.

        Returns: 
            Returns a tuple containing ID, Title, and Artist from user inputs.

        """       
        intCdId = int()
        strTitle = None
        strArtist = None
        try:
            intCdId = (int(input('Enter ID: ').strip()))
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
        except ValueError:
            print('That is not an integer.')
        except Exception:
            print('There was a general error.')
        return intCdId, strTitle, strArtist

# -- Main Body of Script -- #
# Done Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.read_file(strFileName, lstOfCDObjects)


while True:
    # Display menu to user
    IO.print_menu()
    
    # show user current inventory
    IO.show_inventory(lstOfCDObjects)

    strChoice = IO.menu_choice()

    # let user add data to the inventory
    if strChoice == 'a':
        #get user input and pass it to CD Class
        strID, strTitle, strArtist = IO.get_cd_input()  
        
        # Pass user input into an instance of the CD Class
        newCd = CD(strID, strTitle, strArtist)
        
        # append values from newCd instance to a table
        DataProcessor.add_cd(newCd.cd_id, newCd.cd_title,newCd.cd_artist)     
        continue  # start loop back at top
    
    # let user save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # save data to file
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            #IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    
    # let user exit program
    if strChoice == 'x':
        break
        # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
        
