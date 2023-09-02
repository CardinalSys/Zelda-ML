#include <iostream>
#include "proc.h"


uintptr_t moduleBase;
HANDLE hProcess;

void HookEmulator();

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
        moduleBase = GetModuleBaseAddress(procId, L"Mesen.exe");
        //Get handle to process
        hProcess = OpenProcess(PROCESS_ALL_ACCESS, NULL, procId);

        std::cout << hProcess;
    }
}
