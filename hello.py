from cgi import parse_qs
def application(environ, start_response):
    queryString = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    body = ''    
    for key, value in queryString.items():
        for element in value:
            body = body + str(key) + "="
            body = body + str(element) + "\r\n"
    data=body.encode()
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data))),
    ])
    return [data]
