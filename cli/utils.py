# cli/utils.py
import os
import re
import boto3

def generate_slug(text):
    return re.sub(r'[_ ]+', '-', text.lower())

def write_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def upload_to_s3(file_path, content, bucket):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=os.path.basename(file_path), Body=content)

def find_post_by_slug(slug):
    for filename in os.listdir('content'):
        if slug in filename:
            return os.path.join('content', filename), read_file(os.path.join('content', filename))
    return None, None

def update_frontmatter_field(file_path, key, value):
    content = read_file(file_path)
    split_content = content.split('---', 2)
    frontmatter = yaml.load(split_content[1], Loader=yaml.FullLoader)
    frontmatter[key] = value
    updated_content = f"---\n{yaml.dump(frontmatter)}---{split_content[2]}"
    write_file(file_path, updated_content)
