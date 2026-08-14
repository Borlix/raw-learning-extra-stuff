#include<iostream>
using namespace std;
int main(){
    int num , n=1;
    cout<<"Enter a num : ";
    cin>>num ;

    for(int i =0;i<num;i++){
        for(int j=1;j<=num;j++){
            cout<<n<<" ";
            n++;
        }
        cout<<endl;
    }
    return 0;
}