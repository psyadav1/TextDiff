import requests
import pytest


class TestTextDiff(object):
    def setup_method(self):
        self.host = '127.0.0.1'
        self.port = 5000

    def test_text_diff_should_return_stadard_diff_arr(self):
        url = 'http://%s:%d/text-diff' % (self.host, self.port)
        json_obj = {
            'text_from': 'Hello World.',
            'text_to': 'Goodbye World.'
        }
        with requests.session() as session:
            response = session.post(url, json=json_obj)
        result = response.json()
        except_arr = [[-1, 'Hell'], [1, 'G'],
                      [0, 'o'], [1, 'odbye'], [0, ' World.']]
        assert str(except_arr) == str(result['data'])

    def test_text_diff_cleanup_semantic_should_return_diff_word_arr(self):
        url = 'http://%s:%d/text-diff-cleanup-semantic' % (
            self.host, self.port)
        json_obj = {
            'text_from': 'Hello World.',
            'text_to': 'Goodbye World.'
        }
        with requests.session() as session:
            response = session.post(url, json=json_obj)
        result = response.json()
        except_arr = [[-1, "Hello"], [1, "Goodbye"], [0, " World."]]
        assert str(except_arr) == str(result['data'])
