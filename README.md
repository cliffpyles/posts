# Posts

A lightweight Content Management System

## Overview

This project offers a straightforward environment for managing blog posts and associated media. It's designed to be a foundational tool for individuals looking to organize and maintain their content efficiently. The system uses a simple file structure and a command-line interface (CLI) to create, manage, and publish posts written in Markdown with frontmatter.

## File Structure

The project is organized into several directories:

- `content/`: Contains all Markdown files for the posts.
- `media/`: Holds media files like images and videos referenced in the posts.
- `revisions/`: Stores versions and revisions of posts and media files.
- `logs/`: Keeps log files for operations.

## CLI Tool

The CLI tool provides various commands to manage posts and media:

- **Create Posts**: Generate new Markdown files with titles, slugs, and categories.
- **Publish**: Upload posts and media to S3 for online access.
- **Search**: Find posts by searching content and frontmatter.
- **Tagging and Categorizing**: Organize posts by tags and categories.
- **Media Management**: Upload and manage media files on S3.
- **Update Frontmatter**: Modify metadata in the posts.
- **Revisions**: Handle different versions of posts and media.

## Getting Started

To use this project, clone the repository and ensure you have Python installed. The main script `cli.py` in the `cli/` folder is executable and contains all necessary commands to interact with your content.

1. **Clone the repository**: `git clone [repository-url]`
2. **Navigate to the project**: `cd [project-name]`
3. **Install dependencies**: Ensure `click`, `pyyaml`, and `boto3` are installed via `pip install click pyyaml boto3`.
4. **Run the CLI**: Use commands like `./cli/cli.py new --title "Example Post" --slug "example-post" --category "General"` to create new content.

For a full list of commands and options, run `./cli/cli.py --help`.

This project is set up to be a simple, usable starting point for your content management needs. Adjust and expand it as needed to fit your specific requirements.
