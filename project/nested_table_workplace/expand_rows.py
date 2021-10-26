import os
from bs4 import BeautifulSoup, Tag


with open("output.html", "w") as out:
    with open("debug.html", "w") as wf:
        with open("test_table_cp.html") as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')

            results = soup.find_all("td")
            wf.write(soup.prettify())
            for r in results:
                if 'colspan' in r.attrs:
                    count = int(r.attrs.get('colspan', 0))
                    # r.attrs = {}
                    # Make a new string (as a precursor to the beautiful soup object)to replace the colspan attribute.
                    expanded_string = []
                    for i in range(count):
                        expanded_string.append(str(r))

                    expanded_string = "\n".join(expanded_string)
                    soup_string = BeautifulSoup(expanded_string, 'html.parser')
                    r.replaceWith(soup_string)
            out.write(soup.prettify())

            # wf.write(r.text)
            # wf.write(str(r.attrs))

            # attrs = r.attrs
            # # Todo Figure out how to deal with rowspan. Boiler plate code written, just how to place the <td> is remaining.
            # if any(key in attrs for key in ['colspan']):
            #     key_list = attrs.keys()
            #     wf.write('\t spanning element present')
            #     wf.write('\t keys {x}'.format(x=key_list))
            #     wf.write('\t text: {x}'.format(x=r.text))

            #     for key in key_list:
            #         count = int(attrs.get(key, 0))
            #         r.attrs = {}  # Get rid of the colspan
            #         for i in range(count):
            #             out.write(str(r))
            #             out.write('\n')

            # wf.write('\n')
