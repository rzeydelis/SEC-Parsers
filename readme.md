## SEC Parsers
![PyPI - Downloads](https://img.shields.io/pypi/dm/sec-parsers)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fhttps%2F%2Fgithub.com%2Fjohn-friedman%2FSEC-Parsers&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
![GitHub](https://img.shields.io/github/stars/john-friedman/sec-parsers)

Parses non-standardized SEC filings into structured xml. Use cases include LLMs, NLP, and textual analysis. Package is a WIP.

Supported filing types are 10-K, 10-Q, 8-K. More will be added soon.

<div align="center">
  <img src="https://raw.githubusercontent.com/john-friedman/SEC-Parsers/main/Assets/tesla_visualizationv3.png">
</div>
<div align="center">
  <img src="https://raw.githubusercontent.com/john-friedman/SEC-Parsers/main/Assets/tesla_tree_v3.png" width="500">
</div>

Installation
```
pip install sec-parsers
```

Quickstart
```
from sec_parsers import Filing, download_sec_filing

html = download_sec_filing('https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/tsla-20231231.htm')
filing = Filing(html)
filing.parse() # parses filing
filing.visualize() # opens filing in webbrowser with highlighted section headers
filing.find_nodes_by_title(title) # finds node by title, e.g. 'item 1a'
filing.find_nodes_by_text(text) # finds nodes which contains your text
filing.get_tree(node) # if no argument specified returns xml tree, if node specified, returns that nodes tree
filing.get_title_tree() # returns xml tree using titles instead of tags. More descriptive than get_tree.
filing.save_xml(file_name)
filing.save_csv(file_name)
```
### Additional Resources:
* [quickstart](Examples/quickstart.ipynb)
* medium article to define custom parsers
* [Archive of Parsed XMLs / CSVs](https://www.dropbox.com/scl/fo/np1lpow7r3bissz80ze3o/AKGM8skBrUfEGlSweofAUDU?rlkey=cz1r78jofntjeq4ax2vb2yd0u&e=1&st=mdcwgfcm&dl=0) - Last updated 7/10/24.
* [example parsed filing](Examples/tesla_10k.xml)
* [example parsed filing exported to csv](Examples/tesla_10k.csv).

### Feature Requests:
To request features or suggest a way to improve the package please use the form below.
[Google Form](https://forms.gle/cCh7VT93v4tV4ekp8)
* Extract title of section along with its text (sharif)
* Extract subsections from section (sharif)
* Export to dta (Denis)
* option to remove special chars from document in export (bill)

### Statistics
* Speed: On average, 10-K filings parse in 0.25 seconds. There were 7,118 10-K annual reports filed in 2023, so to parse all 10-Ks from 2023 should take about half an hour.

### Updates
#### Towards Version 1:
* Most/All SEC text filings supported
* Few errrors
* xml 

Might be done along the way:
* Faster parsing, probably using streaming approach, and combining modules together.
* Introduction section parsing
* Signatures section parsing

#### Beyond Version 1:
To improve the package beyond V1 it looks like I need compute and storage. Not sure how to get that. Working on it.

Metadata
* Clustering similar section titles using ML (e.g. seasonality headers)
* Adding tags to individual sections using small LLMs (e.g. tag for mentions supply chains, energy, etc)

Other
* Table parsing
* Image OCR
* Parsing non-html filings

### Current Priority list:
* Add S-1 filing
* fix all caps and emphasis issue
* clean text
* Better historical conversion: handle if PART I appears multiple times as header, e.g. logic here item 1 continued.


