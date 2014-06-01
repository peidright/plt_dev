#include <stdint.h>
#include <assert.h>
#include "gene.h";
#include "gene_chaos_tick1.h"
#include "gene_chaos.h"

/*
 * tick 1 make sure is up, or is down, check period tick
 * arg period, level 0-7
 * */
typedef struct tick1_data{
        uint8_t  env_id;
        uint8_t  level;  
        uint16_t  period;
} tick1_data_t;

void* init_func_tick1(void *data,void *config)
{
    gene_meta_t *gene_meta=(gene_meta_t*)data;
    gene_op_t   gene_op;
    if(gene_meta) {
        gene_meta->cn=2;
    }
    return NULL;
err:
    assert(0);
}

void clear_func_tick1(void *data)
{
}
uint8_t  output_func_tick1(void *data)
{
}
bool mutation_func_tick1(void *,void **data)
{
}
bool crossover_func_tick1(void *g1,void *g2, void **g3, void **g4)
{
}
void* copy_func_tick1(void *data)
{
}

