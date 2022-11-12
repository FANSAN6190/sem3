/*3. Write a menu driven program to delete the node from the beginning, from specified position and from the end of linked list.*/
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include <iostream>
using namespace std;
struct node{
    int info;
    node *next;
};
node *delete_at_end(node *start, node *newnode);
node *delete_at_beginning(node *start){
    start = start->next;
    return start;
}
node *delete_at_loc(node *start,int i){
    node *temp = start;
    if(i==1){
        start=delete_at_beginning(start);
    }
    else if(start!=NULL){
        i=i-2;
        while (--i){
            temp = temp->next;
        }
        temp->next = temp->next->next;
        delete temp;
        return start;
    }
    return start;
}
node *delete_at_end(node *start){
    node *temp = start;
    if (start == NULL){return start;}
    else{
        while (temp->next->next != NULL){
            temp = temp->next;
        }   
        temp->next = NULL;               
    }
    delete temp;
    return start;
}
void display(node *start){
    node *temp = start;
    while (temp != NULL){
        cout << temp->info << endl;
        temp = temp->next;
    }
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
    int del_at;
    cout << "delete at Beginning : 1\ndelete at Specific Position: 2\ndelete at End : 3 " << endl;
    while (true){
        cout<<"-------------"<<endl;
        display(start);
        cout<<"-------------"<<endl;
        cout << "Choose one of the option : ";
        cin >> del_at;
        if (del_at == 0){break;}
        switch (del_at){
        case 1:
            start = delete_at_beginning(start);
            break;
        case 2:
            int i;
            cout << "Enter the location = ";
            cin >> i;
            start = delete_at_loc(start,i - 1);
            break;
        case 3:
            start = delete_at_end(start);
            break;
        default:
            cout << "Wrong Input";
            break;
        }
    }
}