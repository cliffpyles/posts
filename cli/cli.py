#!/usr/bin/env python3
# cli/cli.py
import click
from .manager import create_post, publish_post, search_posts, update_post_tags, update_post_category, upload_media, update_frontmatter, manage_revisions

@click.group()
def cli():
    """
    A CLI tool to manage blog content written in Markdown.
    Allows creation, publishing, tagging, categorizing, and searching of blog posts, 
    as well as uploading and managing associated media files.
    """
    pass

@click.command()
@click.option('--title', required=True, help="Title of the post")
@click.option('--slug', required=True, help="URL-friendly identifier of the post, created from the title or main keyword")
@click.option('--category', required=True, help="Category under which the post will be grouped")
def new(title, slug, category):
    """
    Create a new Markdown post with the specified title, slug, and category. 
    The post will be saved with a filename that includes the date and the slug.

    Example:
        cms new --title "My New Post" --slug "my-new-post" --category "Tech"
    """
    create_post(title, slug, category)

@click.command()
@click.option('--slug', required=True, help="Slug of the post to publish")
def publish(slug):
    """
    Publish a post and its associated media to an S3 bucket based on the post's slug.

    Example:
        cms publish --slug "my-new-post"
    """
    publish_post(slug)

@click.command()
@click.option('--query', required=True, help="Text to search for in the content and frontmatter of posts")
def search(query):
    """
    Search posts for a given query string within their content and frontmatter.

    Example:
        cms search --query "Python"
    """
    search_posts(query)

@click.command()
@click.option('--slug', required=True, help="Slug of the post for tagging")
@click.option('--tags', required=True, help="Comma-separated tags to add to the post")
def tag(slug, tags):
    """
    Add tags to a post's frontmatter. Existing tags are replaced by the provided list.

    Example:
        cms tag --slug "my-new-post" --tags "python,development,code"
    """
    update_post_tags(slug, tags)

@click.command()
@click.option('--slug', required=True, help="Slug of the post for categorization")
@click.option('--category', required=True, help="New category for the post")
def categorize(slug, category):
    """
    Update the category of a post's frontmatter.

    Example:
        cms categorize --slug "my-new-post" --category "Programming"
    """
    update_post_category(slug, category)

@click.command()
@click.option('--file-path', required=True, type=click.Path(exists=True), help="Absolute or relative path to the media file to upload")
def upload(file_path):
    """
    Upload a media file to an S3 bucket.

    Example:
        cms upload --file-path "/path/to/image.png"
    """
    upload_media(file_path)

@click.command()
@click.option('--slug', required=True, help="Slug of the post to update frontmatter")
@click.option('--frontmatter', required=True, help="YAML-formatted string of frontmatter to update")
def update(slug, frontmatter):
    """
    Update the frontmatter of a post based on a YAML-formatted string.

    Example:
        cms update --slug "my-new-post" --frontmatter "title: Updated Title"
    """
    update_frontmatter(slug, frontmatter)

@click.command()
@click.option('--slug', required=True, help="Slug of the post for which to manage revisions")
def revisions(slug):
    """
    Manage revisions for a post. This command will show or operate on the different versions of a post.

    Example:
        cms revisions --slug "my-new-post"
    """
    manage_revisions(slug)

cli.add_command(new)
cli.add_command(publish)
cli.add_command(search)
cli.add_command(tag)
cli.add_command(categorize)
cli.add_command(upload)
cli.add_command(update)
cli.add_command(revisions)

if __name__ == '__main__':
    cli()
