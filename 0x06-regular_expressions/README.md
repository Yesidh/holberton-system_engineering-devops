<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# :colombia: DevOps -Regular Expression                                         
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.
## Examples                                                                     
scrip that prints from:,to:,flags: from a logfile with data about VoIP
```
- Data input:
 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'

- Data output:
12392190384,19148265919,-1:0:-1:-1:-1
```
for more information see the task: 100-textme.rb                                
## Prerequisites
Making a lot of exercices in https://regexone.com/problem                                           
## Installing

for have the code in your local machine you only need download the code files and put it into a directory.
## Built With

All the code was write under ubuntu 14.04 and ruby                              


## Contributing

-- Yesid Gutierrez - Holberton Student                                          

## Versioning
for my learning in Holberton School

## Authors

---Yesid Gutierrez  944@holbertonshcool.com                                    
                                                                               
## Files

|             File               |             Description                  |
|--------------------------------| ---------------------------------------- |
|**0-simply_match_holberton.rb**| The regular expression must match Holberton|
|**1-repetition_token_0.rb**| Find the regular expression that will match the cases: hbttn, hbtttn, hbttttn and hbtttttn|
|**2-repetition_token_1.rb**| Find the regular expression that will match the cases: htn and hbtn|
|**3-repetition_token_2.rb**| Find the regular expression that will match the cases: hbtn, hbttn, hbtttn and hbttttn|
|**4-retetition_token_3.rb**| Find the regular expression that will match the cases: hbn, hbtn, hbttn, hbtttn and hbttttn|
|**5-beginning_and_end.rb**| The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between|
|**6-phone_number.rb**| The regular expression must match a 10 digit phone number|
|**7-OMG_WHY_ARE_YOU_SHOUTING.rb**| The regular expression must be only matching: capital letters|
|**100-textme.rb**| output of the scrip will print: [SENDER],[RECEIVER],[FLAGS] from a log file about VoIP|
|**101-passed_linkedin_regex_challenge.jpg**| solution about LinkedIn regex puzzle: https://engineering.linkedin.com/puzzle|