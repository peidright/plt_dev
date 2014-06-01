#ifndef OP_H_
#define OP_H_
typedef void* (*init_func)(void *,void *);
typedef void (*clear_func)(void *);
typedef uint8_t (*output_func)(void *);
typedef bool    (*mutation_func)(void *, void **);
typedef bool    (*crossover_func)(void *, void *, void **, void **);
typedef void*    (*copy_func)(void *);
#endif
