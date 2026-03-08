# Orkut Excavator
A Python tool designed to search archived Orkut pages stored in the Wayback Machine. The vast amount of user-generated content has become difficult to find and recover since the 2014 shutdown of Orkut. This tool is made with the intended to help researchers, OSINT enthusiasts and nostalgic users in recovering fragments of that lost data. Support the Internet Archive.

## Setup
1. Clone the repository  
`git clone https://github.com/hlvini/orkut-excavator.git`
2. Inside, create a Python virtual environment (through conda or venv)  
`python3 -m venv venv`  
3. Activate it  
`source venv/bin/activate`  
4. Install requirements.txt  
`pip install -r requirements.txt`

## Usage
Invoke the script by calling it then specify the arguments  
`python3 orkut-crawler.py --index [0, A-Z] --term [...]`

`--index`  
The archive is divided alphabetically, from numbers and special characters (represented by 0), from A to Z. 

`--term`  
Searches for the specified whole word through the archives, not case-sensitive

## Example 
```
$ python3 orkut-crawler.py --index a --term amigos
SCANNED: https://web.archive.org/web/20170508140728/https://orkut.google.com/l-a.html
FOUND [amigos] IN -> https://web.archive.org/web/20170508140728/https://orkut.google.com/l-a.html
```
## LIMITATIONS  
Beware that this script may cause temporary request blocking by the Internet Archive, also, this script can be extremely slow at times due to Wayback Machine general slowness
