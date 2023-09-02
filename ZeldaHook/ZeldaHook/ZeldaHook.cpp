#include <iostream>
#include <stdlib.h>
#include "proc.h"


uintptr_t moduleBase;
HANDLE hProcess;
uintptr_t baseAddress;

void HookEmulator();
void GetVariables();


//Variables
BYTE playerXPos = 0;
BYTE playerYPos = 0;
BYTE playerDir = 0;

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
    std::vector<unsigned int> playerXposOffsets = {0xB8, 0x78, 0x70};
    uintptr_t playerXposAddress = FindDMAAddy(hProcess, baseAddress, playerXposOffsets);
    ReadProcessMemory(hProcess, (BYTE*)playerXposAddress, &playerXPos, sizeof(char), nullptr);

    std::vector<unsigned int> playerYposOffsets = { 0xB8, 0x78, 0x84 };
    uintptr_t playerYposAddress = FindDMAAddy(hProcess, baseAddress, playerYposOffsets);
    ReadProcessMemory(hProcess, (BYTE*)playerYposAddress, &playerYPos, sizeof(char), nullptr);

    std::vector<unsigned int> playerDirOffsets = { 0xB8, 0x78, 0x98 };
    uintptr_t playerDirAddress = FindDMAAddy(hProcess, baseAddress, playerDirOffsets);
    ReadProcessMemory(hProcess, (BYTE*)playerDirAddress, &playerDir, sizeof(char), nullptr);

    std::cout << (int)playerDir << "\n";
}
