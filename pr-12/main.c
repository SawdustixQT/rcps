#include <SDL.h>
#include <lua.h>
#include <lualib.h>
#include <lauxlib.h>

// Глобальный рендерер - все Lua функции будут его использовать
SDL_Renderer *g_renderer = NULL;

// Функция для Lua: clear(r, g, b) - заливает экран цветом
static int lua_clear(lua_State *L) {
    int r = luaL_checkinteger(L, 1);
    int g = luaL_checkinteger(L, 2);
    int b = luaL_checkinteger(L, 3);
   
    SDL_SetRenderDrawColor(g_renderer, r, g, b, 255);
    SDL_RenderClear(g_renderer);
    return 0;
}

// Функция для Lua: rect(x, y, w, h, r, g, b) - рисует закрашенный прямоугольник
static int lua_rect(lua_State *L) {
    int x = luaL_checkinteger(L, 1);
    int y = luaL_checkinteger(L, 2);
    int w = luaL_checkinteger(L, 3);
    int h = luaL_checkinteger(L, 4);
    int r = luaL_checkinteger(L, 5);
    int g = luaL_checkinteger(L, 6);
    int b = luaL_checkinteger(L, 7);
   
    SDL_SetRenderDrawColor(g_renderer, r, g, b, 255);
    SDL_Rect rect = {x, y, w, h};
    SDL_RenderFillRect(g_renderer, &rect);
    return 0;
}

int main(int argc, char *argv[]) {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window = SDL_CreateWindow("Engine Step 2",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        800, 600, SDL_WINDOW_SHOWN);
    g_renderer = SDL_CreateRenderer(window, -1,
        SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
   
    // Создаём виртуальную машину Lua
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
   
    // Регистрируем наши функции для рисования
    lua_register(L, "clear", lua_clear);
    lua_register(L, "rect", lua_rect);
   
    // Загружаем игровой скрипт
    luaL_dofile(L, "game.lua");
    lua_getglobal(L, "init");
    lua_pcall(L, 0, 0, 0);
   
    int running = 1;
    SDL_Event event;
   
    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) running = 0;

            if (event.type == SDL_KEYDOWN){
                lua_getglobal(L, "key_press");
                lua_pushstring(L, SDL_GetKeyName(event.key.keysym.sym));
                lua_pcall(L, 1, 0, 0);
            }
        }
       
        lua_getglobal(L, "update");
        lua_pcall(L, 0, 0, 0);
       
        // Вызываем Lua функцию draw каждый кадр
        lua_getglobal(L, "draw");
        lua_pcall(L, 0, 0, 0);
       
        SDL_RenderPresent(g_renderer);
        SDL_Delay(16);
    }
   
    lua_close(L);
    SDL_DestroyRenderer(g_renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}