# cli/manager.py
import os
import yaml
import datetime
from utils import generate_slug, write_file, read_file, upload_to_s3

def create_post(title, slug, category):
    slug = generate_slug(slug)
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"{date}-{slug}.md"
    frontmatter = {
        'title': title,
        'date': date,
        'tags': [],
        'category': category,
        'published': False
    }
    content = f"---\n{yaml.dump(frontmatter)}---\n\n# {title}\nWrite your content here..."
    write_file(os.path.join('content', filename), content)

def publish_post(slug):
    slug = generate_slug(slug)
    file_path, content = find_post_by_slug(slug)
    upload_to_s3(file_path, content, 'blog-posts')
    upload_media_for_post(content)

def search_posts(query):
    for filename in os.listdir('content'):
        content = read_file(os.path.join('content', filename))
        if query.lower() in content.lower():
            print(filename)

def update_post_tags(slug, tags):
    slug = generate_slug(slug)
    file_path, content = find_post_by_slug(slug)
    update_frontmatter_field(file_path, 'tags', tags.split(','))

def update_post_category(slug, category):
    slug = generate_slug(slug)
    file_path, content = find_post_by_slug(slug)
    update_frontmatter_field(file_path, 'category', category)

def upload_media(file_path):
    upload_to_s3(file_path, read_file(file_path), 'blog-media')

def update_frontmatter(slug, frontmatter_updates):
    slug = generate_slug(slug)
    file_path, content = find_post_by_slug(slug)
    frontmatter_dict = yaml.load(frontmatter_updates)
    for key, value in frontmatter_dict.items():
        update_frontmatter_field(file_path, key, value)

def manage_revisions(slug):
    # Implementation of revision management logic here.
    pass
