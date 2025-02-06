#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <windows.h>
#include <time.h>

#pragma comment(lib, "ws2_32.lib")

#define DESKTOP_PATH "C:\\Users\\%USERNAME%\\Desktop\\"
#define NUM_FILES 5
#define NUM_IPS 3
#define NUM_REG_KEYS 5

const char *ips[NUM_IPS] = {"100.100.100.100", "200.200.200.200", "150.150.150.150"};

void generate_random_name(char *buffer, int length) {
    static const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    for (int i = 0; i < length; i++) {
        buffer[i] = charset[rand() % (sizeof(charset) - 1)];
    }
    buffer[length] = '\0';
}

void create_random_files() {
    char filepath[MAX_PATH], filename[12];
    for (int i = 0; i < NUM_FILES; i++) {
        generate_random_name(filename, 8);
        snprintf(filepath, sizeof(filepath), DESKTOP_PATH "%s.exe", filename);
        
        FILE *file = fopen(filepath, "w");
        if (file) {
            fprintf(file, "This is a test EXE file\n");
            fclose(file);
        }
    }
}

void modify_registry() {
    HKEY hKey;
    char reg_path[50];

    for (int i = 0; i < NUM_REG_KEYS; i++) {
        snprintf(reg_path, sizeof(reg_path), "Software\\RandomKey_%d", rand() % 1000);
        
        if (RegCreateKeyEx(HKEY_CURRENT_USER, reg_path, 0, NULL, REG_OPTION_NON_VOLATILE, KEY_ALL_ACCESS, NULL, &hKey, NULL) == ERROR_SUCCESS) {
            char data[20];
            generate_random_name(data, 10);
            RegSetValueEx(hKey, "TestValue", 0, REG_SZ, (const BYTE *)data, strlen(data) + 1);
            RegCloseKey(hKey);
        }
    }
}

void connect_to_ips() {
    WSADATA wsa;
    SOCKET s;
    struct sockaddr_in server;
    
    WSAStartup(MAKEWORD(2,2), &wsa);
    
    for (int i = 0; i < NUM_IPS; i++) {
        s = socket(AF_INET, SOCK_STREAM, 0);
        if (s == INVALID_SOCKET) {
            continue;
        }

        server.sin_addr.s_addr = inet_addr(ips[i]);
        server.sin_family = AF_INET;
        server.sin_port = htons(80);

        connect(s, (struct sockaddr *)&server, sizeof(server));
        closesocket(s);
    }
    
    WSACleanup();
}

int main() {
    srand(time(NULL));
    create_random_files();
    modify_registry();
    connect_to_ips();
    return 0;
}
