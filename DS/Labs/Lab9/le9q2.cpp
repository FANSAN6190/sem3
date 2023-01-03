/*2. Write a menu-driven program to implement Stack using linked list with
     following options: 1.Push 2.Pop 3.Display 4.Exit*/
#include<iostream>
using namespace std;
class node{
    public:
    int data;
    node *next;
};
class Stack{
    public:
    node *top;
    Stack(){top=NULL; }
    void push(int ele){
        node *newnode=new node();
        newnode->data=ele;
        newnode->next=top;
        top=newnode; }
    int pop(){
        node *temp=top;
        if(top==NULL){
            cout<<"Stack underflow"<<endl;
            return -1; }
        else{
            int rem=top->data;
            top=top->next;
            return rem; }
    }
    void display(){
        node *temp=top;
        while(temp!=NULL){
            cout<<temp->data<<" ";
            temp=temp->next; }
        cout<<endl; }
};
int main(){
    int choice;
    node *start;
    //start->next=NULL;
    Stack stk;
    while(choice!=4){
        cout<<"***Stack Menu***\n1. Push\n2. Pop\n3. Display\n4. Exit"<<endl;
        cout<<"Enter your choice(1-4): ";
        cin>>choice;
        cout<<"****************"<<endl;
        int ele;
        switch(choice){
        case 1:
            cout<<"Enter element to push : ";
            cin>>ele;
            stk.push(ele);
            break;
        case 2:
            ele=stk.pop();
            cout<<"Deleted element is "<<ele<<endl;
            break;
        case 3:
            stk.display();
            break;
        case 4:
            exit(0);
            break;
        default:
            cout<<"Invalid Input, Try Again"<<endl;
            break;
        }
    }
}


/*2. Write a menu-driven program to implement Stack using linked list with
     following options: 1.Push 2.Pop 3.Display 4.Exit*/
/*#include<iostream>
using namespace std;
class node{
    public:
    //int data;
    char chr;
    node *next;
};
class Stack{
    public:
    node *top;
    Stack(){
        top=NULL;
    }
    void push(char ch){
        node *newnode=new node();
        //newnode->data=ele;
        newnode->chr=ch;
        newnode->next=top;
        top=newnode;
    }
    char pop(){
        node *temp=top;
        if(top==NULL){
            cout<<"Stack underflow"<<endl;
            return -1;
        }
        else{
            char rem=top->chr;
            top=top->next;
            return rem;
        }
    }
    void display(){
        node *temp=top;
        while(temp!=NULL){
            cout<<temp->chr<<" ";
            temp=temp->next;
        }
        cout<<endl;
    }
};
int main(){
    int choice;
    node *start;
    //start->next=NULL;
    Stack stk;
    while(choice!=4){
        cout<<"***Stack Menu***\n1. Push\n2. Pop\n3. Display\n4. Exit"<<endl;
        cout<<"Enter your choice(1-4): ";
        cin>>choice;
        cout<<"****************"<<endl;
        int ele,ch;
        switch(choice){
        case 1:
            cout<<"Enter element to push : ";
            cin>>ch;
            cin.ignore(ch,10);
            //cin.clear();
            stk.push(ch);
            break;
        case 2:
            ch=stk.pop();
            cout<<"Deleted element is "<<ch<<endl;
            break;
        case 3:
            stk.display();
            break;
        case 4:
            exit(0);
            break;
        default:
            cout<<"Invalid Input, Try Again"<<endl;
            break;
        }
    }
    return 0;
}*/