import sys
import os
import datetime
import time

import pyauto
from keyhac import *


def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    if 1:
        keymap.editor = "C:\Program Files (x86)\sakura\sakura.exe"

    # Setting with callable object (Advanced usage)
    if 0:
        def editor(path):
            shellExecute( None, "notepad.exe", '"%s"'% path, "" )
        keymap.editor = editor

    # --------------------------------------------------------------------
    # Customizing the display

    # Font
    keymap.setFont( "MS Gothic", 12 )

    # Theme
    keymap.setTheme("black")

    # --------------------------------------------------------------------

    # Global keymap which affects any windows
    if 1:
        keymap_global = keymap.defineWindowKeymap()

        # IME change
        keymap_global[ "C-Space" ] = "A-Tilde"           # IME ON/OFF
        #keymap_global[ "S-Space" ] = "A-Tilde"           # IME ON/OFF

        # Swap
        keymap_global[ "Semicolon" ] = "S-Colon"         # Colon
        keymap_global[ "S-Colon" ] = "Semicolon"         # Semicolon

        # Move
        keymap_global[ "C-K" ] = "Up"                    # Move cursor up
        keymap_global[ "C-J" ] = "Down"                  # Move cursor down
        keymap_global[ "C-L" ] = "Right"                 # Move cursor right
        keymap_global[ "C-H" ] = "Left"                  # Move cursor left
        keymap_global[ "C-A" ] = "Home"                  # Move cursor home
        keymap_global[ "C-E" ] = "End"                   # Move cursor end
        keymap_global[ "C-I" ] = "A-Right"               # Forword
        keymap_global[ "C-O" ] = "A-Left"                # Back
        keymap_global[ "C-F" ] = "C-Right"               # Move to forward word
        keymap_global[ "C-B" ] = "C-Left"                # Move to back word
        keymap_global[ "C-D" ] = ["Down"]*32             # Scroll half page down
        keymap_global[ "C-U" ] = ["Up"]*32               # Scroll half page up

        # Select
        keymap_global[ "C-S-J" ] = "S-Down"              # Select down
        keymap_global[ "C-S-K" ] = "S-Up"                # Select up
        keymap_global[ "C-S-L" ] = "S-Right"             # Select right
        keymap_global[ "C-S-H" ] = "S-Left"              # Select left
        keymap_global[ "C-S-A" ] = "S-Home"              # Select until beginning of line
        keymap_global[ "C-S-E" ] = "S-End"               # Select until end of line

        # Edit
        keymap_global[ "C-Enter" ] = "F2"                # Edit
        keymap_global[ "C-W" ] = "C-S-Left","Delete"     # Delete back word
        keymap_global[ "C-Y" ] = "C-S-Right","Delete"    # Delete forward word
        keymap_global[ "C-G" ] = "S-End","Delete"        # Delete text until the end of the line
        keymap_global[ "C-T" ] = "S-Home","Delete"       # Delete text until the beiginning of the line

        keymap_global[ "C-Delete" ] = "S-End","Delete"   # Delete text until the end of the line
        keymap_global[ "C-Back" ] = "S-Home","Delete"    # Delete text until the beiginning of the line
        keymap_global[ "C-Period" ] = "C-C"              # Copy
        keymap_global[ "C-Comma" ] = "S-Insert"          # Paste
        #keymap_global[ "S-Space" ] = "S-Insert"          # Paste
        #keymap_global[ "C-Colon" ] = "Delete"            # Delete
        #keymap_global[ "C-Quote" ] = "Back"              # Backspace
        keymap_global[ "C-OpenBracket" ] = "Back"         # Backspace
        keymap_global[ "C-CloseBracket" ] = "Delete"      # Delete
        #keymap_global[ "C-Comma" ] = "Back"              # Backspace
        #keymap_global[ "C-Period" ] = "Delete"           # Delete

        # Task switching
        keymap_global[ "LAlt-Quote" ] = "C-LAlt-Tab"     # Next multitasking view (hold)
        # keymap_global[ "LAlt-Tab" ] = "C-LAlt-Tab"       # Next multitasking view (hold)
        # keymap_global[ "LAlt-J" ] = "C-LAlt-Tab"         # Next multitasking view (hold)
        # keymap_global[ "LAlt-K" ] = "C-LAlt-S-Tab"       # Next multitasking view (hold)
        keymap_global[ "LAlt-Semicolon" ] = "LAlt-Tab"           # Next multitasking view
        keymap_global[ "LAlt-J" ] = "LAlt-Tab"           # Next multitasking view
        keymap_global[ "LAlt-K" ] = "LAlt-S-Tab"         # Previous multitasking view
 
        # Tab switching
        keymap_global[ "LAlt-L" ] = "C-Tab"              # Next tab
        keymap_global[ "LAlt-H" ] = "C-S-Tab"            # Previous tab

        # Desktop switching
        # keymap_global[ "A-OpenBracket" ] = "LWin-C-Left"    # Next desktop region
        # keymap_global[ "A-CloseBracket" ] = "LWin-C-Right"  # Previous desktop region
        keymap_global[ "LAlt-Comma" ] = "LWin-C-Left"       # Next desktop region
        keymap_global[ "LAlt-Period" ] = "LWin-C-Right"     # Previous desktop region

        # Window snapping
        keymap_global[ "LAlt-Minus" ] = "LWin-Down"             # Minimize window
        keymap_global[ "LAlt-Plus" ] = "LWin-Up"                # Maximize window
        keymap_global[ "LAlt-OpenBracket" ] = "LWin-Left"       # Left snap
        keymap_global[ "LAlt-CloseBracket" ] = "LWin-Right"     # Right snap

        # Windows shortcut key
        keymap_global[ "A-A" ] = "C-A"                   # Select all
        # keymap_global[ "A-B" ] = "C-B"                   # Bold
        keymap_global[ "A-C" ] = "C-C"                   # Copy
        keymap_global[ "A-F" ] = "C-F"                   # Search
        keymap_global[ "A-G" ] = "C-G"                   # Grep
        # keymap_global[ "A-I" ] = "C-I"                   # Itaric
        keymap_global[ "A-N" ] = "C-N"                   # New
        keymap_global[ "A-S" ] = "C-S"                   # Save
        # keymap_global[ "A-Minus" ] = "C-U"               # Underbar
        keymap_global[ "A-V" ] = "C-V"                   # Paste
        keymap_global[ "A-W" ] = "C-W"                   # Close
        keymap_global[ "A-X" ] = "C-X"                   # Cut
        keymap_global[ "A-Y" ] = "C-Y"                   # Redo
        keymap_global[ "A-Z" ] = "C-Z"                   # Undo
        # keymap_global[ "S-Space" ] = "LWin-S"            # Search App
        keymap_global[ "C-S-Space" ] = "LWin-X"          # Advance menu

        # Undo/Redo
        keymap_global[ "A-U" ] = "C-Z"                   # Undo
        keymap_global[ "A-R" ] = "C-Y"                   # Redo

        # Keyhac
        keymap_global[ "C-F8" ] = keymap.command_EditConfig    # Edit config file
        keymap_global[ "C-F9" ] = keymap.command_ReloadConfig  # Relaod config file
        
        # Misc
        keymap_global[ "F1" ] = "Esc"                    # Escape
        keymap_global[ "S-F1" ] = "F1"                   # F1

    # Explorer keymap
    if 1:
        keymap_explorer = keymap.defineWindowKeymap( exe_name="explorer.exe" )

        keymap_explorer[ "C-M" ] = ["C-Tab"]*2               # Forcus library window
        keymap_explorer[ "C-Slash" ] = ["C-Tab","S-Tab"]*2   # Forcus navigation window
        #keymap_explorer[ "A-U" ] = "A-Up"                # Move up

    # Multitasking view keymap
    if 1:
        keymap_taskview = keymap.defineWindowKeymap( exe_name="explorer.exe", class_name="MultitaskingViewFrame" )

        # keymap_taskview[ "J" ] = "Down"                  # Down
        # keymap_taskview[ "K" ] = "Up"                    # Up
        keymap_taskview[ "J" ] = "Right"                 # Right
        keymap_taskview[ "K" ] = "Left"                  # Left
        keymap_taskview[ "L" ] = "Right"                 # Right
        keymap_taskview[ "H" ] = "Left"                  # Left
        keymap_taskview[ "Space" ] = "Enter"             # Enter
        keymap_taskview[ "M" ] = "Enter"                 # Enter
        keymap_taskview[ "N" ] = "Esc"                   # Escape
        keymap_taskview[ "1" ] = "Left","Enter"                   # Select right task based on 2nd task
        keymap_taskview[ "2" ] = "Enter"                          # Select right task based on 2nd task
        keymap_taskview[ "3" ] = "Right","Enter"                  # Select right task based on 2nd task
        keymap_taskview[ "4" ] = "Right","Right","Enter"          # Select right task based on 2nd task
        keymap_taskview[ "5" ] = "Right","Right","Right","Enter"  # Select right task based on 2nd task

    # Multitasking view keymap
    # if 1:
    #     keymap_winmenu = keymap.defineWindowKeymap( exe_name="explorer.exe", class_name="LauncherTipWnd" )

    #     keymap_winmenu[ "S" ] = "U", "S"                 # Sleep

    # Mintty keymap
    if 1:
        keymap_mintty = keymap.defineWindowKeymap( exe_name="mintty.exe", class_name="mintty" )

        keymap_mintty[ "C-K" ] = "C-K"                   # Default
        keymap_mintty[ "C-J" ] = "C-J"                   # Default
        keymap_mintty[ "C-L" ] = "C-L"                   # Default
        keymap_mintty[ "C-H" ] = "C-H"                   # Default
        keymap_mintty[ "C-A" ] = "C-A"                   # Default
        keymap_mintty[ "C-E" ] = "C-E"                   # Default
        #keymap_mintty[ "C-S-J" ] = "C-Tab"               # Next window
        #keymap_mintty[ "C-S-K" ] = "C-S-Tab"             # Previous window
        keymap_mintty[ "C-I" ] = "C-I"                   # Default
        keymap_mintty[ "C-O" ] = "C-O"                   # Default
        keymap_mintty[ "C-F" ] = "C-F"                   # Default
        keymap_mintty[ "C-B" ] = "C-B"                   # Default
        keymap_mintty[ "C-W" ] = "C-W"                   # Default
        keymap_mintty[ "C-Y" ] = "C-Y"                   # Default
        keymap_mintty[ "C-D" ] = "C-D"                   # Default
        keymap_mintty[ "C-U" ] = "C-U"                   # Default

    # Windows Terminal keymap
    if 1:
        keymap_winterm = keymap.defineWindowKeymap( exe_name="WindowsTerminal.exe", class_name="Windows.UI.Input.InputSite.WindowClass" )

        #keymap_winterm[ "C-P" ] = "Up"                   # Previous history
        #keymap_winterm[ "C-N" ] = "Down"                 # Next history
        #keymap_winterm[ "C-K" ] = "C-K"                  # Default
        #keymap_winterm[ "C-J" ] = "C-J"                  # Default
        #keymap_winterm[ "C-L" ] = "C-L"                  # Default
        #keymap_winterm[ "C-H" ] = "C-H"                  # Default
        keymap_winterm[ "C-A" ] = "C-A"                  # Default
        keymap_winterm[ "C-E" ] = "C-E"                  # Default
        keymap_winterm[ "C-G" ] = "C-G"                  # Default
        keymap_winterm[ "C-Y" ] = "C-Y"                  # Default
        keymap_winterm[ "C-T" ] = "C-T"                  # Default
        #keymap_winterm[ "C-S-J" ] = "C-Tab"              # Next window
        #keymap_winterm[ "C-S-K" ] = "C-S-Tab"            # Previous window
        keymap_winterm[ "C-I" ] = "C-I"                  # Default
        keymap_winterm[ "C-O" ] = "C-O"                  # Default
        keymap_winterm[ "C-F" ] = "C-F"                  # Default
        keymap_winterm[ "C-B" ] = "C-B"                  # Default
        keymap_winterm[ "C-W" ] = "C-W"                  # Default
        keymap_winterm[ "C-Y" ] = "C-Y"                  # Default
        keymap_winterm[ "C-D" ] = "C-D"                  # Default
        keymap_winterm[ "C-U" ] = "C-U"                  # Default
        #keymap_winterm[ "A-H" ] = "A-H"                  # Default
        #keymap_winterm[ "A-L" ] = "A-L"                  # Default
        keymap_winterm[ "A-W" ] = "A-F3"                 # Close
        keymap_winterm[ "C-S-J" ] = "C-S-J"              # Default
        keymap_winterm[ "C-S-K" ] = "C-S-K"              # Default
        keymap_winterm[ "C-Enter" ] = "C-Enter"          # Default

    # Edge keymap
    if 1:
        keymap_edge = keymap.defineWindowKeymap( exe_name="msedge.exe", class_name="Chrome_WidgetWin_1" )

        #keymap_edge[ "C-E" ] = "C-E"                     # Default
        #keymap_edge[ "C-Backslash" ] = "C-L"             # Default
        #keymap_edge[ "C-S-Back" ] = "C-W"                # Close tab
        #keymap_edge[ "C-Slash" ] = "Slash"               # Search
        #keymap_edge[ "C-M" ] = "Tab","Esc"                # Cancel

    # Chrome keymap
    if 1:
        keymap_chrome = keymap.defineWindowKeymap( exe_name="chrome.exe", class_name="Chrome_WidgetWin_1" )

        #keymap_chrome[ "C-M" ] = "Tab","Esc"             # Cancel
        keymap_chrome[ "A-T" ] = "C-T"                   # Open tab
        keymap_chrome[ "LAlt-I" ] = "C-S-C"              # Element to inspection
        keymap_chrome[ "O-LAlt" ] = "Esc"                # Escape
        keymap_chrome[ "C-Slash" ] = "A-D"               # Address Bar

    # FireFox keymap
    if 1:
        keymap_firefox = keymap.defineWindowKeymap( exe_name="firefox.exe", class_name="MozillaWindowClass" )

        #keymap_firefox[ "C-M" ] = "Tab","Esc"             # Cancel
        keymap_firefox[ "A-T" ] = "C-T"                   # Open tab
        keymap_firefox[ "LAlt-I" ] = "C-S-C"              # Element to inspection
        keymap_firefox[ "O-LAlt" ] = "Esc"                # Escape

    # Excel keymap
    if 1:
        keymap_excel = keymap.defineWindowKeymap( exe_name="excel.exe" )

        keymap_excel[ "C-Comma" ] = "S-F10","V","C-C"    # Paste value
        #keymap_excel[ "S-Space" ] = "S-F10","V","C-C"    # Paste value
        keymap_excel[ "C-LWin-K" ] = "C-Up"              # Move cursor upward data
        keymap_excel[ "C-LWin-J" ] = "C-Down"            # Move cursor down data
        keymap_excel[ "C-LWin-L" ] = "C-Right"           # Move cursor right data
        keymap_excel[ "C-LWin-H" ] = "C-Left"            # Move cursor left data
        keymap_excel[ "C-S-LWin-K" ] = "C-S-Up"          # Select upward data
        keymap_excel[ "C-S-LWin-J" ] = "C-S-Down"        # Select down data
        keymap_excel[ "C-S-LWin-L" ] = "C-S-Right"       # Select right data
        keymap_excel[ "C-S-LWin-H" ] = "C-S-Left"        # Select left data
        #keymap_excel[ "C-Period" ] = "F4"                # Repeat
        keymap_excel[ "C-A-D" ] = "C-D"                  # Duplicate
        keymap_excel[ "C-A-U" ] = "C-U"                  # Underline
        keymap_excel[ "C-D" ] = ["Down"]*32              # Move half page down
        keymap_excel[ "C-U" ] = ["Up"]*32                # Move uhalf page up
        keymap_excel[ "A-Q" ] = "A-F4"                   # Quit
        keymap_excel[ "O-LAlt" ] = "Esc"                 # Escape

        # Tab switching
        keymap_excel[ "LAlt-L" ] = "C-PageDown"          # Next tab
        keymap_excel[ "LAlt-H" ] = "C-PageUp"            # Previous tab
        
        if 1:
            keymap_excel[ "C-S-O" ] = "S-Space"          # Select line
            keymap_excel[ "C-S-I" ] = "C-Space"          # Select column
            keymap_excel[ "C-S-Y" ] = "C-C"              # Yank
            keymap_excel[ "C-S-P" ] = "C-S-Plus","C-C"   # Insert yanked cell
            keymap_excel[ "C-S-N" ] = "Esc","C-S-Plus"   # Insert
            keymap_excel[ "C-S-G" ] = "C-Minus"          # Delete
            keymap_excel[ "C-S-D" ] = "C-D"              # Duplicate
        else:
            keymap_excel[ "C-S-O" ] = "S-Space"                                                     # Select line
            keymap_excel[ "C-S-I" ] = "C-Space"                                                     # Select column
            keymap_excel[ "C-S-Y" ] = keymap.defineMultiStrokeKeymap( "C-S-Y" )
            keymap_excel[ "C-S-Y" ][ "C-S-Y" ] = "S-Space","C-C"                                    # Yank line
            keymap_excel[ "C-S-Y" ][ "C-S-I" ] = "C-Space","C-C"                                    # Yank column
            keymap_excel[ "C-S-Y" ][ "C-S-O" ] = "C-C"                                              # Yank cell
            keymap_excel[ "C-S-P" ] = keymap.defineMultiStrokeKeymap( "C-S-P" )
            keymap_excel[ "C-S-P" ][ "C-S-P" ] = "S-Space","Alt","H","I","E","S-Space","C-C"    # Insert yanked line and Yank
            keymap_excel[ "C-S-P" ][ "C-S-I" ] = "C-Space","Alt","H","I","E","C-Space","C-C"    # Insert yanked column and Yank
            keymap_excel[ "C-S-P" ][ "C-S-O" ] = "Alt","H","I","2","E"                              # Insert yanked cell
            keymap_excel[ "C-S-N" ] = keymap.defineMultiStrokeKeymap( "C-S-N" )
            keymap_excel[ "C-S-N" ][ "C-S-N" ] = "Esc","S-Space","Alt","H","I","R"              # Insert new line
            keymap_excel[ "C-S-N" ][ "C-S-I" ] = "Esc","C-Space","Alt","H","I","C"              # Insert new column
            keymap_excel[ "C-S-N" ][ "C-S-O" ] = "Esc","Alt","H","I","I"                            # Insert new cell
            keymap_excel[ "C-S-D" ] = keymap.defineMultiStrokeKeymap( "C-S-D" )
            keymap_excel[ "C-S-D" ][ "C-S-D" ] = "Alt","H","D","R"                                  # Delete line
            keymap_excel[ "C-S-D" ][ "C-S-I" ] = "Alt","H","D","C"                                  # Delete column
            keymap_excel[ "C-S-D" ][ "C-S-O" ] = "Alt","H","D","D"                                  # Delete cell
            keymap_excel[ "C-S-F" ] = keymap.defineMultiStrokeKeymap( "C-S-F" )
            keymap_excel[ "C-S-F" ][ "C-S-F" ] = "Alt","H","F","I","S","Enter"                      # Auto fill


    # Word keymap
    if 1:
        keymap_word = keymap.defineWindowKeymap( exe_name="winword.exe" )

        keymap_word[ "A-Q" ] = "A-F4"                    # Quit

    # Sakura keymap
    if 1:
        keymap_sakura = keymap.defineWindowKeymap( exe_name="sakura.exe", class_name="SakuraView176" )

        keymap_sakura[ "A-W" ] = "C-F4"                  # Close
        keymap_sakura[ "A-Q" ] = "C-A-F4"                # Quit

    # Acrobat keymap
    if 1:
        keymap_acrobat = keymap.defineWindowKeymap( exe_name="Acrobat.exe", class_name="AVL_AVView"  )

        keymap_acrobat[ "C-J" ] = "Down"                 # Move down
        keymap_acrobat[ "C-K" ] = "Up"                   # Move up
        keymap_acrobat[ "C-H" ] = "Left"                 # Move left
        keymap_acrobat[ "C-L" ] = "Right"                # Move right
        keymap_acrobat[ "C-G" ] = keymap.defineMultiStrokeKeymap( "G" )
        keymap_acrobat[ "C-G" ][ "C-G" ] = "Home"        # Move top
        keymap_acrobat[ "C-G" ][ "G" ] = "End"           # Move bottom
        keymap_acrobat[ "C-D" ] = ["Down"]*32            # Move half page down
        keymap_acrobat[ "C-U" ] = ["Up"]*32              # Move uhalf page up
        keymap_acrobat[ "C-F" ] = ["Down"]*64            # Move half page down
        keymap_acrobat[ "C-B" ] = ["Up"]*64              # Move uhalf page up
        keymap_acrobat[ "C-E" ] = ["Down"]*2             # Move down (Triple)
        keymap_acrobat[ "C-Y" ] = ["Up"]*2               # Move up (Triple)
        keymap_acrobat[ "A-Q" ] = "A-F4"                 # Quit

    # Select word and Search
    if 1:
        keymap_global = keymap.defineWindowKeymap()

        def command_Search():
            # Copy selected word
            terminals = ["WindowsTerminal.exe", "cmd.exe", "powershell.exe"]
            wnd = Window.getForeground()
            if wnd:
                currProcessName = wnd.getProcessName()
                # print("1:",currProcessName)
                if not currProcessName in terminals:
                    # print('copy')
                    keymap.InputKeyCommand("C-C")()
                    if currProcessName == "chrome.exe":
                        # print('vim copy')
                        wnd = wnd.getLastActivePopup()
                        currProcessName = wnd.getProcessName()
                        # print("AA:", currProcessName)
                        # wnd.setForeground()
                        # wnd.setActive()
                        keymap.InputKeyCommand("v","y")()
            else:
                # print('no action')
                return

            # Activate chrome window or launch
            wnd = Window.find( "Chrome_WidgetWin_1", None )
            newProcessName = wnd.getProcessName()
            # print("2:", newProcessName)
            # if wnd:
            if newProcessName == "chrome.exe":
                if wnd.isMinimized():
                    wnd.restore()
                if newProcessName != currProcessName:
                    wnd = wnd.getLastActivePopup()
                    # print('foreground')
                    wnd.setForeground()
                    time.sleep(0.05)
                    # wnd.setActive()
                    # print('activate')
            else:
                executeFunc = keymap.ShellExecuteCommand( None, "chrome.exe", "", "" )
                executeFunc()
                # print('launch')
                return

            # Create new tab and Search
            keymap.InputKeyCommand("C-T", "C-V", "Enter")()
            # keymap.InputKeyCommand("C-T")()
            # time.sleep(0.15)
            # keymap.InputKeyCommand("C-V")()
            # time.sleep(0.15)
            # keymap.InputKeyCommand("Enter")()
            # time.sleep(0.15)

        keymap_global[ "S-C-Backslash" ] = command_Search

    if 0:
        keymap_global = keymap.defineWindowKeymap()

        def command_Test():
            wnd = Window.find( "Chrome_WidgetWin_1", None )
            if wnd:
                # wnd = wnd.getLastActivePopup()
                wnd.setForeground()
                # wnd.setActive()
                newProcessName = wnd.getProcessName()
                print("new:", newProcessName)
            # keymap.InputKeyCommand("C-T","C-V","Enter")()
            keymap.InputKeyCommand("C-T")()
            time.sleep(0.01)
            keymap.InputKeyCommand("C-V")()
            time.sleep(0.01)
            keymap.InputKeyCommand("Enter")()
            time.sleep(0.01)

        keymap_global[ "C-F12" ] = command_Test


