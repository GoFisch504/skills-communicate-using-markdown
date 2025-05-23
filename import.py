import csv

# Path to your CSV file
csv_file = 'issues.csv'

issues = []

# Read and display the CSV contents
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print("CSV Contents:")
    for row in reader:
        print(row)
        # Process each row into an issue dictionary
        issue = {
            'title': row.get('Title', ''),
            'description': row.get('Description', ''),
            'labels': [label.strip() for label in row.get('Labels', '').split(',')] if row.get('Labels') else []
        }
        issues.append(issue)

print("\nProcessed Issue List:")
for i, issue in enumerate(issues, 1):
    print(f"Issue {i}:")
    print(f"  Title: {issue['title']}")
    print(f"  Description: {issue['description']}")
    print(f"  Labels: {issue['labels']}\n")
