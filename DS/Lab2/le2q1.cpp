//1. WAP to generate a Fibonacci series up to n terms.
  #include<iostream>
  using namespace std;
  int main(){
      int a=0,b=1,n;
      cout<<"Enter the number = ";
      cin>>n;
      cout<<a<<" "<<b;
      for(int i=2;i<n;i++){
          b=a+b;
          a=b-a;
          cout<<" "<<b;
        }
      return 0;
    }
