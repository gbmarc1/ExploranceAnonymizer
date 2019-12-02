Disclamer
=========

This tools is used to help anonymize comments from a utf-8 encoded .csv file. 

`Dr. Dolittle is a great veterinarian.   ->  Dr. <PERSON> is a great veterinarian.`

There are NO guaranties that this tool will. The script may produce the following errors:

    - People name will all be replaced by the token `<PERSON>`.
        `Dr. Dolittle is a great veterinarian.   ->  Dr. Dolittle is a great veterinarian.`
    - Some non-people part of the text will be NOT replaced by the token `<PERSON>`.
        `Dr. Dolittle is a great veterinarian.   ->  Dr. <PERSON> is a great <PERSON>.`

Anti Virus
==========
It can happend that `exploranceanonymizer.exe` be detected has a threat to your
computer. Do NOT worry it is ok. Allow and/or restore the file if the file was 
quarantined.

The source code is available here:

`https://github.com/gbmarc1/ExploranceAnonymizer`

OPERATING SYSTEM
================
The built version of this tool is windows compatible only. The python script version in
the github repository is compatible across all platforms.


HOW TO RUN
==========

BUILT VERSION
-------------
On windows run the `ExploranceAnonymizer.bat`, and enter the `.csv` file path when
prompted.

PYTHON SCRIPT
--------------

    - Activate your virtual environment
    - Run `python __main__.py --file "your_comment_csv.csv"`


HOW TO BUILD FROM SOURCE
========================
On windows, 

    - Activate your virtual environment
    - Run `build.bat`






