import csv

# Imports a file and presents it as a table.
# If the table has another table as their only argument, it returns the inner table.
# The function returns [] is unsuccessful.
def import_data(csv_file):

    try:
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            table = [[e for e in r] for r in reader]
        return table
    except FileNotFoundError:
        print("ERROR: The program called a file that did not exist: {} does not appear to exist.".format(csv_file))
        return []

# Writes a table to a given file, effectively overwriting its previous contents.
# Returns true if successful, false if unsuccessful.
def save(table,csv_file):

    # write it
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        [writer.writerow(r) for r in table]
    return True