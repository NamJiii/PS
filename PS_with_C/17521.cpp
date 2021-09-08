#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

long long N;
long long dollar;
long long btc;
bool sell_pos = false;//0 is short, 1 is long
long long price;
long long prev_price;

int main(){

    scanf("%lld %lld",&N,&dollar);
    scanf("%lld",&price);

    for(int i = 1; i<N;i++){
        prev_price = price;
        scanf("%lld",&price);

        if(!sell_pos & price > prev_price){//GAZUAA!!
            btc = dollar/prev_price;
            dollar = dollar - btc*prev_price;
            sell_pos = true;
        }
        else if(sell_pos & price < prev_price){//DOMHWANGCHA!!
            dollar = dollar + btc*prev_price;
            btc = 0;
            sell_pos = false;
        }
        else{//HOLD
            continue;
        }
    }

    dollar = dollar + btc*price;
    printf("%lld",dollar);
    return 0;
}