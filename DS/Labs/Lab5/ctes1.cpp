#include<iostream>
using namespace std;
int main(){
    int k=0,z=0,arr[6][6]={{15,0,0,22,0,-15},
                       {0,11,3,0,0,0},
                       {0,0,0,-6,0,0},
                       {0,0,0,0,0,0},
                       {91,0,0,0,0,0},
                       {0,0,28,0,0,0}};
    int **trip=new int *[3];
    for(int i=0;i<6;i++){
        for(int j=0;j<6;j++){
            if (arr[i][j]==0){
                z++;
            }
            else{
                trip[k]=new int(1);
                trip[k][0]=i;                
                trip[k][1]=j;
                trip[k][2]=arr[i][j];
                k++;
            }
        }
    }
    for (int i = 0; i<k; i++){
        for (int j = 0; j < 3; j++){
            cout<<trip[i][j]<<" ";
        }
        cout<<'\n'; 
    }
    cout<<z<<endl;
}
