/*Write a function Insert_Beginning() to insert a new node at the beginning of
singly linked list. Call this function N time to create a linked list with N nodes.
Also write display function to print the linked list.*/
#include<iostream>
using namespace std;
struct node{
        int data;
        node *next;
};
int insert_Beginning(node * start, node * newnode){
    if(start==NULL){
        start=newnode;
        newnode->next=NULL;
        return 0;
    }
    newnode->next=start;
    start=newnode;
    return 0;
}
void display(node * start){
    node *tem=start;
    while (tem->next!=NULL){
        cout<<tem->data<<endl;
        tem=tem->next;
    }
    cout<<tem->data<<endl;
}
int main(){
    node * start=NULL;
    /*node * nOne=new node();
    node * nTwo=new node();
    node * nThree=new node();
    start=nOne;
    nOne->next=nTwo;
    nTwo->next=nThree;
    nThree->next=NULL;

    nOne->data=1;
    nTwo->data=2;
    nThree->data=3;*/
    
    int n,i=1;
    //cin>>n;
    n=5;
    while(n--){
        node * newnode=new node();
        newnode->data=i;
        insert_Beginning(start,newnode);
        i++;
    } 
    display(start);
}
