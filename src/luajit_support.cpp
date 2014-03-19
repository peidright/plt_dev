#include "luajit_support.h"
//"local p = \"E:\\devshare\\resource\\LuaJIT-2.0.2\\src\" \n"  
//"local m_package_path = package.path \n" 
//"package.loadlib('E:\\devshare\\resource\\LuaJIT-2.0.2\\src\\lua51.dll','ffi') \n"
const char *lua_code =  
"local ffi = require(\"ffi\");                   \n"  
"ffi.cdef[[                                   \n"  
"const char * hello_from_lua(const char *);   \n" // matches the C prototype  
"void printf(const char *);"
"int Add(int,int);"  
"]]                                           \n"  
"ffi.C.hello_from_lua('Hello from LUA!')      \n" // do actual C call 
"ffi.C.printf(\"dddd\");"
"sum = ffi.C.Add(10,20)      \n"  
"print('sum:'..sum)      \n"  
; 

extern "C"   
{  
    __declspec(dllexport) void __cdecl hello_from_lua(const char *msg)  
    {  
        printf("A message from LUA: %s\n", msg);  
    }  
    __declspec(dllexport) int  Add(int a,int b)  
    {  
        return a+b;  
    }  
} 

void  luajit_demo()  
{  
    lua_State *lua = luaL_newstate();  
    assert(lua);  
    luaL_openlibs(lua);  
  
    const int status = luaL_dostring(lua, lua_code);  
    if(status)  
        printf("Couldn't execute LUA code: %s\n", lua_tostring(lua, -1));  
  
    lua_close(lua);  
}  