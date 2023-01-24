import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
from myconverter import SelectConverter

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        urlparsed = urlparse(self.path)
        queryparsed= parse_qs(urlparsed.query)
        choice, amount = queryparsed['choice'][0],queryparsed['amount'][0]
        
        converter = SelectConverter.get_converter(int(choice))
        
        result = converter.convert(int(amount))
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response = f'your choice is {choice} and the amount is {amount}, the result is {result}'
        self.wfile.write(str.encode(response))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()