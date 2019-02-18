################################################################################
#####	Creator: Morgan Frisby											   #####
#####	User: 	 Angela Kang											   #####
#####	Purpose: Assist in the blinding process of OJ applications		   #####
#####	Date: 	 February 10, 2019										   #####
################################################################################


import os
from shutil import copyfile
from sys import exit
from operator import itemgetter

ORIGINAL_DIR = "test_files"
BLINDED_DIR  = "testing"

class application_blinding:

	def create_folder(folder_name):
		"""
		Creates a new folder in the current working directory
		"""
		path = os.path.join(os.getcwd(), folder_name)

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
		Removes the folder from the current working directory
		"""
		path = os.getcwd()

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
		output_dir = {}
		
		inputPath = os.path.join(os.getcwd(), input_folder)
		outputPath = os.path.join(os.getcwd(), output_folder)

		inputFiles = os.listdir(inputPath)

		index = 1
		for filename in sorted(inputFiles, key=itemgetter(0)):

			if not filename.startswith('.'):

				renamed = "MCB_" + str(index)

				source = os.path.join(inputPath, filename)
				target = os.path.join(outputPath, renamed)

				# adding exception handling
				try:
					copyfile(source, target)

				except IOError as e:
				    print("Unable to copy file. %s" % e)
				    exit(1)

				except:
				    print("Unexpected error:", sys.exc_info())
				    exit(1)

				print("\n File %s successfully copied as %s \n" % (filename, renamed))
				output_dir[filename]=renamed
				
				index += 1
		
		print("mapping is ",output_dir)




# this is the driver code	
if __name__ == '__main__':

	# creates a folder in the current working directory named "testing"
    application_blinding.create_folder(BLINDED_DIR)

	# removes the folder from the current working directory named "testing"
	# application_blinding.remove_folder("testing")

	# does the filename blinding and copies the blinded files to new folder
    application_blinding.copy_files(ORIGINAL_DIR, BLINDED_DIR)

