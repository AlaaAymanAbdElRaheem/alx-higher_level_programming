#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_len = PyList_Size(p);
	PyObject *item;
	int i;

	printf("[*] Size of the Python List = %ld\n", list_len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < list_len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
