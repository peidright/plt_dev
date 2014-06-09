#include "genome.h"

/*
typedef struct genome_meta{
    uint8_t  *gene_cell_feas;
    uint8_t   gene_cells[10];
    uint16_t  cell_num;
    uint16_t  gene_num;
} genome_meta_t;

typedef struct genome_op
{
        init_func      init;
        clear_func     clear;
        output_func    output; 
        mutation_func  mutation;
        crossover_func crossover;
        copy_func      copy;
}genome_op_t;
*/


uint8_t * get_gene_feabuf(genome_meta_t *genome_meta,int gene_idx)
{
    int l=(genome_meta->cell_num * 4 + 8) /8;
    return &genome_meta->gene_cell_feas[l*gene_idx];
}


int get_gene_fea(genome_meta_t *genome_meta,int gene_idx, int fea_idx)
{
    uint8_t *feabuf=get_gene_feabuf(genome_meta, gene_idx);
    int major_idx=fea_idx / 2;
    int minor_idx=fea_idx % 2;
    if(minor_idx) {
        return feabuf[major_idx] & 0x0F;
    }else {
        return (feabuf[major_idx]) & 0xF0 >> 4;
    }
    return 0;
}

int set_gene_fea(genome_meta_t *genome_meta,int gene_idx, int fea_idx,int fea)
{
    uint8_t *feabuf=get_gene_feabuf(genome_meta, gene_idx);
    int major_idx=fea_idx / 2;
    int minor_idx=fea_idx % 2;
    if(minor_idx) {
        feabuf[major_idx]=(feabuf[major_idx] & 0xF0) | (fea);
    }else {
        feabuf[major_idx]=(feabuf[major_idx] & 0x0F) | (fea << 4);
    }
    return 0;
}


int get_gene_val(genome_meta_t *genome_meta,int gene_idx)
{
    int fea_idx=genome_meta->cell_num+1;
    return get_gene_fea(genome_meta, gene_idx, fea_idx);
}

int set_gene_val(genome_meta_t *genome_meta,int gene_idx, int val)
{
    int fea_idx=genome_meta->cell_num+1;
    return  set_gene_fea(genome_meta, gene_idx, fea_idx, val);
}
