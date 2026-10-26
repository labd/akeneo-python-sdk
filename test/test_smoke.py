"""Smoke tests for the generated client: models and an API call round-trip."""

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

import akeneo
from akeneo.models.categories import Categories

CATEGORIES = {
    "_links": {"self": {"href": "http://localhost/api/rest/v1/categories"}},
    "current_page": 1,
    "_embedded": {
        "items": [
            {
                "code": "master",
                "parent": None,
                "labels": {"en_US": "Master catalog"},
            }
        ]
    },
}


def test_model_round_trip():
    categories = Categories.from_dict(CATEGORIES)
    assert categories.current_page == 1
    assert categories.embedded.items[0].code == "master"
    assert categories.to_dict()["_embedded"]["items"][0]["labels"] == {
        "en_US": "Master catalog"
    }
    assert Categories.from_json(categories.to_json()) == categories


@pytest.fixture
def server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            body = json.dumps(CATEGORIES).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            Handler.paths.append(self.path)

        def log_message(self, *args):
            pass

    Handler.paths = []
    httpd = HTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield httpd, Handler.paths
    httpd.shutdown()
    httpd.server_close()


def test_api_call(server):
    httpd, paths = server
    configuration = akeneo.Configuration(
        host=f"http://127.0.0.1:{httpd.server_address[1]}"
    )
    with akeneo.ApiClient(configuration) as api_client:
        result = akeneo.CategoryApi(api_client).get_categories(limit=10)

    assert isinstance(result, Categories)
    assert result.embedded.items[0].code == "master"
    assert paths == ["/api/rest/v1/categories?limit=10"]
