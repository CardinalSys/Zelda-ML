#include <iostream>
#include <stdlib.h>
#include "proc.h"
#include <thread>
#include <mutex>
#include <string>
#include <iomanip>
#include <chrono>

std::mutex mtx;
uintptr_t moduleBase;
HANDLE hProcess;
uintptr_t baseAddress;

bool stop = false;

time_t lastTime = time(NULL) - 10;

void HookEmulator();
void GetVariables();
void ShowRepetitions();
void WriteMemory(std::vector<unsigned int> offsets, BYTE value);
char ReadMemory(std::vector<unsigned int> offsets);


//Variables
int input = 0;
int resetsNumberDecenas = 0;
int resetsNumberUnidades = 0;
int resetsNumberCentenas = 0;
int resetsNumberMil = 0;
int resetsNumberDecMil = 0;
int resetsNumberCentMil = 0;

bool isReseting = false;
bool isOpeningMenu = false;


//Varialbes-Player
BYTE playerXPos = 0;
BYTE playerYPos = 0;
BYTE playerDir = 0;
BYTE playerMapLocation = 0;
BYTE playerLife = 0;
BYTE currentSword = 0;

BYTE playerBtnPressed = 0;
BYTE gameStatus = 0;
BYTE killsCount = 0;

//Variables-Enemies
BYTE enemy1xPos = 0;
BYTE enemy2xPos = 0;
BYTE enemy3xPos = 0;
BYTE enemy4xPos = 0;
BYTE enemy5xPos = 0;
BYTE enemy6xPos = 0;

BYTE enemy1yPos = 0;
BYTE enemy2yPos = 0;
BYTE enemy3yPos = 0;
BYTE enemy4yPos = 0;
BYTE enemy5yPos = 0;
BYTE enemy6yPos = 0;

BYTE enemy1Dir = 0;
BYTE enemy2Dir = 0;
BYTE enemy3Dir = 0;
BYTE enemy4Dir = 0;
BYTE enemy5Dir = 0;
BYTE enemy6Dir = 0;

BYTE enemy1xProjectil = 0;
BYTE enemy2xProjectil = 0;
BYTE enemy3xProjectil = 0;
BYTE enemy4xProjectil = 0;

BYTE enemy1yProjectil = 0;
BYTE enemy2yProjectil = 0;
BYTE enemy3yProjectil = 0;
BYTE enemy4yProjectil = 0;

int main()
{
    HookEmulator();
}

void HookEmulator()
{
    DWORD procId = GetProcID(L"Mesen.exe");
    if (procId != 0)
    {
        HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

        //Get Module base address
        moduleBase = GetModuleBaseAddress(procId, L"MesenCore.dll");
        //Get handle to process
        hProcess = OpenProcess(PROCESS_ALL_ACCESS, NULL, procId);
        //Resolve base address
        baseAddress = moduleBase + 0x042E0F30;

        while (true)
        {
            GetVariables();
            //Print a string with all data so python subprocess can read it
            std::cout << "Player:" << (int)playerXPos << ";" << (int)playerYPos << ";" << (int)playerDir << ";" << (int)playerMapLocation << ";" << (int)playerLife << ";" << (int)currentSword << ";";
            std::cout << "Enemies:" << (int)enemy1xPos << ";" << (int)enemy2xPos << ";" << (int)enemy3xPos << ";" << (int)enemy4xPos << ";" << (int)enemy5xPos << ";" << (int)enemy6xPos << ";";
            std::cout << (int)enemy1yPos << ";" << (int)enemy2yPos << ";" << (int)enemy3yPos << ";" << (int)enemy4yPos << ";" << (int)enemy5yPos << ";" << (int)enemy6yPos << ";";
            std::cout << (int)enemy1Dir << ";" << (int)enemy2Dir << ";" << (int)enemy3Dir << ";" << (int)enemy4Dir << ";" << (int)enemy5Dir << ";" << (int)enemy6Dir << ";";
            std::cout << (int)enemy1xProjectil << ";" << (int)enemy2xProjectil << ";" << (int)enemy3xProjectil << ";" << (int)enemy4xProjectil << ";";
            std::cout << (int)enemy1yProjectil << ";" << (int)enemy2yProjectil << ";" << (int)enemy3yProjectil << ";" << (int)enemy4yProjectil << ";" << (int)killsCount << "\n";

            std::cin >> input;

            //ShowRepetitions();
        }

    }
}


