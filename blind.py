################################################################################
#####	Creator: Morgan Frisby											   #####
#####	User: 	 Angela Kang											   #####
#####	Purpose: Assist in the blinding process of OJ applications		   #####
#####	Date: 	 February 10, 2019										   #####
################################################################################


import os
from shutil import copyfile
from sys import exit


# global variable that sets the cwd to the home directory's desktop
PATH = "/Users/morganfrisby/Desktop/"


class application_blinding:

	def create_folder(folder_name):
		"""
		Creates a new folder in the global variable specified PATH
		"""
		path = PATH

		try:
			if not os.path.exists(folder_name):
				os.mkdir("%s/" % folder_name)
				print("Successfully created the folder %s" % folder_name)

			else:
				print("Error: The folder %s already exists" % folder_name)

		except OSError:
			print("Error: Could not create the folder %s" % folder_name)


	def remove_folder(folder_name):
		"""
		Removes the folder from the global variable specified PATH
		"""
		path = PATH

		try: 
			if not os.path.exists(folder_name):
				print("Error: The folder %s does not exist" % folder_name)

			else:
				os.rmdir("%s/" % folder_name)
				print ("Successfully deleted the folder %s" % folder_name)

		except OSError:
			print("Error: Could not remove the folder %s" % folder_name)


	def copy_files(input_folder, output_folder):
		"""
		Parses the files in input_folder alphabetically, renames them based on 
		convention MCB_<index_order> and copies the renamed files to output_folder
		"""
		inputPath = PATH+input_folder+"/"
		outputPath = PATH+output_folder+"/"

		index = 1
		for filename in (os.listdir(inputPath)):

			if not filename.startswith('.'):

				renamed = "MCB_" + str(index)

				source = inputPath+filename
				target = outputPath+renamed

				# adding exception handling
				try:
					copyfile(source, target)

				except IOError as e:
				    print("Unable to copy file. %s" % e)
				    exit(1)

				except:
				    print("Unexpected error:", sys.exc_info())
				    exit(1)

				print("\n File %s successfully copied! \n" % filename)

				index += 1





# this is the driver code	
if __name__ == '__main__':

	# current_path = os.getcwd()
	# print("The current working directory is: %s" % current_path)

	# creates a folder in the current working directory named "testing"
	application_blinding.create_folder("testing")

	# removes the folder from the current working directory named "testing"
	# application_blinding.remove_folder("testing")

	# does the filename blinding and copies the blinded files to new folder
	application_blinding.copy_files("test_files", "testing")


