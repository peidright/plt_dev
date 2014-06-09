#include <stdint.h>
#include <unistd.h>
#include "gene.h"
#include "gene_chaos_tick3.h"
#include "gene_chaos.h"


void* init_func_tick3(void *data,void *config)
{
    gene_cell_meta_t *gene_cell_meta=(gene_cell_meta_t*)data;
    gene_cell_meta->cn=5;
    return NULL;
}
void clear_func_tick3(void *data)
{
}
uint8_t  output_func_tick3(void *data)
{
    return 0;
}
bool mutation_func_tick3(void *,void **data)
{
    return true;
}
bool crossover_func_tick3(void *g1,void *g2, void **g3, void **g4)
{
    return true;
}
void* copy_func_tick3(void *data)
{
    return NULL;
}
