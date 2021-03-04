#include <iostream>
using namespace std;
int main()
{
    int a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;
    if (a > b){
        a += b;
        b = a - b;
        a -= b;
    }
    if (b > c){
        b += c;
        c = b - c;
        b -= c;
    }
    if (a > c){
        a += b;
        b = a - b;
        a -= b;
    }
    cout << a << " " << b << " " << c;
    return 0;
}
