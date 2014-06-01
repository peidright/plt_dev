#ifndef CONTAINER_H_
#define CONTAINER_H_
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

template<typename T>
class container
{
    public:
        typedef int (*call_back)(T* item,void *arg);
        container(int total);
        int put(T item);
        T*  get(int idx);
        int clr(int idx);
        int size();
        int iterator(call_back func);

    private:
        char *bits;
        T    *arrs;
        int total;
        int csize;
        int cidx;
};
template<typename T>
container<T>::container(int total)
{
    this->total=((total+8)/8)*8;
    this->bits=new char[this->total/8];
    this->arrs=new T[this->total];
    this->csize=0;
    this->cidx=0;
    memset(bits,0x0,this->total/8);
}

template<typename T>
T* container<T>::get(int idx)
{
    if(idx >= this->total) {
        return NULL;
    }
    if(idx < 0) {
        for(int i=(this->cidx/8); i<(this->total/8);i++) {
            if(this->bits[i]!=0xFF) {
                for(int j=7;j>=0;j--) {
                    if(!(this->bits[i] & (1<<j))) {
                        this->bits[i] | (1<<j);
                        this->cidx=i*8+7-j;
                        this->csize++;
                        return &this->arrs[this->cidx];
                    }
                }
            }
        }
        for(int i=0;i< (this->cidx/8+1);i++) {
            if(this->bits[i]!=0xFF) {
                for(int j=7;j>=0;j--) {
                    if(!(this->bits[i] & (1<<j))) {
                        this->bits[i] | (1<<j);
                        this->cidx=i*8+7-j;
                        this->csize++;
                        return &this->arrs[this->cidx];
                    }
                }
            }
        }

    }else {
        return &this->arrs[idx];
    }
    /*
    if(this->bits[idx/8] & (1<<(7-idx%8))) {
        return &this->arrs[idx];
    }else {
        return NULL;
    }
    */
    return NULL;
}

template<typename T>
int container<T>::put(T item)
{
    for(int i=(this->cidx/8); i<(this->total/8);i++) {
        if(this->bits[i]!=0xFF) {
            for(int j=7;j>=0;j--) {
                if(!(this->bits[i] & (1<<j))) {
                    this->bits[i] | (1<<j);
                    this->cidx=i*8+7-j;
                    this->csize++;
                    this->arrs[this->cidx]=item;

                    return this->cidx;
                }
            }
        }
    }
    for(int i=0;i< (this->cidx/8+1);i++) {
        if(this->bits[i]!=0xFF) {
            for(int j=7;j>=0;j--) {
                if(!(this->bits[i] & (1<<j))) {
                    this->bits[i] | (1<<j);
                    this->cidx=i*8+7-j;
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
int container<T>::clr(int idx)
{
    if(idx >= this->total) {
        return -1;
    }
    if(this->bits[idx/8] & (1<<(7-idx%8))) {
        memset(&this->arrs[idx],0x0, sizeof(T));
        this->bits[idx/8]=this->bits[idx/8] & (~(1<<(7-idx%8)));
    } else {
        return -1;
    }
    return 0;
}

template<typename T>
int container<T>::size()
{
    return this->csize;
}

template<typename T>
int container<T>::iterator(call_back func)
{
    for(int i=0;i<this->total;i++) {
        if(this->bits[i/8] & (1<<(7-i%8))) {
            func(&this->arrs[i],NULL);
        }else {

        }
    }
    return 0;
}
#endif
