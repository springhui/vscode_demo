#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main_handler(event, context):
    f = open("./demo.html")
    html = f.read()
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body": html
    }