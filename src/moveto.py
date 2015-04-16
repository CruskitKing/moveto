import sys
import os
import shutil
import logging


def checkInputs():
    if sys.argv[1][0] == ".":
        if len(sys.argv[1]) > 1:
            print "Merging Directory with CWD"
            directory = os.path.join(os.getcwd(), sys.argv[1][2:])
            print directory
        else:
            directory = os.getcwd()
    else:
        directory = sys.argv[1]

    if not os.path.isdir(directory):
        raise ValueError("Invalid Directory")

    search = sys.argv[2]

    return directory, search

######################


def moveto(directory, search):
    for root, folder, files in list(os.walk(directory))[1:]:
        for f in files:
            if f in [x for x in os.listdir(directory) if os.path.isfile(x)]:
                print f + " already exists in " + directory
                continue
            if search in f:
                # os.rename(os.path.join(root, f), os.path.join(directory, os.path.basename(f)))
                shutil.copy2(os.path.join(root, f), os.path.join(directory, os.path.basename(f)))
                print "Moved \"" + f + "\" from " + root

############################################

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print """
-- moveto directory search

Moves all files in the directory and subdirectories with the search term to the directory """
    elif sys.argv[1] == "undo":
        print "To Be Implemented"
    elif len(sys.argv) == 3:
        try:
            print
            directory, search = checkInputs()
            moveto(directory, search)
        except IOError as e:
            print e
        except ValueError as e:
            print e
        except shutil.Error as e:
            print e
    else:
        print "Invalid Parameters"