#    # Simple key replacement
#    keymap.replaceKey( "LWin", 235 )
#    keymap.replaceKey( "RWin", 255 )
#
#    # User modifier key definition
#    keymap.defineModifier( 235, "User0" )
#
#    # USER0-F1 : Test of launching application
#    if 0:
#        keymap_global[ "U0-F1" ] = keymap.ShellExecuteCommand( None, "notepad.exe", "", "" )


#    # USER0-F2 : Test of sub thread execution using JobQueue/JobItem
#    if 0:
#        def command_JobTest():
#
#            def jobTest(job_item):
#                shellExecute( None, "notepad.exe", "", "" )
#
#            def jobTestFinished(job_item):
#                print( "Done." )
#
#            job_item = JobItem( jobTest, jobTestFinished )
#            JobQueue.defaultQueue().enqueue(job_item)
#
#        keymap_global[ "U0-F2" ] = command_JobTest


#    # Test of Cron (periodic sub thread procedure)
#    if 0:
#        def cronPing(cron_item):
#            os.system( "ping -n 3 www.google.com" )
#
#        cron_item = CronItem( cronPing, 3.0 )
#        CronTable.defaultCronTable().add(cron_item)


#    # USER0-F : Activation of specific window
#    if 0:
#        keymap_global[ "U0-F" ] = keymap.ActivateWindowCommand( "cfiler.exe", "CfilerWindowClass" )


