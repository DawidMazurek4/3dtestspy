#include <cstdint>
#include "rasterizer.h"


uint32_t buffer[window_w * window_h];

void drawPixel(float P0[2], float P1[2], uint32_t color){
    float x0 = P0[0];
    float x1 = P1[0];

    float y0 = P0[1];
    float y1 = P1[1];

    float a = (y1 - y0) / (x1 - x0);
    float b = y0 - a * x0;
    for(int i=x0;i<x1;i++){
        float y = a * i + b;
        buffer[int(y)*window_w + i] = color;
    }
}