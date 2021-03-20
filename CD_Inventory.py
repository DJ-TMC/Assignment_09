#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# TMcFarland, 2021-Mar-16, addressed TODOs
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO


lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        #Find specific CD from List of CD Objects. Returns cd (object)
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while True:
            #PRINT CD title info & tracks
            IO.ScreenIO.print_CD_menu()
            # Get choice from user
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x': #exit
                break
            elif strChoice == 'a': #add track
                tplTrkInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrkInfo, cd)
            elif strChoice == 'd': #display cd details
                IO.ScreenIO.show_tracks(cd)
            elif strChoice == 'r': #remove track
                IO.ScreenIO.show_tracks(cd)
                rmv_trk = ''
                while rmv_trk == '':
                    rmv_trk = input('Enter Track ID number you wish to remove ').strip()
                    try:
                        rmv_trk = int(rmv_trk)
                    except Exception:
                        print('Please enter a whole number')
                        rmv_trk = ''
                cd.rmv_track(rmv_trk)
            else:
                print('Instructions unclear, Please enter "a", "d", "r", or "x"')
                continue
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    elif strChoice == 't':
        IO.ScreenIO.print_CD_menu
        IO.ScreenIO.test
    else:
        print('General Error')