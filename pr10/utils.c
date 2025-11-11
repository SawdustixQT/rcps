#include <stdio.h>
#include <lua.h>
#include <lualib.h>
#include <lauxlib.h>

static int lua_hex(lua_State* l) {
    lua_Integer count = luaL_checkinteger(l, 1);
    //printf("%d", count);
    const char hex_str[] = "0123456789ABCDEF";
    char result[64];
    int index = 0;

    while (count > 0)
    {
        result[index++] = hex_str[count % 16];
        count /= 16;
    }

    //printf("%s", result);

    char final[64] = "0x";
    int index2 = 2;
    for (int i = index - 1; i >= 0 ; i--) {
        final[index2++] = result[i];
    }

    //printf("%s", final);

    lua_pushstring(l, final);

    return 1;
}

static int lua_sum(lua_State* L){
    luaL_checktype(L, 1, LUA_TTABLE);
    const int len = lua_rawlen(L, 1);
    lua_Number res = 0;
    for (int i = 1; i <= len; i++){
        lua_rawgeti(L, 1, i);
        res += lua_tonumber(L, -1);
        lua_pop(L, 1);
    }
    lua_pushnumber(L, res);
    return 1;
}

static int lua_min(lua_State* L){
    luaL_checktype(L, 1, LUA_TTABLE);
    const int len = lua_rawlen(L, 1);
    lua_Number res = INT_MAX;
    for (int i = 1; i <= len; i++){
        lua_rawgeti(L, 1, i);
        if (lua_tonumber(L, - 1) < res){
            res= lua_tonumber(L, - 1);
        }
        lua_pop(L, 1);
    }
    lua_pushnumber(L, res);
    return 1;
}

static const luaL_Reg utils[] = {
    {"hex", lua_hex},
    {"sum", lua_sum},
    {"min", lua_min},
    {NULL, NULL}
};

int luaopen_utils(lua_State* L){
    luaL_newlib(L, utils_functions);
    return 1;
}