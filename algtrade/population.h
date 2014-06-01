#ifndef POPULATION_H_
#define POPULATION_H_
#include <stdint.h>

typedef struct population_meta {
    uint16_t genomes[65536];
} population_meta_t;
typedef struct populations {
    uint8_t  populations[256];
}populations_t;
struct population_op {
};
struct populations_op{
};
#endif
