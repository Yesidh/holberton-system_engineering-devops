<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# :colombia: Bash - Loops, condition and parsing                                
- How to create SSH keys
- What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
- How to use while, until and for loops
- How to use if, else, elif and case condition statements
- How to use the cut command
- What are files and other comparison operators, and how to use them
## Examples                                                                     
Write a Bash script that displays numbers from 1 to 100.
                                                                                
Requirements:                                                                   
                                                                                
- Displays FizzBuzz when the number is a multiple of 3 and 5                    
- Displays Fizz when the number is multiple of 3                                
- Displays Buzz when the number is a multiple of 5                              
- Otherwise, displays the number                                                
- In a list format                                                              
the output:                                                                     
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```
for more information see the task 10
## Prerequisites
Reading about: Loops sample, variable assignment and arithmetic, comparision operators,
 file test operators and make your scrips portable.                             
## Installing

for have the code in your local machine you only need download the code files and put it into a directory.
## Built With

All the code was write under ubuntu 14.04 and the Shellcheck                    


## Contributing

-- Yesid Gutierrez - Holberton Student                                          

## Versioning
for my learning in Holberton School

## Authors

---Yesid Gutierrez  944@holbertonshcool.com                                    
                                                                               
## Files

|             File               |             Description                  |
|--------------------------------| ---------------------------------------- |
|**0-RSA_puclic_key.pub**| ssh-keygen RSA|
|**1-for_holberton_school**| Bash script that display 10 times Holberton School using for loop|
|**2-while_holberton_school**| Bash script that display Holberton School 10 times using while loop|
|**3-until_holberton_shcool**| Bash script that display Holberton School 10 times using until loop|
|**4-if_9_say_hi**| Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line|
|**5-4_bad_luck_8_is_your_change**| Bash script that loops from 1 to 10 and display bad luck for the 4th iteration, good luck for the 8th iteration adn Holberton School for the other iterations. using while loop and if, elif and else statements|
|**6-superstitious_numbers**| Bash script that displays numbers from 1 to 20 and: display 4 and then bad luck form China for the 4th loop iteration, displays 9 and then bad luck from Japan for the 9th loop iteration, displays 17 and then bad luck from Italy for the 17th loop iteration|
|**7-clock**| Bash script that displays the time for 12 hours and 59 minutes: display hours from 0 to 12 and displays minutes from 1 to 59. using while loop|
|**8-for_ls**| Bash script that displays: the content of the current directory ina list format, where only the part of the name after the first dash is displayed. using for loop|
|**9-to_file_or_not_to_file**| Bash script that gives you information about the holbertonschool file: use if and else; if the file exist print: holbertonschool file exists, if does exists print: holbertonschool file does not not exist. If the file exists print: if is empty: holbertonschool file is empty. if not empty: holbertonschool file is not empty. if is a regular file: holbertonschool is a regular file|
|**10-fizzbuzz**| Bash script that displays numbers from 1 to 100: display FizzBuzz when the number is a multiple of 3 and 5; Fizz when the number is multiple of 3 and Buzz when the number is a multiple of 5, otherside display the number|
|**100-read_and_cut**| Bash script that displays the content of the file /etc/passwd and only display: username, user id and home directory path for the user|