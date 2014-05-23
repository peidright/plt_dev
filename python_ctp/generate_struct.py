#-*- coding=utf-8 -*-
"""
A wrapper for CTP's Api library
author: Lvsoft@gmail.com
date: 2010-07-20

This file is part of python-ctp library

python-ctp is free software; you can redistribute it and/or modify it
under the terms of the GUL Lesser General Public License as published
by the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

python-ctp is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY of FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along the python-ctp; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301 USA
"""

def generate_py(struct_name, datas, f):
    fields = datas[struct_name]['fields']
    f.write("class %s:\n" % struct_name)
    f.write("    def __init__(self, %s):\n" % 
            ", ".join(
            ["%s=%s" % 
             (x, fields[x]['default']) for x in fields]))
    for i in fields:
        f.write("        self.%s=%s\n" % (i,i))

    vcmap={}
    for i in fields:
        if fields[i]['type']['type'].startswith('enum'):
            vcmap[i]={}
            ev = fields[i]['type']
            for j in ev['values']:
                vcmap[i][ev['values'][j]['value']] = ev['values'][j]['comment']

    f.write("        self.vcmap=%s\n" % repr(vcmap))

    f.write('    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ' + repr([x for x in fields])+'])\n')
    f.write('    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in ' + '[%s]' % (",".join(["('%s', u'%s')" % (x, fields[x]['comment'].encode('utf-8')) for x in fields]),) + '])\n')
    f.write('    def getval(self, n):\n')
    f.write('        if n in %s:\n' % repr([x for x in fields if fields[x]['type']['type'].startswith('enum')]))
    f.write('            return self.vcmap[n][getattr(self, n)].encode("utf-8")\n')
    f.write('        else: return getattr(self, n)\n')

def get_struct_type(t):
    if t.startswith("enum"): return "c"
    elif t=='short': return 'h'
    else: return t[0]

def generate_cpp(struct_name, datas, f):
    fields = datas[struct_name]['fields']
    f.write("\n//%s\n" % datas[struct_name]['comment'].encode('utf-8'));
    f.write("PyObject * new_%s(%s * p){\n" % (struct_name, struct_name))
    f.write('  return PyObject_CallMethod(mod, (char*)"%s", %s,\n' % (struct_name, 
                                                               fields and '(char*)"'+"".join([get_struct_type(fields[i]['type']['type']) for i in fields])+'"' or "NULL"))
    f.write(", ".join(['p->%s' % i for i in fields ]))
    f.write(");\n}\n")

    f.write("%s * from_%s(PyObject * p){\n" % (struct_name, struct_name))
    
    f.write("  %s *t = (%s *)calloc(1, sizeof(%s));\n" % (struct_name, struct_name, struct_name))
    for i in fields:
        f.write("  //%s\n" % fields[i]['comment'].encode('utf-8'));
        t=fields[i]['type']['type']
        if t == 'double':
            f.write("  t->%s = " %  i)
            f.write("  PyFloat_AsDouble(PyObject_GetAttrString(p, \"%s\"));\n" % i)
        elif t == 'int':
            f.write("  t->%s = " % i)
            f.write("  PyInt_AsLong(PyObject_GetAttrString(p, \"%s\"));\n" % i)
        elif t == 'short':
            f.write("  t->%s = " % i)
            f.write("  PyInt_AsLong(PyObject_GetAttrString(p, \"%s\"));\n" % i)
        elif t == 'string' or i[0] in ['Time','Date']: # FIXME
            f.write("  strcpy(t->%s, PyString_AsString(PyObject_GetAttrString(p, \"%s\")));\n" % (i, i))
        elif t.startswith('enum'):
            f.write("  //enum类型\n")
            ev = fields[i]['type']['values']
            for e in ev:
                f.write("  //%s -> %s, %s\n" % (e, ev[e]['value'],
                                                ev[e]['comment'].encode('utf-8')))
            f.write("  t->%s = " % i)
            f.write("  PyString_AsString(PyObject_GetAttrString(p, \"%s\"))[0];\n" % i)
            
        else: 
            print "unknown type:", t
    
    f.write("\n  return t;\n};\n")

def generate_hpp(struct_name, datas, f):
#    fields = datas[struct_name]['fields']
    f.write("PyObject * new_%s(%s * p);\n" % (struct_name, struct_name))
    f.write("%s * from_%s(PyObject * p);\n" % (struct_name, struct_name))


def generate_interface():
    import parse_struct
    datas = parse_struct.parse("../inc/ThostFtdcUserApiDataTypeSSE.h",
                               '../inc/ThostFtdcUserApiStructSSE.h')
    
#generate python
    f=file("UserApiStruct.py", "w")
    f.write('#-*- coding=utf-8 -*-\n"""'+__doc__+'"""\n')
    f.write('"""\n'+__doc__+'"""\n')
    f.write("""
#This file is auto generated! Please don't edit directly.
""")
    for i in datas: generate_py(i, datas, f)

    f.write("# Set short name alias for the stupid Hungarian Notation\n")
    for i in datas:
        f.write("%s=%s\n" % (i[12:-5],i))

    f.close()


#generate cpp
    f=file("struct.cpp", "w")
    f.write("/*"+__doc__+'*/\n')
    f.write("""
//This file is auto generated! Please don't edit directly.
""")
    f.write("""#include "struct.h"

static PyObject * mod=NULL;
PyObject * register_struct(PyObject * self, PyObject * args){
  mod = PyTuple_GET_ITEM(args,0);
  Py_INCREF(Py_None);
  return Py_None;
}
""")
    for i in datas: generate_cpp(i, datas, f)
    f.close()

#generate hpp
    f=file("struct.h", "w")
    f.write("/*"+__doc__+'*/\n')
    f.write("""
//This file is auto generated! Please don't edit directly.
""")
    f.write("""#ifndef STRUCT_TRADE_H
#define STRUCT_TRADE_H

#include <Python.h>
#include "ThostFtdcUserApiStructSSE.h"


PyObject * register_struct(PyObject * self, PyObject * args);
""")
    for i in datas: generate_hpp(i, datas, f)

    f.write("#endif\n")
    f.close()

generate_interface()
