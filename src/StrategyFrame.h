#ifndef STRATEGY_FRAME_H_
#define STRATEGY_FRAME_H_

enum symsg_type {
	TCHANGE,
	KCHANGE,
	TMSSAGE,
};

enum symsg_subtype {
	OLD,
	NEW,
};

typedef struct symsg_tchange_s {
	symsg_subtype subtype;
	float v;
}symsg_tchange_t;

typedef struct symsg_kchange_s {
	symsg_subtype subtype;
	float o;
	float c;
	float h;
	float l;
}symsg_kchange_t;


typedef struct  symsg_s{
	symsg_type type;
	int     len;
	void    *data;
}symsg_t;






#endif
