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

static int lua_min(lua_State *L){
    luaL_checktype(L, 1, LUA_TABLE);
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

int main() {
    lua_State* l = luaL_newstate();
    luaL_openlibs(l);

    lua_register(l, "hex", lua_hex);
    luaL_dostring(l, "print(hex(25))");

    lua_register(l, "sum", lua_sum);
    luaL_dostring(l, "print(sum({1, 2, 3}))");

    lua_register(l, "min", lua_min);
    luaL_dostring(l, "print(min({1, 2, -3}))");

    lua_close(l);

    return 0;
}