#include "gene.h"
#include "gene_chaos.h"

/*
typedef void (*init_func)(void *,void *);
typedef void (*clear_func)(void *);
typedef uint8_t (*output_func)(void *);
typedef bool    (*mutation_func)(void *, void **);
typedef bool    (*crossover_func)(void *, void *, void **, void **);
typedef void*    (*copy_func)(void *);
*/

gene_op_t g_gene_chaos[3]={
        {"tick1",
          init_func_tick1,
          clear_func_tick1,
          output_func_tick1,
          mutation_func_tick1,
          crossover_func_tick1,
          copy_func_tick1,
          },
        {"tick2",
          init_func_tick2,
          clear_func_tick2,
          output_func_tick2,
          mutation_func_tick2,
          crossover_func_tick2,
          copy_func_tick2,
          },
        {"tick2",
          init_func_tick2,
          clear_func_tick2,
          output_func_tick2,
          mutation_func_tick2,
          crossover_func_tick2,
          copy_func_tick2,
          }
};

int init_chaos()
{
    return 0;
}


