#include <iostream>
#include <stdlib.h>

class Leak
{
public:
    int *pNum;
    Leak();
    Leak(int n)
    {
       leak(n);
    }
    int leak(int n) {
        if(n > 0)  {
            pNum = (int*)malloc(sizeof(int));
            *pNum = n;
        }
        else
            return 0;
    }
};

int main() {
    int num = 0;

    std::cin >> num;
    Leak *lk = new Leak(num);
}