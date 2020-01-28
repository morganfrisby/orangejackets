# OJ Application Binding
This program provides an easy method for performing application binding for the MCB scholarship application.


### Relevant background information:

The Orange Jackets (OJ) organization requires application blinding in their application process in order to mitigate potential sources of bias. Prospective scholarship recipients submit their application through a Google Form online, which is hosted by a single OJ member. Applicants upload a PDF copy of their application through this form, which will have the naming convention “LastnameFirstname_MCB” (Note: MCB is the name of the scholarship they are applying for). The documents themselves do not contain any identifiers, only the names of the files. The Google Form will create a subfolder containing all PDF files submitted via this form. The Google form closes at the application deadline, at which point the folder of PDFs can be downloaded and this program can be run.


### Solution:

This program provides a relatively quick and easy solution to this otherwise-time-intensive process. The program parses the PDFs from the original folder, blinds each name to be of the naming convention “MCB_<index>”, adds the blinded PDFs to a new folder, and creates a csv file with the relationships between original and blinded filenames. The indices start at 1 and correspond to the ascending alphanumeric ordering of the original filenames.


#### Notes:

- The original folder should be downloaded only once, after all submissions are in the folder.
- The output folder should not already be created.
- This assumes that no application files have the same name.
- This does not require the applicants to have correctly followed your naming convention, as the sorting is alphanumeric.


#### Further improvements:

After each app is read by the membership committee members, there’s a Google Form they submit saying “I graded application "MCB_23" and gave them a score of <score>.” The OJ member in charge of handling the scholarship applications has running excel sheet with the blinded applications and the scores they each received. She then sorts the blinded applications by score and has to check the csv file to match the blinded application name back to the original applicant's name to reveal who won the scholarship. A further improvement could be streamlining this process to remove that manual work.


## Instructions:

1. Download [python3](https://www.python.org/downloads/). To confirm this was done correctly, typing `python3 --version` in Terminal should output the expected version of python installed, e.g. `Python 3.6.8`.

2. Go to [my GitHub repository](https://github.com/morganfrisby/orangejackets). In the top right corner, click on the green "Clone or download" button and click on "Download ZIP." This will download a folder named "orangejackets-master" to your computer's Downloads folder, which will contain two files, "blind.py" and "README.md." You only actually need the "blind.py" file.

3. Move the file `blind.py` from your `Downloads/orangejackets-master` folder to some desired location, wherever you want the blinded files to be after running this (Desktop, Downloads, etc.).

4. From Google Drive, download the folder containing all the application submission PDF files. Make sure this is done after the submission deadline and that all the application files are in there.

5. Move that folder from your Downloads to the same desired location from step 3 (Desktop, Downloads, etc.).

6. Open the file `blind.py`. You can do this in any text editor, such as TextEdit, Sublime Text, IntelliJ, etc.

7. At the top of the file, change the global variables so that “test_files” is the name of the downloaded folder with the original PDFs and “testing” is the name you want for the folder with the blinded PDFs:
    
    *  ORIGINAL_DIR = "test_files"
    
    *  BLINDED_DIR  = "testing"

8. Open Terminal (Macs) or Command Prompt (Windows).

9. Type:

    `cd {desired location}` 		    [return]
    
    
    `python3 blind.py > output.txt` 	[return]


That’s it! In your desired location, you will now have the following:

*  `blind.py` ~ this is the file you downloaded from my GitHub and modified to have the right variable names.

*  `ORIGINAL_DIR` ~ this is the folder of downloaded PDF applications with the original names.

*  `output.txt` ~ this is the log of what happened when the program was run; not really important.

*  `blinded.csv` ~ this is a csv file that contains the matching information between original filenames and blinded filenames. This is important to keep so that you can match them back after the blinded applications have been graded.

*  `BLINDED_DIR` ~ this will be a folder (named whatever you name it in step 7 above) that contains all the PDF applications with blinded filenames. These are the files you will give to the OJ members who grade the applications.


#### Questions?

Feel free to reach out to me (Morgan Frisby) if you have any questions about the program, process, etc. or if you have any requests for future improvements.

Email: frisby.morgan@gmail.com
