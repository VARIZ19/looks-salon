import json
import sys

with open('extracted_menu_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('all_pages_dump.txt', 'w', encoding='utf-8') as out:
    for p in data:
        out.write(f"==================== PAGE {p['page']} ====================\n")
        out.write(p['text'].strip() + "\n\n")

print("Dumped all pages to all_pages_dump.txt")
