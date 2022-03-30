from jinja2 import Template, Environment, FileSystemLoader

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)

pages = ('projetos', 'contato', 'index')

for page in pages:
    name = f'{page}.html'
    with open(name, 'w') as f:
        template = env.get_template(name)
        f.write(template.render())
file_loader = FileSystemLoader('articles')
env = Environment(loader=file_loader)
with open('article.html', 'w') as f:
    template = env.get_template('internet-nos-anos-2020-1.html')
    f.write(template.render())
