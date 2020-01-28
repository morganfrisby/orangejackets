###############################################################
#  Author:  Morgan Frisby
#  User: 	Angela Kang
#  Purpose: Assist in the blinding process of OJ applications
#  Date: 	February 17, 2019
###############################################################


import os
import sys
from shutil import copyfile
from operator import itemgetter
import csv

"""
ORIGINAL_DIR - the name of the downloaded folder that has the original application files.
BLINDED_DIR  - the name of the folder that will have the blinded application files.
"""
ORIGINAL_DIR = "test_files"  # <-- change this!
BLINDED_DIR = "testing"  # <------ change this!


def create_folder(folder_name):
    """ Creates a new folder in the current working directory. """
    try:
        if not os.path.exists(folder_name):
            os.mkdir(f"{folder_name}/")
            print(f"Successfully created the folder {folder_name}.")
        else:
            print(f"Error: The folder {folder_name} already exists.")
    except OSError:
        print(f"Error: Could not create the folder {folder_name}.")


def remove_folder(folder_name):
    """ Removes the folder from the current working directory. """
    try:
        if not os.path.exists(folder_name):
            print(f"Error: The folder {folder_name} does not exist.")
        else:
            os.rmdir(f"{folder_name}/")
            print(f"Successfully deleted the folder {folder_name}.")
    except OSError:
        print(f"Error: Could not remove the folder{folder_name}.")


def copy_files(input_folder, output_folder):
    """ Parses the files in input_folder alphabetically, renames them based on the convention MCB_<index_order> and
    copies the renamed files to output_folder. """

    input_path = os.path.join(os.getcwd(), input_folder)
    output_path = os.path.join(os.getcwd(), output_folder)
    input_files = os.listdir(input_path)
    index = 1
    output_dir = {}

    for filename in sorted(input_files, key=itemgetter(0)):
        if not filename.startswith("."):
            renamed = "MCB_" + str(index)
            source = os.path.join(input_path, filename)
            target = os.path.join(output_path, renamed)
            try:
                copyfile(source, target)
            except IOError as e:
                print(f"Unable to copy file. Error: {e}")
                sys.exit(1)
            except:
                print("Unexpected error:", sys.exc_info())
                sys.exit(1)

            print(f"\n File {filename} successfully copied as {renamed}. \n")
            output_dir[filename] = renamed
            index += 1
    print(f"mapping is {output_dir}.")

    with open("blinded.csv", "w") as output:
        writer = csv.writer(output)
        for orig, blind in output_dir.items():
            writer.writerow([orig, blind])


if __name__ == "__main__":
    create_folder(BLINDED_DIR)
    # remove_folder(BLINDED_DIR)
    copy_files(ORIGINAL_DIR, BLINDED_DIR)
