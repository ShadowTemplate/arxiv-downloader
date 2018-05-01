from bs4 import BeautifulSoup

import re
import time
import traceback
import urllib.request


def find_year(soup):
    try:
        submissions = soup.body.find("div", attrs={"class": "submission-history"})
        print("%s" % submissions.text)
        for line in submissions.text.split("\n"):
            if line.startswith("[v1]"):
                print("First submission: %s" % line)
                # remove content between () and [] and strip whitespaces
                date = re.sub("[\(\[].*?[\)\]]", "", line).strip()
                print("Date: %s" % date)
                parsed_date = time.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
                year = time.strftime("%Y", parsed_date)
                print("Year: %s" % year)
                return year
    except Exception:
        print(traceback.format_exc())
        print("Unable to parse date. Stopping.")
        exit(-1)

    print("Unable to find first submission. Stopping.")
    exit(-1)


def find_title(soup):
    try:
        title = soup.body.find("h1", attrs={"class": "title mathjax"})
        parsed_title = title.text.lstrip("Title:").lstrip("\n")
        print("Title: %s" % parsed_title)
        return parsed_title
    except Exception:
        print(traceback.format_exc())
        print("Unable to parse title. Stopping.")
        exit(-1)


def find_authors(soup):
    try:
        authors = soup.body.find("div", attrs={"class": "authors"})
        parsed_authors = authors.text.lstrip("Authors:\n").replace("\n", "")
        print("Authors: %s" % parsed_authors)
        authors = parsed_authors.split(", ")
        formatted_authors = []
        for a in authors:
            tokens = a.split(" ")
            for i in range(len(tokens) - 1):
                if len(tokens[i]) > 2:
                    tokens[i] = tokens[i][0] + "."
            formatted_authors.append(" ".join(tokens))
        return ", ".join(formatted_authors)
    except Exception:
        print(traceback.format_exc())
        print("Unable to parse authors. Stopping.")
        exit(-1)


def main(url):
    print("Processing URL %s..." % url)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "lxml")

    year = find_year(soup)
    title = find_title(soup)
    authors = find_authors(soup)

    file_name = "{} - {} - {}.pdf".format(year, title, authors)
    print(file_name)
    print("Downloading pdf...")
    try:
        download_url = url.replace("/abs/", "/pdf/")
        urllib.request.urlretrieve(download_url, file_name)
        print("Download completed.")
    except Exception:
        print(traceback.format_exc())
        print("Unable to download pdf. Stopping.")
        exit(-1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="A simple tool to download arXiv papers via CLI.")
    parser.add_argument("-p", "--paper", type=str, required=True,
                        help="Link to arXiv paper")
    args = parser.parse_args()
    main(args.paper)
