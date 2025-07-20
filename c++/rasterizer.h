#ifndef RASTERYZER_H
#define RASTERYZER_H

#include <cstdint>

const int window_w = 500;
const int window_h = 500;

extern uint32_t buffer[window_w * window_h];

void drawPixel(float P0[2], float P1[2], uint32_t color);

#endif