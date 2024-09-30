#ifndef PYTHON_H
#define PYTHON_H

#include <Python.h>  // Necessary to interact with Python objects

// Function prototypes
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

#endif /* PYTHON_H */
