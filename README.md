# sitereview
Bulk Symantec Site Review Checker (CLI) for use within an environment with SSL decryption issues. 

## Description

Site Review described by Symantec:

*"Site Review allows users to check and dispute the current WebPulse categorization for any URL"*

https://sitereview.bluecoat.com/

This Python script focuses on the first portion, allowing Users to quickly query the Site Review service via the CLI. This script can be run stand-alone, or imported as a module to extend the functionality of another script.

## Usage

Place a text file named `url.txt` into the same directory as the `sitereview.py` file. This text file should contain the URLs to check, one per line. The program will output a file named `output.txt` with the applicable categories. Please note that the program will **append** resluts to the file, so it there is an existing `output.txt` file, it will be added to.

One you have the files ready, execute the program using: 
```
python sitereview.py
```

## Results

The resutls will be shown both in the console during execution and output to a file named `output.txt`.

## Installation

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

