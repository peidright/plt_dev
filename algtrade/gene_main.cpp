#include "gene.h"
#include "genome.h"
#include "population.h"
#include "container.h"
#include "global.h"
#include "log.h"
/*
container<gene_op_t> g_gene_op_pool(256);
container<gene_meta_t> g_gene_meta_pool(256);

container<genome_op_t> g_genome_op_pool(1024);
container<genome_meta_t> g_genome_meta_pool(1024);

container<population_meta_t> g_population_meta_pool(64);
container<gene_data_t> g_gene_data_pool(65535);
populations_t g_populations;
*/

struct gene_op gop;

int main()
{
    gop.init=NULL;
	log_init();
    global_init();
    return 0;
}
