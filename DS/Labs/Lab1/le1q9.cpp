//9.WAP to concatenate two strings using pointer.
#include<iostream>
#include<string.h>
using namespace std;
int main(){
    string *s1;//=new string();
    string *s2;//=new string();
    string *s3;
    getline(cin,*s1);
    getline(cin,*s2);
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