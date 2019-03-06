PyQt5 Bitcoin Price Checker
===========================

Install PyQt5 dependencies::

  pip install pyqt5

To rebuild the designer file if modified, run::

  pyuic5 templates/main_window.ui -o main_window.py

To run::

  python main.py

To package::

  pyinstaller main.py

To create a Debian package, inside the dist/ build folder with
the program output, create a DEBIAN directory, and add a ``control``
file, with these contents, for example::

 Package: bitcoin-checker
 Version: 1.0.0
 Maintainer: Your Name <you@example.com>
 Description: My test package, please ignore
 Homepage: https://github.com/username/projectname
 Architecture: all

And then create the directory structure desired in the root project dist folder.
For example, create ``/opt/bitcoin-checker`` w/ all the python files,
and ``/usr/bin/bitcoin-checker`` launch file.



Link to live stream: https://www.youtube.com/watch?v=4Q2vsbqhE14