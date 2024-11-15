import csv

def save_to_csv(quotes, filename):
    """
    Saves a list of quotes to a CSV file.

    Args:
        quotes (list): The list of quotes to save.
        filename (str): The name of the CSV file.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote"])  # Header row
        for quote in quotes:
            writer.writerow([quote])
