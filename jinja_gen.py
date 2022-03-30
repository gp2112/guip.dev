from jinja2 import Template, Environment, FileSystemLoader
from bs4 import BeautifulSoup
import os

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)


# render static pages
pages = ('projetos', 'contato', 'index')

for page in pages:
    name = f'{page}.html'
    with open(name, 'w') as f:
        template = env.get_template(name)
        f.write(template.render())

file_loader = FileSystemLoader('articles')
env = Environment(loader=file_loader)

# render blog articles
articles = os.listdir('./articles')
for article_file in articles:
    with open('./blog/'+article_file, 'w') as f:
        template = env.get_template(article_file)
        f.write(template.render())

# render blog page

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)
articles_data = []
for article_file in articles:
    with open(f'./blog/{article_file}') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('title').get_text()
    preview = soup.find('p').get_text()[:100]+'...'
    articles_data.append({
                'title':title,
                'preview':preview,
                'url':article_file
            })
with open('blog.html', 'w') as f:
    template = env.get_template('blog.html')
    f.write(template.render(articles=articles_data))

