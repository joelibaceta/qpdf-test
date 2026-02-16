#!/usr/bin/env python3
"""
Basic Python HTTP Server

This script provides a simple HTTP server that serves files from the current directory.
It can be used for testing and development purposes.
"""

import argparse
import errno
import http.server
import os
import socketserver
import sys
from pathlib import Path


class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler with logging."""
    
    def log_message(self, format, *args):
        """Log an arbitrary message."""
        sys.stdout.write(f"[{self.log_date_time_string()}] {format % args}\n")


def start_server(port=8000, directory=None):
    """
    Start the HTTP server.
    
    Args:
        port (int): Port number to listen on (default: 8000)
        directory (str): Directory to serve files from (default: current directory)
    """
    if directory:
        directory_path = Path(directory).resolve()
        if not directory_path.exists():
            print(f"Error: Directory '{directory}' does not exist")
            sys.exit(1)
        if not directory_path.is_dir():
            print(f"Error: '{directory}' is not a directory")
            sys.exit(1)
    else:
        directory_path = Path.cwd()
    
    # Change to the directory before starting the server
    os.chdir(directory_path)
    
    handler = SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"Server started at http://localhost:{port}")
            print(f"Serving files from: {directory_path}")
            print("Press Ctrl+C to stop the server")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        sys.exit(0)
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            print(f"Error: Port {port} is already in use")
        else:
            print(f"Error: {e}")
        sys.exit(1)


def main():
    """Main function to parse arguments and start the server."""
    parser = argparse.ArgumentParser(
        description="Basic Python HTTP Server - Serves files from a directory"
    )
    parser.add_argument(
        "-p", "--port",
        type=int,
        default=8000,
        help="Port number to listen on (default: 8000)"
    )
    parser.add_argument(
        "-d", "--directory",
        type=str,
        default=None,
        help="Directory to serve files from (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Validate port number
    if not (1 <= args.port <= 65535):
        print(f"Error: Port must be between 1 and 65535")
        sys.exit(1)
    
    start_server(port=args.port, directory=args.directory)


if __name__ == "__main__":
    main()
