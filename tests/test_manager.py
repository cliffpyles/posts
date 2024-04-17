# tests/test_manager.py
import pytest
from unittest.mock import patch
from cli.manager import create_post, publish_post, search_posts

def test_create_post():
    with patch('cli.manager.write_file') as mocked_write, \
         patch('cli.manager.generate_slug', return_value='my-new-post'), \
         patch('cli.manager.datetime.datetime') as mocked_datetime:
        mocked_datetime.now.return_value.strftime.return_value = '2024-04-17'
        create_post("Test Post", "Test Post", "Test")
        expected_filename = '2024-04-17-my-new-post.md'
        expected_content = '---\n' + 'title: Test Post\ndate: \'2024-04-17\'\ntags: []\ncategory: Test\npublished: false\n' + '---\n\n# Test Post\nWrite your content here...'
        mocked_write.assert_called_once_with(f'content/{expected_filename}', expected_content)

def test_publish_post():
    with patch('cli.manager.upload_to_s3') as mocked_upload, \
         patch('cli.manager.find_post_by_slug', return_value=('path/to/post.md', 'content')):
        publish_post("my-new-post")
        mocked_upload.assert_called_once()

@pytest.mark.parametrize("query, expected", [
    ("python", True),
    ("nothing", False)
])
def test_search_posts(query, expected, mocker):
    mocker.patch('cli.manager.os.listdir', return_value=['post1.md', 'post2.md'])
    mocker.patch('cli.manager.read_file', side_effect=["python content", "other content"])
    mocker.patch('builtins.print')
    search_posts(query)
    assert print.called is expected
