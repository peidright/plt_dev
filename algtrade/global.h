#ifndef GLOBAL_H_
#define GLOBAL_H_
#include "gene.h"
#include "genome.h"
#include "population.h"
#include "container.h"
#include "gene_chaos.h"

extern container<gene_op_t> g_gene_op_pool;
extern container<gene_meta_t> g_gene_meta_pool;

extern container<genome_op_t> g_genome_op_pool;
extern container<genome_meta_t> g_genome_meta_pool;

extern container<population_meta_t> g_population_meta_pool;
extern container<gene_data_t> g_gene_data_pool;
extern populations_t g_populations;
#endif
