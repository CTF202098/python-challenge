PyBank
1.	After adding my imports, I added the line of code “os.chdir(os.path.dirname(os.path.realpath(__file__)))” which was provided to the class by Kourt Bailey to make relative path compatibility possible
2.	I used Professor Booths “PyBank_test_BOOOOTH.py” and “PyBank_starter.BOOOOOTH.py” examples as general logic guides for this activity. Where his code is copied verbatim, I have notated as such as pseudo code in my own submission. 
3.	As I iterated my code, I encountered an error when I used a simple print command to test my work calculating net profit. The error was “ValueError: invalid literal for int() with base 10: 'a'”. In reviewing the Prof.’s examples, I realized that the issue came from me using “filepath” instead of “csvreader” in the initiation of my For-Loop. I corrected this based on the example given by Prof. 
4.	While calculating monthly profit changes, I tried to use “last_prof = int((row-1)[1])” to extract a value for the previous month’s profit, but this created an error. I saw in Prof. Booth’s example that this value had not been extracted after the beginning of this loop, so I used the same logic and copied that code block. 

PyPoll
1.	For this activity, my goal was to reuse, or follow the logic of, as much code from PyBank as possible. This worked for my imports, initializations, and outputs. I relied on example code given by Professor Booth for most of the functions of my code.
2.	I ran into trouble with creating a list of each candidate because the data was not sorted by candidate. To solve this, I followed the code logic shown in Professor Booth’s “PyPoll_starter_BOOOOOTh.py” example for the variable “vote_dict”. I used the variable “candidates” in my work. Since this logic was tied into the vote count logic, I used Prof.’s vote count logic too. 
3.	I also used Prof.’s example logic to create a list of results by candidate.
4.	The method I used to calculate a winner was not copied from Prof.’s example verbatim, but it does use the same code logic. I am not aware of simpler methods of determining a maximum in Python.
