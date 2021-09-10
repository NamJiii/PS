#include<stdio.h>
#include<vector>
#include<iostream>
#include<stdlib.h>//abs
using namespace std;
//한쪽 방향으로 냅다 뛰어라.. 그게 최고다

bool up_ = true;
bool right_ = true;
bool left_ = true;
bool down_ = true;
int police_x[500001];
int police_y[500001];
int N;
int thief_x;
int thief_y;
int lives = 4;

int main(){
    scanf("%d",&N);
    for(int i = 0; i<N;i++){
        scanf("%d %d",&police_x[i],&police_y[i]);
    }
    scanf("%d %d",&thief_x,&thief_y);

    for(int i = 0; i < N ; i++ ){
        if(up_){
            if(police_y[i]-thief_y-abs(police_x[i]-thief_x)>=0){
                up_ = false;
                lives--;
            }
        }
        if(down_){
            if(police_y[i]-thief_y+abs(police_x[i]-thief_x)<=0){
                down_ = false;
                lives--;
            }
        }
        if(right_){
            if(police_x[i]-thief_x-abs(police_y[i]-thief_y)>=0){
                right_ = false;
                lives--;
            }
        }
        if(left_){
            if(police_x[i]-thief_x+abs(police_y[i]-thief_y)<=0){
                left_ = false;
                lives--;
            }
        }
        if(!lives){
            printf("NO");
            return 0;
        } 
    }
    printf("YES");
    return 0;
}
