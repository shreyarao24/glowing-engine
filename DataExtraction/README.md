## Data Extraction from PDFs using Python

This project involved extracting data from multiple PDF files and converting them to CSV files for easier use and manipulation. Using a combination of these 3 custom algorithms, data was extracted from 11 different PDF files.

The PDFs were first converted into text files using XpdfReader. XpdfReader (https://www.xpdfreader.com/) has multiple applications that can be accessed through the command prompt. The text files were then converted into CSV files using OpenRefine. Since all the datasets were rather small (400-500 rows), empty rows could be checked for manually, and flagged for removal using OpenRefine.

Once converted into CSV format, the data did not contain any empty/header rows. Although our text file had the data organized into columns, when exported by OpenRefine, each row of data was compressed into a single column. Furthermore, the data was not present on a single line either - in many cases, the data for each observation (or individual) was stored on 2 rows, or even 4 rows.

To extract data from the raw CSV file, I used the pandas and numpy modules in Python 3. I had to create 3 different algorithms based on the structure of the PDF file.