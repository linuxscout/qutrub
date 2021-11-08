#!/usr/bin/env python3
import sys
sys.path.insert(0,"/var/www/html/qutrub/interfaces/web/")
sys.path.insert(0,"/var/www/html/qutrub/")
from qutrub_webserver import app as application
# just for testing
def application2(environ,start_response):
    status = '200 OK'
    html = '<html>\n' \
           '<body>\n' \
           '<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n' \
           'Welcome to mod_wsgi Test Page\n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n'
    html = bytes(html, encoding= 'utf-8')           
    response_header = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(html)))]

    start_response(status,response_header)
    
    return [html]

