#ifndef GENOME_H_
#define GENOME_H_
#include <stdint.h>
#include "op.h"

typedef struct genome_meta{
    uint8_t  *gene_cell_feas;
    uint8_t   gene_cells[10];
    uint16_t  cell_num;
    uint16_t  gene_num;
} genome_meta_t;

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
