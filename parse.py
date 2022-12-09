import bs4
import json
import re


def get_comments(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup.find_all(class_="_292iotee39Lmt0MkQZ2hPV")

DATA = {
    1: "age",
    2: "education",
    3: "xp",
    4: "function",
    5: "salary_before_tax",
    6: "salary_after_tax",
    7: "extralegal",
    8: "location",
    9: "industry",
    10: "happy",
}


def parse_comment(raw):
    data = {}
    ps = raw.find_all("p")
    pcount = 1
    for p in ps:
        meaningful_children = 0
        for c in p.children:
            if c.text == "" or c.text.isspace():
                next
            else:
                meaningful_children += 1
                if meaningful_children == 2 and pcount <= 10:
                    text = c.text
                    text = re.sub(r"\n", " ", text)
                    text = re.sub(r"\s+", " ", text)
                    text = re.sub(r"\u20ac", "", text)
                    data[DATA[pcount]] = text.strip()
        pcount += 1
    return data


def read_file():
    with open("test.html") as f:
        return f.read()


def check_data(data):
    stats = {
        "age": 0,
        "education": 0,
        "xp": 0,
        "function": 0,
        "salary_before_tax": 0,
        "salary_after_tax": 0,
        "extralegal": 0,
        "location": 0,
        "industry": 0,
        "happy": 0,
        "full": 0,
    }

    for d in data:
        if len(d) == 10:
            stats["full"] += 1
        for k in d.keys():
            stats[k] += 1

    return stats

def first_number(raw):
    all_numbers = re.findall(r'\d+(?:\.\d+)?', raw)
    return float(all_numbers[0]) if len(all_numbers) > 0 else None

def update_types(data):
    for d in data:
        age = re.sub(r'\D', '', d["age"])
        d["age"] = first_number(d["age"])
        d["xp"] = first_number(d["xp"])
        d["salary_before_tax"] = first_number(d["salary_before_tax"])

        if(d["salary_before_tax"] is not None and d["salary_before_tax"] < 10):
            d["salary_before_tax"] *= 1000
        d["salary_after_tax"] = first_number(d["salary_after_tax"])
        if(d["salary_after_tax"] is not None and d["salary_after_tax"] < 10):
            d["salary_after_tax"] *= 1000
    return data

contents = read_file()
comments = get_comments(contents)

all_data = []
for c in comments:
    data = parse_comment(c)
    all_data.append(data)

stats = check_data(all_data)

complete_records = [d.copy() for d in all_data if len(d) == 10]

typed_records = update_types(complete_records)

print(stats)
with open("data.json", "w") as f:
    json.dump(all_data, f)

with open("complete.json", "w") as f:
    json.dump(typed_records, f)
