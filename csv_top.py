
import csv
def get_top_rows(path, column, n):
    with open (path) as f:
        reader = csv.DictReader(f)
        rows = sorted(reader, key=lambda x: int(x[column]), reverse=True)
    return rows[:n]

if __name__ == "__main__":
    top_rows = get_top_rows("products.csv", "score", 3)
    for row in top_rows:
        print(f"{row['name']}: {row['score']}")

