#ifndef GENE_H_
#define GENE_H_
#include <stdint.h>
#include <string>
#include "op.h"

enum action{
    BUY,
    SELL,
    BCOVER,
    SCOVER,
};

using namespace std;
typedef struct gene_meta{
    uint8_t  oid;
    int16_t did;
    uint8_t  cn:4;
    uint8_t  c:4;
} gene_meta_t;

typedef struct gene_object{
    action act;
}gene_object_t;

typedef struct gene_data{
    gene_object_t gene_object;
    uint8_t  cn;
    uint8_t  data[123];
} gene_data_t;

typedef struct gene_op{
        char name[32];
        init_func      init;
        clear_func     clear;
        output_func    output; 
        mutation_func  mutation;
        crossover_func crossover;
        copy_func      copy;
}gene_op_t;
#endif
