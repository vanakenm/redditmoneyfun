# Reddit.be salaries

This is an attempt at extracting data from the Reddit.be [salary thread of 2022](https://www.reddit.com/r/belgium/comments/ze9fqk/whats_your_salary_2022_edition/).

Usual disclaimer: nothing scientific here, if you use this for something else than having fun, you are insane.

## Process

### Parsing

I've taken the whole HTML from the page, save it locally, try to get comments info using BeautifulSoup

### Converting to data

I'm hoping that people follow exactly the structure presented (top secret: they don't), so I get the various lines after each title

### Cleaning

After I try to make numbers out of things that should be numbers. Thanks to people being "23, 24 soon" or other earning 2K€, this was not that easy.

### Filtering

I only keep records that have all data asked - around 100 for now

### Analysis

Finally - let's do a small notebook with nice charts.
