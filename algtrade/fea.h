#ifndef FEA_H_
#define FEA_H_
#include <string>
using namespace std;
class fea{
    public:
        int i;
};
#if 0

typedef struct gene{
    uint8_t  oid;
    uint16_t did;
    uint8_t  pad;
} gene_meta_t;
typedef struct genome_meta{
    uint8_t genes[10];
}genome_meta_t;
typedef struct population_meta {
    uint16_t genomes[65536]
} population_meta_t;
struct populations {
    uint8_t  populations[256];
};
struct gene_op{
};
struct genome_op
{
};
struct population_op {
};
struct populations_op{
};

template<typename T>
class container
{
    public:
        container(int size);
        int put_item(T *);
        T*  get_item(int idx);
        int clr_item(int idx);
    private:
        char *bits;
        T    *arrs;
        int size;
};
template<typename T>
container<T>::container(int size)
{
    this->size=((size+8)/8)*8;
    this->bits=new char[this->size/8];
    this->arrs=new T[this->size];
    this->csize=0;
    this->cidx=0;
    memset(bits,0x0,this->size/8);
}

template<typename T>
T* container<T>::get_item(int idx)
{
    if(idx > this->size) {
        return NULL;
    }
    if(this->bits[idx/8] & (1<<(idx%8+1))) {
        return this->array[idx];
    }else {
        return NULL;
    }
    return NULL;
}

template<typename T>
int container<T>::put_item(T item)
{
    for(int i=(this->cidx/8); i<(this->size/8);i++) {
        if(this->bits[i]!=0xFF) {
            for(int j=1;i<=8;j++) {
                if(!(this->bits[0] & (1<<j))) {
                    this->cidx=i*8+j-1;
                    this->csize++;
                    this->arrs[this->cidx]=item;
                    return this->cidx;
                }
            }
        }
    }
    for(int i=0;i< (this->cidx/8+1);i++) {
        if(this->bits[i]!=0xFF) {
            for(int j=1;i<=8;j++) {
                if(!(this->bits[0] & (1<<j))) {
                    this->cidx=i*8+j-1;
                    this->csize++;
                    this->arrs[this->cidx]=item;
                    return this->cidx;
                }
            }
        }
    }
    return -1;
}

template<typename T>
int container<T>::clr_item(T item)
{
}
#endif
#endif
