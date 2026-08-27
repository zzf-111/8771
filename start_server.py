# -*- coding: utf-8 -*-
"""启动本地检索服务，供网页版访问 kb_search.html + kb_data.json。"""
import http.server, socketserver, os, webbrowser

ROOT = os.path.join(os.path.dirname(__file__))
PORT = 8788

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, *a):
        pass

os.chdir(ROOT)
with socketserver.TCPServer(("", PORT), H) as httpd:
    print(f"检索服务已启动: http://localhost:{PORT}/search/kb_search.html")
    print("按 Ctrl+C 停止")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("已停止")
