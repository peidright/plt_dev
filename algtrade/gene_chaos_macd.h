#ifndef GENE_CHAOS_MACD_H_
#define GENE_CHAOS_MACD_H_
#include <stdint.h>

void init_func_macd(void *data);
void clear_func_macd(void *data);
uint8_t  output_func_macd(void *data);
bool mutation_func_macd(void *,void *data);
bool crossover_func_macd(void *g1,void *g2, void **g3, void **g4);
void copy_func_macd(void *data);

#endif
