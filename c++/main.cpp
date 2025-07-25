#include <windows.h>
#include "rasterizer.h"
#include <cstdint>

LRESULT CALLBACK windowprocedure(HWND, UINT, WPARAM, LPARAM);


BITMAPINFO bmi = {0};
float list[2] = {100, 50};
float list1[2] = {300, 200};

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR args, int ncmdshow){
    drawPixel(list, list1, 0x00FF0000);
    bmi.bmiHeader.biSize = sizeof(BITMAPINFOHEADER);
    bmi.bmiHeader.biWidth = 500;
    bmi.bmiHeader.biHeight = -500;
    bmi.bmiHeader.biPlanes = 1;
    bmi.bmiHeader.biBitCount = 32;
    bmi.bmiHeader.biCompression = BI_RGB;


    WNDCLASSW wc = {0};
    wc.hbrBackground = (HBRUSH) COLOR_WINDOW;
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);
    wc.hInstance = hInst;
    wc.lpszClassName = L"clasaokn";
    wc.lpfnWndProc = windowprocedure;

    if (!RegisterClassW(&wc)){
        return -1;
    }

    CreateWindowW(L"clasaokn", L"okno dla gitow", WS_OVERLAPPEDWINDOW | WS_VISIBLE, 100, 100, window_w, window_h, NULL, NULL, NULL, NULL);

    MSG msg = {0};

    while( GetMessage(&msg, nullptr, 0, 0)){
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}


LRESULT CALLBACK windowprocedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp){
    switch (msg){
        case WM_DESTROY:
            PostQuitMessage(0);
        case WM_PAINT: {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hWnd, &ps);
            StretchDIBits(
                hdc,
                0, 0, 500, 500,
                0, 0, 500, 500,
                buffer,
                &bmi,
                DIB_RGB_COLORS,
                SRCCOPY
            );


            EndPaint(hWnd, &ps);
            return 0;
        }
        default:
            return DefWindowProcW(hWnd, msg, wp, lp);
    }
}