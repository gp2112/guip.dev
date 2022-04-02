from jinja2 import Template, Environment, FileSystemLoader
from bs4 import BeautifulSoup
import os


domain = 'guip.dev'
file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)


# render static pages
pages = ('projetos', 'contato', 'index', 'license')

for page in pages:
    name = f'{page}.html'
    with open(f'{domain}/{name}', 'w') as f:
        template = env.get_template(name)
        f.write(template.render())

file_loader = FileSystemLoader('articles')
env = Environment(loader=file_loader)

# render blog articles
articles = os.listdir('./articles')
articles.remove('base.html')
for article_file in articles:
    with open(f'./{domain}/blog/'+article_file, 'w') as f:
        template = env.get_template(article_file)
        f.write(template.render())

# render blog page

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)
articles_data = []
for article_file in articles:
    with open(f'./{domain}/blog/{article_file}') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('title').get_text()
    preview = soup.find('p').get_text()[:200]+'...'
    thumb = soup.find('img', class_='graf-image').attrs['src']
    articles_data.append({
                'title':title,
                'preview':preview,
                'url':article_file,
                'thumb':thumb
            })
with open(f'{domain}/blog.html', 'w') as f:
    template = env.get_template('blog.html')
    f.write(template.render(articles=articles_data))
