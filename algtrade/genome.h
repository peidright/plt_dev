#ifndef GENOME_H_
#define GENOME_H_
#include <stdint.h>
#include "op.h"

typedef struct genome_meta{
    uint8_t genes[10];
    uint8_t cases[10];
    uint8_t envids[3];
    uint8_t gnum;
}genome_meta_t;

typedef struct genome_op
{
        init_func      init;
        clear_func     clear;
        output_func    output; 
        mutation_func  mutation;
        crossover_func crossover;
        copy_func      copy;
}genome_op_t;

#endif
