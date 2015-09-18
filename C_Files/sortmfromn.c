//
//  sort.c
//  
//
//  Created by Xiaosheng Wu on 9/18/15.
//
//

#include "sort.h"
#include <stdio.h>
#include <stdlib.h>
int n = 1;

void swap(int *a, int *b)
{
    int m;
    m = *a;
    *a = *b;
    *b = m;
}

void perm(int list[], int k, int m)
{
    int i;
    if (k>m)
    {
        for (i=0; i<=m; i++)
            printf("%d\t",list[i]);
        printf("%d",n);
        printf("\n");
        n++;
    }
    else {
        for (i = k; i<=m; i++) {
            swap(&list[k], &list[i]);
            perm(list,k+1,m);
            swap(&list[k], &list[i]);
        }
        
    }
}

int main(){
    int list[] = [1,2,3,4,5];
    perm(list,0,2);
    return 0;
}
