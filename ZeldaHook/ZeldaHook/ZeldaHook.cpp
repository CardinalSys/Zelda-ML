#include <iostream>
#include <stdlib.h>
#include "proc.h"


uintptr_t moduleBase;
HANDLE hProcess;
uintptr_t baseAddress;

void HookEmulator();
void GetVariables();
char ReadMemory(std::vector<unsigned int> offsets);


//Variables

//Varialbes-Player
BYTE playerXPos = 0;
BYTE playerYPos = 0;
BYTE playerDir = 0;
BYTE playerMapLocation = 0;

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

BYTE enemy1xProlectil = 0;
BYTE enemy2xProlectil = 0;
BYTE enemy3xProlectil = 0;
BYTE enemy4xProlectil = 0;

BYTE enemy1yProlectil = 0;
BYTE enemy2yProlectil = 0;
BYTE enemy3yProlectil = 0;
BYTE enemy4yProlectil = 0;

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
            Sleep(100);
        }
        
    }
}

void GetVariables()
{
    //Player
    playerXPos = ReadMemory({ 0xB8, 0x78, 0x70 });  
    playerYPos = ReadMemory({ 0xB8, 0x78, 0x84 });
    playerDir = ReadMemory({ 0xB8, 0x78, 0x98 });
    playerMapLocation = ReadMemory({ 0xB8, 0x78, 0xEB });
    

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

}

char ReadMemory(std::vector<unsigned int> offsets) {
    uintptr_t address = FindDMAAddy(hProcess, baseAddress, offsets);
    char value;
    ReadProcessMemory(hProcess, (BYTE*)address, &value, sizeof(value), nullptr);
    return value;
}
