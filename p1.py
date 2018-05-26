from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('story-template.html')
context = {
    'desc': 'asdflkjasd f',
    'number': '#221',
    'module': '资源',
    'estimate': 3,
    'priority': 'H',
    'title': 'asdf'
}
print(template.render(context))
