#include<iostream>
using namespace std;
int main(){
    int num = 4 ;
    char Latter = 'A' ;

    for(int i =0;i<num;i++){
        for(int j=1;j<=num;j++){
            cout<< Latter <<" ";
            Latter++;
        }
        cout<<endl;
    }
    return 0;
}