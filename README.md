# arXiv Downloader

A simple tool to download papers from [arxiv.org](https://arxiv.org/) via CLI.

---
## Information

**Status**: `Occasionally maintained`

**Type**: `Personal project`

**Development year(s)**: `2018+`

**Authors**: [ShadowTemplate](https://github.com/ShadowTemplate)

**Notes**: *This tool parses arXiv source code and may thus suddenly break if
changes are performed on its front end.*

---
## Getting Started

The script is ready to be used and no configuration is required.
An arXiv paper can be downloaded by its URL (typically 
_https://arxiv.org/abs/PAPER_ID_), e.g.:

```
python arxiv.py https://arxiv.org/abs/1709.07020
```

The output should be a nicely formatted PDF with title "*2017 - The arXiv of 
the future will not look like the arXiv - l. Pepe, M. Cantiello, J. 
Nicholson.pdf*".

### Prerequisites

Clone the repository with:

```
git clone https://github.com/ShadowTemplate/arxiv-downloader.git
```

Move to the new project folder:

```
cd arxiv-downloader
```

Install the required Python dependencies via pip: 

```
pip install -r requirements.txt
```

---
## Building tools

* [Python 3.6](https://www.python.org/downloads/release/python-360/) - Programming language
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - 
Web page scraping

---
## Contributing

Any contribution is welcome. Feel free to open issues or submit pull requests.

---
## License

This project is licensed under the  GNU GPLv3 license.
Please refer to the [LICENSE.md](LICENSE.md) file for details.

---
*This README.md complies with [this project template](https://github.com/ShadowTemplate/project-template). Feel free to adopt it
and reuse it.*
