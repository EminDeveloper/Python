import csv

# Load sample data (a restaurant menu of items)
with open('menu_items.csv') as file:
    lines = csv.reader(file)

    # Store the name of the menu items in this array. In Chroma, a "document" is a string i.e. name, sentence, paragraph, etc.
    documents = []

    # Store the corresponding menu item IDs in this array.
    metadatas = []

    # Each "document" needs a unique ID. This is like the primary key of a relational database. We'll start at 1 and increment from there.
    ids = []
    id = 1

    # Loop thru each line and populate the 3 arrays.
    for i, line in enumerate(lines):
        if i==0:
            # Skip the first row (the column headers)
            continue

        documents.append(line[1])
        metadatas.append({"item_id": line[0]})
        ids.append(str(id))
        id+=1