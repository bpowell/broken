#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char *msg;
    msg = (char *)malloc(sizeof(char)*5);
    strcpy(msg, "1234");

    printf("MSG: %s\n", msg);

    free(msg);

    printf("MSG: %s\n", msg);

    return 0;
}
