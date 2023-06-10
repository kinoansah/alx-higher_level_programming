This is a project task done as part of the ALX SOFTWARE ENGINEERING COURSE

TOPIC: Python - Data Structures: Lists, Tuples

AUTHOR: OWUSU ANSAH, Kingsley

# advanced tasks

14. CPython#0: Python lists

CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used used implementation of the language.
Since we now know a bit of C, and let's look at what makes Python so easy to use.

All your files will be interpreted/compiled on Ubuntu 14.04 LTS

Create a C function that prints some basic info about Python lists.

Prototype: void print_Python_list_info(Py0bject *p);
Format: see example
Python version: 3.4
Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
OS: ubuntu 14.04 LTS
Start by reading:
	listobject.h
	object.h
	Common Object Structures
	List Objects 

# mandatory tasks

13.
