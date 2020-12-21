from csv import reader, writer, DictWriter
from functools import partial

left, right = {}, {}
with open('input.csv', 'r') as d:
    left, right = [dict(x) for x in zip(*[(t[:2], t[2:]) for t in reader(d)])]

output = {number: {'name': name, 'updated': False, 'added': False}
          for number, name in left.items()}
remains = {}

for number, name in right.items():
    output_record = output.get(number)
    if output_record is not None:
        if output_record.get('name') != name:
            output_record.update({'name': name, 'updated': True})
        else:
            continue
    else:
        output.update({number: {'name': name, 'updated': False, 'added': True}})
    remains.update({number: name})


file_rewriter = partial(open, mode='w', newline='')
with file_rewriter('output.csv') as output_file:
    dos_output = DictWriter(output_file, fieldnames=['number', 'name', 'updated', 'added'])
    dos_output.writeheader()
    dos_output.writerows({'number': k, **v} for k, v in output.items())

with file_rewriter('remains.csv') as remains_file:
    remains_output = writer(remains_file)
    remains_output.writerows(remains.items())
