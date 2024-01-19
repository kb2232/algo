from strings_hash import parsepair

def main():
    s = "Method=GET Path=/sample?param1=value1&param2=value2 HTTP/1.1 Host:www.example.com User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Accept: application/json X-Service-Time: 100ms X-Request-Id: abc123"
    print(parsepair(s))
    return
if __name__ == "__main__":
    main()