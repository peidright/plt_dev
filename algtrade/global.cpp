#include "global.h"
#include "gene_cell.h"
#include <assert.h>
#include <vector>
#include "log.h"

container<gene_cell_meta_t> g_gene_cell_meta_pool(256);
container<gene_cell_op_t> g_gene_cell_op_pool(1024);
container<gene_cell_data_t> g_gene_cell_data_pool(65535);

container<gene_op_t> g_gene_op_pool(256);
container<gene_meta_t> g_gene_meta_pool(256);

container<genome_op_t> g_genome_op_pool(1024);
container<genome_meta_t> g_genome_meta_pool(64000);
container<genome_meta_t> g_genome_meta_pool_small(64000);
container<genome_meta_t> g_genome_meta_pool_half(64000);

container<population_meta_t> g_population_meta_pool(64);
container<gene_data_t> g_gene_data_pool(65535);
populations_t g_populations;

int global_gene_cell_init();
int global_gene_init();
int global_genome_init();
int populations_init();



int global_init()
{
    int ret;
    //init gene
    ret = global_gene_cell_init();

    //init genome
    ret = global_gene_init();

    //init population
    return 0;
}

int global_genome_init()
{
    int size=g_gene_meta_pool.size();
    int cell_num;
    int gene_num;
    genome_meta_t *pgenome_meta=g_genome_meta_pool.get(-1);

    cell_num=sizeof(g_gene_chaos)/sizeof(g_gene_chaos[0]);
    gene_num=g_gene_meta_pool.size();

    pgenome_meta->cell_num=cell_num;
    pgenome_meta->gene_num=gene_num;

    for(int i=0;i<g_gene_meta_pool.total;i++) {
        gene_meta_t *pgene_meta=g_gene_meta_pool.get(i);
        if(pgene_meta) {
                        pgene_meta->gene_cells[i]=i;
                        pgene_meta->cell_cases[i];
/*
typedef struct genome_meta{
    uint8_t  *gene_cell_feas;
    uint8_t   gene_cells[10];
    uint16_t  cell_num;
    uint16_t  gene_num;
} genome_meta_t;

typedef struct gene_meta{
    uint8_t gene_cells[10];
    uint8_t cell_cases[10];
    uint8_t cnums;
    gene_action action;    
}gene_meta_t;

*/
        }
    }
    return 0;
}

void gene_generate(vector< vector<gene_cell_meta_t> >::iterator begin , 
                    vector< vector<gene_cell_meta_t> >::iterator end,
                    vector< gene_cell_meta_t> &dest, container<gene_meta_t> &gene_meta_pool)
{
    if(begin == end) {
        /*process
         * */
        //T* container<T>::get(int idx)
        gene_meta_t *gene_meta=gene_meta_pool.get(-1);
        if(gene_meta) {
            memset(gene_meta,0x0,sizeof(gene_meta_t));
            gene_meta->cnums=dest.size();
            LOG_DEBUG<<"dest.size:"<<dest.size()<<std::endl;

            for(int i=0;i<dest.size();i++) {
                if(i<10){
                    int did=dest[i].did;
                    gene_cell_data_t *pgene_cell_data=g_gene_cell_data_pool.get(did);
                    if(pgene_cell_data) {
                        //special case i=i
                        gene_meta->gene_cells[i]=i;
                        gene_meta->cell_cases[i]=pgene_cell_data->cn;

                    }else {
                        assert(0);
                    }
                }else {
                    assert(0);
                }
            }
        }else {
            assert(0);
        }
    } else {
        for(int i=0; i<begin[0].size();i++) {
            dest.push_back(begin[0][i]);
            gene_generate(begin+1,end, dest, gene_meta_pool);
            dest.erase(dest.end()-1);
        }
    }
}


int global_gene_init()
{
    //gene init
    int op_total=g_gene_cell_meta_pool.size();
    vector< vector<gene_cell_meta_t> > gene_cell_meta_vv;
    vector< gene_cell_meta_t> dest;
    LOG_DEBUG<<"op_total:"<<op_total<<std::endl;
    for(int i=0;i<op_total;i++) {
        gene_cell_meta_t *pgene_cell_meta=g_gene_cell_meta_pool.get(i);
        if(pgene_cell_meta) {
            vector<gene_cell_meta_t> gene_cell_meta_v;
            gene_cell_meta_v.clear();
            gene_cell_meta_t gene_cell_meta;
            gene_cell_data_t gene_cell_data;
            gene_cell_data_t *pgene_cell_data;

            pgene_cell_data=g_gene_cell_data_pool.get(pgene_cell_meta->did);

            for(int j=0;j<pgene_cell_meta->cn;j++) {
                memcpy(&gene_cell_meta, pgene_cell_meta, sizeof(gene_cell_meta_t));
                memcpy(&gene_cell_data, pgene_cell_data, sizeof(gene_cell_data_t));
                gene_cell_data.cn=j;
                int data_idx=g_gene_cell_data_pool.put(gene_cell_data);
                gene_cell_meta.did=data_idx;
                gene_cell_meta_v.push_back(gene_cell_meta);
                int meta_idx=g_gene_cell_meta_pool.put(gene_cell_meta);
            }
            LOG_DEBUG<<"gene_cell_meta_v.size: "<<gene_cell_meta_v.size()<<std::endl;
            gene_cell_meta_vv.push_back(gene_cell_meta_v);
        }
        LOG_DEBUG<<"gene_cell_meta_vv.size: "<<gene_cell_meta_vv.size()<<std::endl;
    }

    /*gene gene_pool
     * */

    //gene all the genome
    if(gene_cell_meta_vv.size() < 6) {
        gene_generate(gene_cell_meta_vv.begin() , gene_cell_meta_vv.end(),
                        dest, g_gene_meta_pool);
        LOG_DEBUG<<"g_gene_meta_pool.size:"<<g_gene_meta_pool.size()<<std::endl;
    }else if(gene_cell_meta_vv.size() > 10) {
        /*
        gene small
        gene half
        gene full
        */
    }else {
        /*
        gene small
        gene full
        */
    }
    return 0;
}

int global_gene_cell_init()
{
    int len=sizeof(g_gene_chaos)/sizeof(g_gene_chaos[0]);
    int meta_idx=0;
    int data_idx=0;
    int op_idx=0;

    gene_cell_meta_t gene_cell_meta;
    gene_cell_data_t gene_cell_data;
    gene_cell_meta_t *pgene_cell_meta;
    gene_cell_data_t *pgene_cell_data;
    gene_cell_op_t   *pgene_cell_op;

    for(int i=0;i<len;i++){
        op_idx=g_gene_cell_op_pool.put(g_gene_chaos[i]);

        data_idx=g_gene_cell_data_pool.put(gene_cell_data);
        
        gene_cell_meta.oid=op_idx;
        gene_cell_meta.did=data_idx;

        meta_idx=g_gene_cell_meta_pool.put(gene_cell_meta);

        pgene_cell_op=g_gene_cell_op_pool.get(op_idx);
        pgene_cell_meta=g_gene_cell_meta_pool.get(data_idx);
        pgene_cell_data=g_gene_cell_data_pool.get(op_idx);

        typedef void* (*init_func)(void *,void *);
        pgene_cell_op->init(pgene_cell_meta,NULL);
        LOG_DEBUG<<"op_idx:"<<op_idx<<" data_idx:"<<data_idx<<" meta_idx:"<<meta_idx<<" meta_cn:"<<(int)pgene_cell_meta->cn<<std::endl;
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
