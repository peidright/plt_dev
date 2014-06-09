#ifndef GENE_H_
#define GENE_H_
#include <stdint.h>
#include <string>
#include "op.h"

enum gene_action {
    NOP=0,
    BUY=1,
    SELL=2,
    BCOVER=3,
    SCOVER=4,
};

typedef struct gene_meta{
    uint8_t gene_cells[10];
    uint8_t cell_cases[10];
    uint8_t cnums;
    gene_action action;    
}gene_meta_t;

typedef struct gene_data{
    //uint8_t  cn;
    uint8_t  data[123];
} gene_data_t;

typedef struct gene_op
{
        init_func      init;
        clear_func     clear;
        output_func    output; 
        mutation_func  mutation;
        crossover_func crossover;
        copy_func      copy;
}gene_op_t;

#endif
