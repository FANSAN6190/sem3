#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i,f,r;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }
    r=num-1;
    for(i=0;i<=num/2 && r>=num/2;i++,r--){
        f=*(arr+i);
        *(arr+i)=*(arr+r);
        *(arr+r)=f;
    }
    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}