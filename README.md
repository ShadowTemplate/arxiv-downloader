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

Clone the repository with:

```
git clone https://github.com/ShadowTemplate/arxiv-downloader.git
```

Move to the new project folder:

```
cd arxiv-downloader

```


### Prerequisites

Install the required Python dependencies via pip: 

```
pip install -r requirements.txt
```

### Installing

Download an arXiv paper by its URL (typically _https://arxiv.org/abs/PAPER_ID_)
with: 

```
python3 arxiv.py https://arxiv.org/abs/PAPER_ID
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
