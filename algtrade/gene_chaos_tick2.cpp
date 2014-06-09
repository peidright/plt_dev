#include <stdint.h>
#include <unistd.h>
void* init_func_tick2(void *data,void *config)
{
    return NULL;
}
void clear_func_tick2(void *data)
{
}
uint8_t  output_func_tick2(void *data)
{
    return 0;
}
bool mutation_func_tick2(void *,void **data)
{
    return true;
}
bool crossover_func_tick2(void *g1,void *g2, void **g3, void **g4)
{
    return true;
}
void* copy_func_tick2(void *data)
{
    return NULL;
}

