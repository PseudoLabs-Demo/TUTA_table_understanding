from bs4 import BeautifulSoup
from argparse import ArgumentParser



parser = ArgumentParser()
parser.add_argument("in_file")
parser.add_argument("out_file")

args = parser.parse_args()
soup = BeautifulSoup(open(args.in_file).read(), "html.parser")
trs = soup.find_all("tr")
tdss = [ tr.find_all("td") for tr in trs ]
width = max( sum( int(td.get("colspan", 1)) for td in tds ) for tds in tdss )
height = len(trs)

new_table = [ [None]*width for i in range(height) ]

for row, tds in enumerate(tdss):
    col = 0

    for td in tds:
        col += new_table[row][col:].index(None)
        cspan = int(td.get("colspan", 1))
        rspan = int(td.get("rowspan", 1))
        inner = td.text.replace("\n", "")

        for i in range(rspan):
            for j in range(cspan):
                new_table[row+i][col+j] = inner

table_tag = soup.find("tbody")
table_tag.clear()

for row in new_table:
    tr = soup.new_tag("tr")
    
    for inner in row:
        td = soup.new_tag("td")
        td.string = inner

        tr.append(td)

    table_tag.append(tr)

open(args.out_file, "w").write(soup.prettify())
