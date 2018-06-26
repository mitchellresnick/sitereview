# sitereview
Bulk Symantec Site Review Checker (CLI) for use within an environment with SSL decryption issues. 

### Description

Site Review described by Symantec:

*"Site Review allows users to check and dispute the current WebPulse categorization for any URL"*

https://sitereview.bluecoat.com/

This Python script focuses on the first portion, allowing Users to quickly query the Site Review service via the CLI. This script can be run stand-alone, or imported as a module to extend the functionality of another script.

### Usage

Place a text file named `url.txt` into the same directory as the `sitereview.py` file. This text file should contain the URLs to check, one per line.

### Results

Sample results, for a known-malicious domain:

```
http://www.google.com/ , Search Engines/Portals
```
### Installation

```
python setup.py install
```

### Python Requirements

* argparse
* bs4
* json
* requests
* sys
* lxml

