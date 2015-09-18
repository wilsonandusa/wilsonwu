//
//  MacStartTime.c
//  
//
//  Created by Xiaosheng Wu on 9/18/15.
//
//

#include "MacStartTime.h"
#include <time.h>
#include<windows.h>
#include<stdlib.h>
#include <stdio.h>

void sleep( long wait );
void gettime();

int main( void )
{
    int flag=1;
    char time[128];
    //ªÒ»°œµÕ≥µ±«∞ ±º‰
    _strtime(time);
    printf( "OS time:%s\n",time);
    //printf( "Delay for one seconds\n" );
    //	do
    //	{
    //		gettime();
    //		sleep( 1000 );
    //	}while(flag);
    printf("“—ø™ª˙ ±º‰:");
    gettime();
    system("pause");
    return 0;
}

void sleep( long wait )
{
    long goal;
    goal = wait + clock();
    while( goal > clock() );
}

void gettime()
{
    int i=GetTickCount();
    int h=(i/1000)/3600;
    int m=(i/1000)/60-h*60;
    int s=(i/1000)-h*3600-m*60;
    printf("%d–° ±%d∑÷%d√Î\n",h,m,s);
    
}