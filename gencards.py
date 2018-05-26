import csv, os
import pdfkit
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

colnums = {
    'number': 0,
    'module': 1,
    'desc': 2,
    'estimate': 5,
    'priority': 6
}

stories = []

with open('print.csv') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        stories.append({
            'number': row[colnums['number']],
            'module': row[colnums['module']],
            'desc': row[colnums['desc']],
            'estimate': row[colnums['estimate']],
            'priority': row[colnums['priority']]
        })

template = env.get_template('story-template.html')
options = {
    'page-size': 'A4',
    'margin-top': '3mm',
    'encoding': "UTF-8",
    'no-outline': None,
    'quiet': ''
}

for story in stories:
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    outputfile = output_dir + '/' + story['number'] + '.html'
    with open(outputfile, 'w') as output:
        output.write(template.render(story))
    print("Converting html file {} to pdf...".format(outputfile))
    pdfkit.from_file(outputfile, output_dir + '/' + story['number'] + '.pdf', options=options)
