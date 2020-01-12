#!usr/bin/python3
# -*- coding: utf-8 -*-
from server import app


# run on port 3031: uWSGI
if __name__ == '__main__':
    app.run()

