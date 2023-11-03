#include "stdio.h"

int main() {
    int x ;
    int y;
    int max;
    scanf("%i %i",&x,&y);
    if (x > y) {
        max = x;
    } else if (x < y) {
        max = y;
    } else {
        printf("Numbers are equal");
    }
}
