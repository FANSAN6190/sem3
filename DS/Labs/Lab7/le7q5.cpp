//5.WAP to search an element in the linked list
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
using namespace std;
struct node{
        int data;
        node *next;
};
int search(node * start, int e){
    int loc=1;
    node * temp=start;
    while(temp->data!=e){
        temp=temp->next;
        loc++;
    }
    return loc;
}
void display(node * start){
    node *tem=start;
    while (tem->next!=NULL){
        cout<<tem->data<<endl;
        tem=tem->next;
    }
    cout<<tem->data<<endl;
    delete tem;
}
int main(){
    node *start;
    node *node1;
    node *node2;
    node *node3;
    start=node1;
    node1->next=node2;
    node2->next=node3;
    node3->next=NULL;
    node1->data=10;
    node2->data=20;
    node3->data=30;
    int e;
    cin>>e;
    int loc=search(start,e);
    cout<<e<<endl;
}
