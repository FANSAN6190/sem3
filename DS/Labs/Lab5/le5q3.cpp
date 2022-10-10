/*3.Write  a  program  to  check whether given  Matrix  is  sparse  or  not.  We  say  a  matrix  as sparse when more 
than 50% of total elements are zero. If matrix is sparse then represent it in triplet form with the help of array data 
structure. Also print the number of bytes that are saved or wasted when you representinput matrix in the triplet form*/
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
    if(z>6*6/2){
        cout<<"This matrix is a Sparse Matrix."<<endl;
    }
    else{
        cout<<"This is not a Sparse Matrix."<<endl;
    }
    for (int i = 0; i<k; i++){
        for (int j = 0; j < 3; j++){
            cout<<trip[i][j]<<" ";
        }
        cout<<endl; 
    }
    cout<<"Memory Saved = "<<(6*6)-(3*k)<<" Bytes."<<endl;
}