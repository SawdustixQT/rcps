#include "SDL.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const int W = 640;
const int H = 480;
const int size = 4;
const int cols = W / size;
const int rows = H / size;

int grid[cols][rows];

void update(int grid[cols][rows]){
	for (int i = 0; i < cols; i++){
		if (rand() % 20 == 0){
			grid[i][0] = 1;
		}
	}
	for (int i = rows - 2; i >= 0; i--){
		for (int j = 0; j < cols; j++){
			if (grid[j][i] == 1){
				if (grid[j][i + 1] == 0){
					grid[j][i] = 0;
					grid[j][i + 1] = 1;
				}
			}
		}
	}
}

void draw(SDL_Renderer *r, int grid[cols][rows]){
	for (int i = 0; i < rows; i++){
		for (int j = 0; j < cols; j++){
			if (grid[j][i] == 0){
				SDL_SetRenderDrawColor(r, 0, 0, 0, 255);
			}
			else if (grid[j][i] == 1){
				SDL_SetRenderDrawColor(r, 255, 255, 255, 255);
			}
			SDL_Rect rect = {j * size, i * size, size, size};
			SDL_RenderDrawRect(r, &rect);
			SDL_RenderFillRect(r, &rect);
		}
	}
	SDL_RenderPresent(r);
}

int main(void) {
	srand(time(NULL));

	SDL_Init(SDL_INIT_VIDEO); // Initialize SDL2
	// Create an application window with the following settings:
	SDL_Window *window = SDL_CreateWindow(
		"black square", // window title
		SDL_WINDOWPOS_UNDEFINED, // initial x position
		SDL_WINDOWPOS_UNDEFINED, 
		W, 
		H,
		// SDL_WINDOW_OPENGL // По умолчанию
		SDL_WIDNOW_RESIZEABLE
	);

	// -1 
	SDL_Renderer *r = SDL_CreateRenderer(window, -1, SDL_RENDERED_ACCELERATED);
	
	for (int i = 0; i < rows; i++){
		for (int j = 0; j < cols; j++){
			grid[i][j] = 0;
		}
	}


	// // Для квадрата из 4 практической
	// SDL_SetRenderDrawColor(r, 255, 255, 255, 255); // RGB+Alpha канал
	// SDL_RenderClear(r);
	// SDL_RenderPresent(r);

	// render квадрата
	// SDL_Rect re = {W / 2 - 50, H / 2 - 50, 100, 100};
	
	// заполнение
	SDL_RenderFillRect(r, &re);
	SDL_RenderDrawRect(r, &re);

	// Для мака, незакрытие экрана
	SDL_Event e;
	int flag = 1;

	while(flag){
		while(SDL_PollEvent(&e)){
			if (e.type == SDL_QUIT){
				flag = 0;
				break;
			}
		}
		update(grid);
		draw(r, grid)
		SDL_Delay(1000 / 60); // 
	}


	SDL_DestroyWindow(window);
	SDL_Quit();
	return 0;
}