#    # USER0-E : Activate specific window or launch application if the window doesn't exist
#    if 0:
#        def command_ActivateOrExecuteNotepad():
#            wnd = Window.find( "Notepad", None )
#            if wnd:
#                if wnd.isMinimized():
#                    wnd.restore()
#                wnd = wnd.getLastActivePopup()
#                wnd.setForeground()
#            else:
#                executeFunc = keymap.ShellExecuteCommand( None, "notepad.exe", "", "" )
#                executeFunc()
#
#        keymap_global[ "U0-E" ] = command_ActivateOrExecuteNotepad


    # Ctrl-Tab : Switching between console related windows
    if 1:

        def isConsoleWindow(wnd):
            if wnd.getClassName() in ("PuTTY","MinTTY","CkwWindowClass"):
                return True
            return False

        keymap_console = keymap.defineWindowKeymap( check_func=isConsoleWindow )

        def command_SwitchConsole():

            root = pyauto.Window.getDesktop()
            last_console = None

            wnd = root.getFirstChild()
            while wnd:
                if isConsoleWindow(wnd):
                    last_console = wnd
                wnd = wnd.getNext()

            if last_console:
                last_console.setForeground()

        keymap_console[ "C-TAB" ] = command_SwitchConsole


#    # Execute the System commands by sendMessage
#    if 0:
#        def close():
#            wnd = keymap.getTopLevelWindow()
#            wnd.sendMessage( WM_SYSCOMMAND, SC_CLOSE )
#
#        def screenSaver():
#            wnd = keymap.getTopLevelWindow()
#            wnd.sendMessage( WM_SYSCOMMAND, SC_SCREENSAVE )
#
#        keymap_global[ "U0-C" ] = close              # Close the window
#        keymap_global[ "U0-S" ] = screenSaver        # Start the screen-saver


