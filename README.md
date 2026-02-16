# qpdf-test

A simple Python HTTP server for testing and development.

## Features

- Simple HTTP server using Python's built-in `http.server` module
- Serves static files from a specified directory
- Configurable port number
- Command-line interface with arguments
- Proper error handling and logging

## Requirements

- Python 3.x (tested with Python 3.12)

## Usage

### Basic Usage

Start the server on the default port (8000):

```bash
python3 server.py
```

### Custom Port

Start the server on a specific port:

```bash
python3 server.py -p 8080
```

or

```bash
python3 server.py --port 8080
```

### Custom Directory

Serve files from a specific directory:

```bash
python3 server.py -d /path/to/directory
```

or

```bash
python3 server.py --directory /path/to/directory
```

### Combined Options

```bash
python3 server.py -p 9000 -d /path/to/directory
```

### Help

Display help information:

```bash
python3 server.py --help
```

## Example

```bash
$ python3 server.py -p 8888
Server started at http://localhost:8888
Serving files from: /home/user/qpdf-test
Press Ctrl+C to stop the server
```

Then open your browser and navigate to `http://localhost:8888` to see the directory listing and access files.

## Notes

- The server will serve all files in the specified directory
- Use Ctrl+C to stop the server
- The default directory is the current working directory
- Port numbers must be between 1 and 65535