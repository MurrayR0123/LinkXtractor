# LinkXtractor
Built to complement other web enumeration tools to help in identifying possible hidden services linked in web content.
Accepts a text file containing target urls, outputs any urls discovered in the content.

Usage: link-extract.py [-h] <file_of_target_urls>

1. Scan a given input file for urls (Allows you to input the output from other enumeration tools such as dirbuster/gobuster/feroxbuster etc)
2. Retrieves web content from the list of urls
3. Scans web content for the presence of urls

Please only use this tool against systems you have permission to access.
