#include "global.h"

container<gene_op_t> g_gene_op_pool(256);
container<gene_meta_t> g_gene_meta_pool(256);

container<genome_op_t> g_genome_op_pool(1024);
container<genome_meta_t> g_genome_meta_pool(64000);
container<genome_meta_t> g_genome_meta_pool_small(64000);
container<genome_meta_t> g_genome_meta_pool_half(64000);

container<population_meta_t> g_population_meta_pool(64);
container<gene_data_t> g_gene_data_pool(65535);
populations_t g_populations;

int global_gene_init();
int global_genome_init();
int populations_init();

int global_init()
{
    int ret;
    //init gene
    ret = global_gene_init();

    //init genome

    //init population
    return 0;
}

void genome_generate(vector< vector<gene_meta_t>>::iterator begin , 
                    vector< vector<gene_meta_t>>::iterator end,
                    vector< gene_meta_t> &dest)
{
    if(begin == end) {
        /*process
         * */
        //T* container<T>::get(int idx)

    } else {
        for(int i=0; i<begin->size();i++) {
            dest.push_back(begin[i]);
            genome_generate(begin+1;end; dest);
            dest.erase(dest::end()-1);
        }
    }
}

int global_genome_init()
{
    vector< vector<gene_meta_t> gene_meta_vv;
    for(int i=0;i<g_gene_meta_pool.total;i++) {
        gene_meta_t *pgene_meta=g_gene_meta_pool.get(i);
        if(pgene_meta) {
            vector<gene_meta_t> gene_meta_v;
            gene_meta_v.clear();
            gene_meta_t gene_meta;
            gene_data_t gene_data;
            gene_data_t *pgene_data;

            pgene_data=g_gene_data_pool.get(gene_meta->did);

            for(int j=0;j<pgene_meta->cn;j++) {
                memcpy(&gene_meta, pgene_meta, sizeof(gene_meta_t));
                memcpy(&gene_data, pgene_data, sizeof(gene_data_t));
                int data_idx=g_gene_data_pool.put(gene_data);
                gene_meta.did=data_idx;
                gene_meta_v.push_back(gene_meta);
                //int meta_idx=g_gene_meta_pool.put(gene_meta);
            }
            gene_meta_vv.push_back(gene_meta_v);
        }
    }

    //container<genome_meta_t> g_genome_meta_pool(64000);
    //container<genome_meta_t> g_genome_meta_pool_small(64000);
    //container<genome_meta_t> g_genome_meta_pool_half(64000);

    //gene all the genome
    if(gene_meta_vv.size() < 6) {
        //gene full

    }else if(gene_meta_vv.size() > 10) {
        //gene small
        //gene half
        //gene full
    }else {
        //gene small
        //gene full
    }
    return 0;
}

int global_gene_init()
{
    int len=sizeof(g_gene_chaos)/sizeof(g_gene_chaos[0]);
    int meta_idx=0;
    int data_idx=0;
    int op_idx=0;

    gene_meta_t gene_meta;
    gene_data_t gene_data;
    gene_meta_t *pgene_meta;
    gene_data_t *pgene_data;
    gene_op_t   *pgene_op;

    for(int i=0;i<len;i++){
        /*put op*/
        op_idx=g_gene_op_pool.put(g_gene_chaos[i]);

        data_idx=g_gene_data_pool.put(gene_data);
        
        gene_meta.oid=op_idx;
        gene_meta.did=data_idx;

        meta_idx=g_gene_meta_pool.put(gene_meta);

        pgene_op=g_gene_op_pool.get(op_idx);
        pgene_data=g_gene_meta_pool.get(data_idx);
        pgene_meta=g_gene_data_pool.get(op_idx);

        //typedef void* (*init_func)(void *,void *);
        pgene_op.init(pgene_meta,NULL);
    }
    return 0;
}

/*
int get_op_idx(char *opname)
{
    int len=sizeof(g_gene_chaos)/sizeof(g_gene_chaos[0]);
    for(int i=0;i<len;i++){
        if(strcmp(opname, g_gene_chaos[0].name)==0){
            return i;
        }
    }
    return -1;
}

int get_op(char *opname, gene_op_t *gene_op)
{
    int len=sizeof(g_gene_chaos)/sizeof(g_gene_chaos[0]);
    for(int i=0;i<len;i++){
        if(strcmp(opname, g_gene_chaos[i].name)==0){
            memcpy(gene_op,g_gene_chaos[i],sizeof(g_gene_chaos[0]));
            return 0;
        }
    }
    return -1;
}
*/
