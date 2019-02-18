# orangejackets
Application binding program for the MCB scholarship application SP 2019


Relevant background information:

The Orange Jackets (OJ) organization requires application blinding in their application process in order to mitigate potential sources of bias. Prospective scholarship recipients submit their application through a Google Form online, which is hosted by a single OJ member (Angela Kang). Applicants upload a PDF copy of their application through this form, which will have “LastnameFirstname_MCB” as the naming convention (Note: MCB is the name of the scholarship they are applying for). The documents themselves do not contain any identifiers, only the names of the files. The Google Form will create a subfolder containing all PDF files submitted via this form. The application deadline is on February 22, 2019 and the Google Form will close at 5:00pm.


Solution:

This program provides a quick and easy solution to this otherwise-time-intensive process. The program parses the PDFs from the original folder, blinds each name to be of the naming convention “MCB_<index>”, adds the blinded PDFs to a new folder, and creates a csv file with the relationships between original and blinded filenames. The indices start at 1 and correspond to the ascending alphanumeric ordering of the original filenames. 


Notes:

If you want the ordering based on something else (such as timestamp), I can play with that
The original folder should be downloaded only once, after all submissions are in the folder
The output folder should not already be created
This relies on files not having the same original names
This does not require the applicants to have correctly followed your naming convention

Further improvements:

After each app is read by the membership committee members, there’s a Google Form they submit saying “I graded application ‘MCB_23’ and gave them a score of <score>.” NG has running excel sheet with the blinded applications they scored and the scores they gave them. She then sorts by number and adds column by names and identify what goes with what. 
→ Could I make this easier?


Instructions:

1. Download python3

2. Go to my GitHub repository

3. Download the program file (blind.py) to your laptop

4. Move the file from your Downloads to desired location (Desktop, Downloads, etc.)

5. Download the application submission folder containing all the PDFs (from Google Drive)

6. Move that folder from your Downloads to same desired location (Desktop, Downloads, etc.)

7. Open the file blind.py

8. At the top of the file, change the global variables so that “test_files” is the name of the downloaded folder with the original PDFs and “testing” is the name you want for the folder with the blinded PDFs:
    a. ORIGINAL_DIR = "test_files"
    b. BLINDED_DIR  = "testing"

9. Open Command Prompt

10. Type: 
    cd (desired location) 		[return]
    python3 blind.py > output.txt 	[return]


That’s it! In the desired location, you will now have the following:

blind.py
  The program file

ORIGINAL_DIR
  This is the folder of downloaded PDF applications with the original names

output.txt
  This is the log of what happened when the program was run.

blinded.csv
  This is a csv file that contains the matching information between original filenames and blinded filenames. You can save this as an excel spreadsheet!

BLINDED_DIR
  This will be a folder (named whatever you name it in step 8b. above) that contains all the PDF applications with blinded filenames.
