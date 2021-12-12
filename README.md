# glowing-engine

This repository contains all the data analysis and data collection projects that I have worked on.

## Data Extraction from PDFs using Python

This project involved extracting data from multiple PDF files and converting them to CSV files for easier use and manipulation. Using a combination of these 3 custom algorithms, data was extracted from 11 different PDF files.

The PDFs were first converted into text files using XpdfReader. XpdfReader (https://www.xpdfreader.com/) has multiple applications that can be accessed through the command prompt. The text files were then converted into CSV files using OpenRefine. Since all the datasets were rather small (400-500 rows), empty rows could be checked for manually, and flagged for removal using OpenRefine.

Once converted into CSV format, the data did not contain any empty/header rows. Although our text file had the data organized into columns, when exported by OpenRefine, each row of data was compressed into a single column. Furthermore, the data was not present on a single line either - in many cases, the data for each observation (or individual) was stored on 2 rows, or even 4 rows.

To extract data from the raw CSV file, I used the pandas and numpy modules in Python 3. I had to create 3 different algorithms based on the structure of the PDF file.

## The Spread of COVID-19 in India

This project focused on analysing trends present in COVID-19 data sourced from worldometer. An initial analysis was performed on data from all around the world by comparing the trend of cases and deaths in the top 5 countries with the most number of cases. The report then focuses on the transmission within India, and aims to answer two questions -

1. What are the factors that led to Maharashtra developing such a high number of cases?
2. Which state has the highest death rate, and why?

All analyses were performed using the pandas and matplotlib modules in Python 3.

## Analysis of student data

In this report, we examine the data obtained from an online survey conducted for students enrolled in the Data Analytics unit (DATA2x02) students in Semester 2, 2021 at The University of Sydney. The survey was conducted via the online discussion forum Ed and was open to all students enrolled in the Data Analytics unit, both mainstream and advanced (DATA2002 and DATA2902). The survey consisted of 23 questions in total.

The report aims to answer four questions - 

* Does the number of COVID tests a student has taken in the past two months follow a Poisson distribution?
* Do students in the advanced unit (DATA2902) experience higher levels of stress than students in the mainstream unit (DATA2002)?
* How do living arrangements affect the levels of loneliness that students experience?
* Do students who find the unit easier have a higher self-rated math/coding ability?
