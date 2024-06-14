import os
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(
    server_class=HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
    port=8888,
    directory="public",
):
    if directory:  # Change the current working directory if directory is specified
        print(f"Changing directory to {directory}")
        os.chdir(directory)
        print(f"Current working directory: {os.getcwd()}")
        print(f"Directory contents: {os.listdir()}")
        if 'images' in os.listdir():
            print(f"Images directory contents: {os.listdir('images')}")
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on http://localhost:{port} from directory '{directory}'...")
    httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Server")
    parser.add_argument(
        "--dir", type=str, help="Directory to serve files from", default="."
    )
    parser.add_argument("--port", type=int, help="Port to serve HTTP on", default=8888)
    args = parser.parse_args()

    run(port=args.port, directory=args.dir)
