#ifndef GENE_CHAOS_TICK1_H_
#define GENE_CHAOS_TICK1_H_

void* init_func_tick1(void *data,void *config);
void clear_func_tick1(void *data);
uint8_t  output_func_tick1(void *data);
bool mutation_func_tick1(void *,void **data);
bool crossover_func_tick1(void *g1,void *g2, void **g3, void **g4);
void* copy_func_tick1(void *data);

#endif
