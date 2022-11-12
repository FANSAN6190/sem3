//9.WAP to concatenate two strings using pointer.
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
#include<string.h>
using namespace std;
int main(){
    char *s1;//=new string();
    char *s2;//=new string();
    char *s3;
    cin>>s1;
    cin>>s2;
    cout<<s1<<"    "<<s2<<endl;
    for(int i=0,j=0;s3[i]!='\0';i++){
        if(s1[i]!='\0'){s3[i]=s1[i];}
        else{
            s3[i]=s2[j];
            j++;
        }
    }
    cout<<"New string = "<<s3<<endl;
    return 0;
}