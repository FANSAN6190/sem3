//6. WAP to find the reverse of given string.
#include<iostream>
#include<cstring>
//#include<conio.h>
using namespace std;
int main(){
	char s1[]="hello123";
	cout<<s1<<endl;
	int l=strlen(s1);
	cout<<l;
	char s2[l];
	for(int i=0;l!=0;i++){
		l--;
		s2[i]=s1[l-1];
	}
	cout<<s2<<endl;
//	getch();
	return 0;	
}
