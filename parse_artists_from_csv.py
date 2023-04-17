import os
import csv
artists = set()
for i in os.listdir('res/'):
    with open(f'res/{i}', newline='', encoding='utf-8') as csvfile:
        c = csv.reader(csvfile)
        for r in c:
            print(r[0])
            if not r[0].startswith('['):
                artists.add(r[0])
print(len(artists))

with open('artists_v2', 'w', encoding='utf-8') as out:
    out.write('\n'.join(artists))