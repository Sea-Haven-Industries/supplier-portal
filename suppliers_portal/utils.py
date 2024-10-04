def before_request(request, method, url, headers):
    print("Before Request")
    print(request)
    print(method)
    print(url)
    print(headers)
