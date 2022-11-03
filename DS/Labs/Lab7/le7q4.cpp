/*4.WAP to reverse the singly linked list.*/
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
using namespace std;
struct node{
        int info;
        node *next;
};
node *reverse(node * start){
        node* curr = start;
        node *prev = NULL, *next = NULL;
        while (curr != NULL) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        start = prev;
    }
void display(node * start){
    node *temp=start;
    while (temp->next!=NULL){
        cout<<temp->info<<endl;
        temp=temp->next;
    }
    cout<<temp->info<<endl;
    delete temp;
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
    node1->info=10;
    node2->info=20;
    node3->info=30;
    start=reverse(start);
    display(start);
}
