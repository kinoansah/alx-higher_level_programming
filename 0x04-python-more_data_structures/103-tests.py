#include <Python.h>

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    unsigned char *bytes;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes:", size + 1);
    for (i = 0; i <= size; i++)
        printf(" %02x", bytes[i]);

    printf("\n");
}
