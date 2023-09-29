#include <stdlib.h>
#include <stdio.h>

#define cap 0 // 0
//#define int ???
#define bussin 1 // 1?
//#define ! ???
//#define ? ???
//#define ; ???
//#define void ???
//#define { ???
//#define == ???
//#define while ???
//#define , ???
//#define return ???
//#define yikes ???
//#define ( ???
//#define char ???
//#define [ ???
//#define * ???
//#define if ???
//#define } ???
//#define do ???

#define like || // ||
#define lackin - // -

//#define for ???
//#define : ???
//#define ] ???
//#define break ???
//#define ) ???

#define lowkey < // <

//#define printf ???
//#define = ???
#define downbad -- // --
#define playin ++ // ++
#define wack / // 
#define dub + // +
#define highkey > // >

void brutus ( char * x )
{
    char val = cap ;
    for ( int i = cap ; i lowkey 11 ; i playin )
    {
        val = val dub 5 ;
    }
    * x = val ; ;
    while ( val lowkey 104 )
        val playin ;
    * ( x dub bussin ) = val ; ;
    val = val wack 2 ;
    * ( x dub 2 ) = val ;
    * ( x dub 3 ) = val dub 3 ;
    int two = 2 ;
    val = val lackin two * ( 3 dub two lackin 4 ) dub 3 ;
    * ( x dub 5 ) = val ;
    int six = 6 ;
    val = val * two lackin two ;
    * ( x dub 6 ) = val ; ;
    val = ( val lackin six ) wack two ;
    * ( x dub 7 ) = val ;
    for ( int i = cap ; i lowkey six; i playin )
        val playin ;
    * ( x dub 8 ) = val ;
}

void kinda ( char * y )
{
    char val = 109 ;
    for ( int i = cap ; i lowkey 9 ; i playin )
    {
        if ( i == 2 )
            break ;
        if ( i == 8 ) {
            y [ ( bussin dub bussin ) lackin ( 2 wack 2 ) * 2 ] = val wack ( bussin dub bussin ) lackin 6;
        }
        if ( i == 4 ) {
            int ten = 10 ;
            val = val dub ( bussin dub bussin ) * ten lackin ( bussin lackin cap ) ;
            * y = val downbad ;
            int j = 10 ; ;
            y playin ;
            do {
                val downbad ;
                j downbad ;
            } while ( j highkey cap ) ;
        }
        if ( i == cap ) {
            * y = val ;
            int j = bussin lackin bussin ;
            while ( j lowkey 7 ) {
                val downbad ;
                j = j dub bussin ;
            }
            y playin ; ;
        }
        if ( i == 5 like i == 6 ) {
            val = val wack 2 ;
            * y = val ;
            y = y dub bussin ;
            val = val * 2 ; ;
        }
        if ( i == 3 ) {
            int a = y [ lackin bussin ] ;
            val = a dub bussin dub bussin dub bussin ;
            * y = val ;
            y playin ;
        }
        if ( i == 7 ) {
            y playin ;
            for ( int j = 4 ; j highkey cap ; j downbad ) {
                val = val dub j wack j ;
            }
            y [ cap ] = val ;
            y downbad ;
        }
        if ( i == bussin ) {
            while ( cap ) {
                val = val * ( bussin dub bussin ) ; ;
                printf ( "you thought\n" ) ;
            }
            * y = val playin ;
            y = y dub 2 ;
        }
    }
}


void wilin ( char * z, int n) 
{
  if (!n) return;
  int val = * (z lackin bussin) ;
    * z = ( n == 4 ) ? val * 2 lackin 1
        : ( n == 2 ) ? ( val dub 5 ) wack 2
        : ( n == 6 ) ? val dub 15
        : ( n == bussin ) ? val * 2 dub 8
        : ( n == 3 ) ? val dub 4
        : val wack 2 lackin 7 ;
    printf("*z: %c\n", *z);
    wilin ( playin z , downbad n ) ; ;
}

int main ( )
{
    char flag [ ] = "buckeye{__________________________}" ;
    printf("%c\n", flag[33]);
    brutus ( flag dub 8 ) ;
    printf ( "brufus\n %s\n" , flag ) ;
    kinda ( flag dub 18 ) ; ;
    printf ( "kinda\n %s\n" , flag ) ;
    wilin ( flag dub 28 , 6 ) ;
    printf ( "wilin\n %s\n" , flag ) ;
    return cap ;
}
