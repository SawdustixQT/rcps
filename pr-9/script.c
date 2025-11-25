// 1-3 задачи https://github.com/true-grue/kisport/blob/main/pract2.md

// Для запуска программы использовать script.bat (требуется установленный gcc)

#include <stdio.h>
#include <lua.h>
#include <lualib.h>
#include <lauxlib.h>
// Для 3 задания
#include <stdint.h>

// ↓ Фукнция и переменная для 3 задачи
static uint32_t x = 123456;

uint32_t xorshift32(){
    x ^= x << 13;
    x ^= x >> 17;
    x ^= x << 5;
    return x;
}

static int lua_rnd(lua_State* L){
    uint32_t y = xorshift32();
    if (lua_gettop(L) == 0){
        double z = (double) y / UINT32_MAX;
        lua_pushnumber(L, z);
        // printf("%.2f", z);
    }
    else {
        int n = luaL_checkinteger(L, 1);
        lua_pushinteger(L, (y % n) + 1);
    }
    return 1;
}
// ↑ Фукнция и переменная для 3 задачи


int main(){
    lua_State* L = luaL_newstate();
    luaL_openlibs(L);

    // Задача 1
    luaL_dostring(L, "print(2 + 2)");
    if (luaL_dostring(L, "print(2 + 2)") != LUA_OK){
        fprintf(stderr, "Error: %s\n", lua_tostring(L, -1));
        lua_close(L);
    }

    // Задача 2 - Работа с функцией LUA  
    lua_State* L = luaL_newstate();
    luaL_openlibs(L);

    double a = 1.0, b = -5.0, c = 6.0;
    lua_pushnumber(L, b);
    lua_pushnumber(L, b);
    lua_arith(L, LUA_OPMUL);
    lua_pushnumber(L, c);
    lua_pushnumber(L, a);
    lua_pushnumber(L, 4);
    lua_arith(L, LUA_OPMUL);
    lua_arith(L, LUA_OPMUL);
    printf("4ac: %.2f\n", lua_tonumber(L, -1));

    lua_arith(L, LUA_OPSUB);

    double result = lua_tonumber(L, -1);

    // Задача 2 - Работа с функцией LUA  
    luaL_dofile(L, "script.lua");
    lua_getglobal(L, "discriminante");
    lua_pushnumber(L, a);
    lua_pushnumber(L, b);
    lua_pushnumber(L, c);
    lua_call(L, 3, 1);
    double res = lua_tonumber(L, -1);
    printf("File: %.2f\n", result);
    
    // Задача 3
    lua_register(L, "rnd", lua_rnd);
    if (luaL_dostring(L, "print(rnd())") != LUA_OK){
        fprintf(stderr, "%s\n", lua_tostring(L, -1));
    }
    luaL_dostring(L, "print(rnd(5))");

    lua_close(L);
    
}