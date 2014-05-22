#ifndef FEA_H_
#define FEA_H_
#include <string>
using namespace std;
class fea{
    public:
    fea(int type, int key);
    string update(void *data);
    int get_key();
    int key;
    string get_val();
};

#endif


