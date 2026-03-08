# Orkut Excavator
This script allows users to search for terms inside the Orkut archives on the Wayback Machine, since the death of the social network huge amounts of content have been lost and hard to find, that this script may help some find what they're looking for. Support The Internet Archive.

## Setup
1. Clone the repository  
`git clone https://github.com/hlvini/orkut-navigator.git`
2. Inside, create a Python virtual environment (through conda or venv)  
`python3 -m venv venv`  
4. Activate it  
`source venv/bin/activate`  
3. Install requirements.txt  
`pip install -r requirements.txt`

## Usage
Invoke the script by calling it then specify the arguments  
`python3 orkut-crawler.py --index [0, A-Z] --word [...]`

`--index`  
The archive is divided alphabetically, from numbers and special characters (represented by 0), from A to Z. 

`--word`  
Searches for the specified whole word through the archives, not case-sensitive

## LIMITATIONS  
Beware that this script may cause temporary request blocking by the Internet Archive, also, this script can be extremely slow at times due to Wayback Machine general slowness
