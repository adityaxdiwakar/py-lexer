#include "stdio.h"

int main() {
    int x;
    int y;
    int max;
    scanf("%d %d",&x,&y);
    if (x > y) {
        max = x;
    } else {
        max = y;
    }
    printf("%d",max);
}
