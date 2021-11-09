import os
from collections import deque
from typing import Counter
from bs4 import BeautifulSoup, Tag

with open("test_output.html", "w") as test_out:
    with open("output.html", "w") as out:
        with open("debug.html", "w") as wf:
            with open("test_table_cp.html") as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')

                results = soup.find_all("td")
                rows = soup.find_all("tr")

                wf.write(str(rows))

                rows_queue = []
                # This is the position of all the tags (position meaning first column, second column etc).
                rows_queue_posts = []
                out.write(str(rows))
                for row in rows:
                    """
                        Position-wise insertion
                    """

                    if len(rows_queue) != 0:
                        # row_to_insert = rows_queue.popleft()
                        elements_to_insert = []

                        current_column = 0
                        # This to tell soup where to insert each row
                        index_insertion = deque()
                        column_to_search_to = max(rows_queue_posts)

                        while current_column <= column_to_search_to:
                            # Gone through all the columns required for insertion
                            try:
                                col_index = rows_queue_posts.index(
                                    current_column)
                                elements_to_insert.append(
                                    rows_queue[col_index])

                                # Remove the element that you inserted from the queues
                                index_insertion.append(
                                    rows_queue_posts.pop(col_index))
                                rows_queue.pop(col_index)
                            except Exception as e:
                                print(e)

                            current_column += 1

                        for each_ele in elements_to_insert:
                            each_ele.attr = {}
                            soup_string = BeautifulSoup(
                                str(each_ele), "html.parser")
                            row.insert(index_insertion.popleft(), soup_string)

                    # This indicates the position of the element
                    element_post = 0

                    for element in row:
                        # If multiple elements need to be expanded in the same row, then this will store each instance of them together
                        elements_to_expand = []
                        local_store = []
                        if (isinstance(element, Tag)):
                            # print("this is an element {x}".format(x=element))
                            if 'colspan' in element.attrs:
                                col_count = int(
                                    element.attrs.get('colspan', 0))
                                element.attrs = {}
                                # Make a new string (as a precursor to the beautiful soup object)to replace the colspan attribute.
                                expanded_string = []
                                for i in range(col_count):
                                    expanded_string.append(str(element))

                                expanded_string = "\n".join(expanded_string)
                                soup_string = BeautifulSoup(
                                    expanded_string, 'html.parser')
                                element.replaceWith(soup_string)

                            if 'rowspan' in element.attrs:
                                row_count = int(
                                    element.attrs.get('rowspan', 0))
                                ATTRS = element.attrs
                                ELEMENT = str(element)
                                element.attrs = {}
                                STRING_R = str(element)

                                if len(element.find_all()) != 0:
                                    inner_elements = element.find_all()
                                    combined_text = []
                                    tag_class = inner_elements[0].name

                                    table_data_soup = BeautifulSoup(
                                        "<td></td>", features="html.parser")
                                    table_data_tag = table_data_soup.td
                                    insert_soup = soup.new_tag(tag_class)

                                    for ele in inner_elements:
                                        combined_text.append(ele.text)

                                    combined_text = "".join(combined_text)
                                    insert_soup.append(combined_text)
                                    table_data_tag.append(insert_soup)
                                    modified_element = table_data_tag
                                else:
                                    # No change
                                    modified_element = element

                                print(element, modified_element)
                                # Insert the cleaned element back into the row.
                                soup_string = BeautifulSoup(
                                    str(modified_element), 'html.parser')
                                element.replaceWith(soup_string)

                                # As one is already done for us
                                for i in range(row_count - 1):
                                    # Store the element along with the position it is to be placed
                                    rows_queue.append(modified_element)
                                    rows_queue_posts.append(element_post)

                            element_post += 1

                    # Add expanded row elements

                test_out.write(soup.prettify())