void ShowRepetitions()
{
    WriteMemory({ 0xB8, 0x78, 0x657 }, 1);

    resetsNumberUnidades++;

    if (resetsNumberUnidades > 9)
    {
        resetsNumberUnidades = 0;
        resetsNumberDecenas++;
    }

    if (resetsNumberDecenas > 9)
    {
        resetsNumberDecenas = 0;
        resetsNumberCentenas++;
    }

    if (resetsNumberCentenas > 9)
    {
        resetsNumberCentenas = 0;
        resetsNumberMil++;
    }

    if (resetsNumberMil > 9)
    {
        resetsNumberMil = 0;
        resetsNumberDecMil++;
    }

    if (resetsNumberDecMil > 9)
    {
        resetsNumberDecMil = 0;
        resetsNumberCentMil++;
    }



    WriteMemory({ 0x98, 0x70, 0x1F }, resetsNumberUnidades);
    WriteMemory({ 0x98, 0x70, 0x1E }, resetsNumberDecenas);
    WriteMemory({ 0x98, 0x70, 0x1D }, resetsNumberCentenas);

    WriteMemory({ 0x98, 0x70, 0x1C }, resetsNumberMil);
    WriteMemory({ 0x98, 0x70, 0x1B }, resetsNumberDecMil);
    WriteMemory({ 0x98, 0x70, 0x1A }, resetsNumberCentMil);

    input = 0;
    isReseting = false;
}

void GetVariables()
{
    //Player
    playerXPos = ReadMemory({ 0xB8, 0x78, 0x70 });
    playerYPos = ReadMemory({ 0xB8, 0x78, 0x84 });
    playerDir = ReadMemory({ 0xB8, 0x78, 0x98 });
    playerMapLocation = ReadMemory({ 0xB8, 0x78, 0xEB });
    playerLife = ReadMemory({ 0xB8, 0x78, 0x670 });
    playerBtnPressed = ReadMemory({ 0xB8, 0x78, 0xFA });
    currentSword = ReadMemory({ 0xB8, 0x78, 0x657 });
    gameStatus = ReadMemory({ 0xB8, 0x78, 0x12 });
    killsCount = ReadMemory({ 0xB8, 0x78, 0x627 });

    //Enemies
    enemy1xPos = ReadMemory({ 0xB8, 0x78, 0x71 });
    enemy2xPos = ReadMemory({ 0xB8, 0x78, 0x72 });
    enemy3xPos = ReadMemory({ 0xB8, 0x78, 0x73 });
    enemy4xPos = ReadMemory({ 0xB8, 0x78, 0x74 });
    enemy5xPos = ReadMemory({ 0xB8, 0x78, 0x75 });
    enemy6xPos = ReadMemory({ 0xB8, 0x78, 0x76 });

    enemy1yPos = ReadMemory({ 0xB8, 0x78, 0x85 });
    enemy2yPos = ReadMemory({ 0xB8, 0x78, 0x86 });
    enemy3yPos = ReadMemory({ 0xB8, 0x78, 0x87 });
    enemy4yPos = ReadMemory({ 0xB8, 0x78, 0x88 });
    enemy5yPos = ReadMemory({ 0xB8, 0x78, 0x89 });
    enemy6yPos = ReadMemory({ 0xB8, 0x78, 0x8A });

    enemy1Dir = ReadMemory({ 0xB8, 0x78, 0x99 });
    enemy2Dir = ReadMemory({ 0xB8, 0x78, 0x9A });
    enemy3Dir = ReadMemory({ 0xB8, 0x78, 0x9B });
    enemy4Dir = ReadMemory({ 0xB8, 0x78, 0x9C });
    enemy5Dir = ReadMemory({ 0xB8, 0x78, 0x9D });
    enemy6Dir = ReadMemory({ 0xB8, 0x78, 0x9E });

    enemy1xProjectil = ReadMemory({ 0xB8, 0x78, 0x77 });
    enemy2xProjectil = ReadMemory({ 0xB8, 0x78, 0x78 });
    enemy3xProjectil = ReadMemory({ 0xB8, 0x78, 0x79 });
    enemy4xProjectil = ReadMemory({ 0xB8, 0x78, 0x7A });

    enemy1yProjectil = ReadMemory({ 0xB8, 0x78, 0x8B });
    enemy2yProjectil = ReadMemory({ 0xB8, 0x78, 0x8C });
    enemy3yProjectil = ReadMemory({ 0xB8, 0x78, 0x8D });
    enemy4yProjectil = ReadMemory({ 0xB8, 0x78, 0x8E });
}


char ReadMemory(std::vector<unsigned int> offsets) {
    uintptr_t address = FindDMAAddy(hProcess, baseAddress, offsets);
    char value;
    ReadProcessMemory(hProcess, (BYTE*)address, &value, sizeof(value), nullptr);
    return value;
}

void WriteMemory(std::vector<unsigned int> offsets, BYTE value)
{
    LPVOID addressToWrite = (LPVOID)FindDMAAddy(hProcess, baseAddress, offsets);
    SIZE_T bytesWritten;
    BOOL result = WriteProcessMemory(hProcess, addressToWrite, &value, sizeof(value), &bytesWritten);
}


