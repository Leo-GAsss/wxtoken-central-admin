import datetime
import json
import os
import sys
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from secrets import token_urlsafe
from threading import Lock, Timer
from urllib.parse import urlencode
from urllib.request import urlopen

token = ""
token_lock = Lock()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.lstrip('/').rstrip('/') == os.environ["apikey"]:
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            token_lock.acquire()
            self.wfile.write(json.dumps(
                {"access_token": token}).encode("utf-8"))
            token_lock.release()
        else:
            self.send_response(HTTPStatus.UNAUTHORIZED)
            self.end_headers()


def get_access_token():
    global token

    url = os.environ["url"] + urlencode({k: os.environ[k]
                                        for k in os.environ["params"].split(',')})
    with urlopen(url) as req:
        resp = json.loads(req.read())
        token_lock.acquire()
        token = resp["access_token"]
        token_lock.release()
        expires_in = resp["expires_in"]

    print(f"Get at {datetime.datetime.now()}")
    # Refresh When 5 Minutes Before Expires
    timer = Timer(expires_in - 5 * 60, get_access_token)
    timer.setDaemon(True)
    timer.start()


if __name__ == "__main__":
    if "apikey" not in os.environ:
        print("apikey generated, please fill out .env\n")
        print(' ' * 4 + token_urlsafe(64) + '\n')
    else:
        get_access_token()
        with HTTPServer(("127.0.0.1", int(os.environ["port"])), Handler) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                sys.exit(0)
