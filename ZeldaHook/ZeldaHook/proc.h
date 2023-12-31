#pragma once
#include <vector>
#include <Windows.h>
#include <TlHelp32.h>
#pragma comment(lib, "Ws2_32.lib")

DWORD GetProcID(const wchar_t* procName);

uintptr_t GetModuleBaseAddress(DWORD procId, const wchar_t* modName);

uintptr_t FindDMAAddy(HANDLE hProc, uintptr_t ptr, std::vector<unsigned int> offsets);