#    # Test of text input
#    if 0:
#        keymap_global[ "U0-H" ] = keymap.InputTextCommand( "Hello / こんにちは" )


    # For Edit box, assigning Delete to C-D, etc
    if 0:
        keymap_edit = keymap.defineWindowKeymap( class_name="Edit" )

        keymap_edit[ "C-D" ] = "Delete"              # Delete
        keymap_edit[ "C-H" ] = "Back"                # Backspace
        keymap_edit[ "C-K" ] = "S-End","C-X"         # Removing following text


    # Customize Notepad as Emacs-ish
    # Because the keymap condition of keymap_edit overlaps with keymap_notepad,
    # both these two keymaps are applied in mixed manner.
    if 0:
        keymap_notepad = keymap.defineWindowKeymap( exe_name="notepad.exe", class_name="Edit" )

        # Define Ctrl-X as the first key of multi-stroke keys
        keymap_notepad[ "C-X" ] = keymap.defineMultiStrokeKeymap("C-X")

        keymap_notepad[ "C-P" ] = "Up"                  # Move cursor up
        keymap_notepad[ "C-N" ] = "Down"                # Move cursor down
        keymap_notepad[ "C-F" ] = "Right"               # Move cursor right
        keymap_notepad[ "C-B" ] = "Left"                # Move cursor left
        keymap_notepad[ "C-A" ] = "Home"                # Move to beginning of line
        keymap_notepad[ "C-E" ] = "End"                 # Move to end of line
        keymap_notepad[ "A-F" ] = "C-Right"             # Word right
        keymap_notepad[ "A-B" ] = "C-Left"              # Word left
        keymap_notepad[ "C-V" ] = "PageDown"            # Page down
        keymap_notepad[ "A-V" ] = "PageUp"              # page up
        keymap_notepad[ "A-Comma" ] = "C-Home"          # Beginning of the document
        keymap_notepad[ "A-Period" ] = "C-End"          # End of the document
        keymap_notepad[ "C-X" ][ "C-F" ] = "C-O"        # Open file
        keymap_notepad[ "C-X" ][ "C-S" ] = "C-S"        # Save
        keymap_notepad[ "C-X" ][ "C-W" ] = "A-F","A-A"  # Save as
        keymap_notepad[ "C-X" ][ "U" ] = "C-Z"          # Undo
        keymap_notepad[ "C-S" ] = "C-F"                 # Search
        keymap_notepad[ "A-X" ] = "C-G"                 # Jump to specified line number
        keymap_notepad[ "C-X" ][ "H" ] = "C-A"          # Select all
        keymap_notepad[ "C-W" ] = "C-X"                 # Cut
        keymap_notepad[ "A-W" ] = "C-C"                 # Copy
        keymap_notepad[ "C-Y" ] = "C-V"                 # Paste
        keymap_notepad[ "C-X" ][ "C-C" ] = "A-F4"       # Exit
