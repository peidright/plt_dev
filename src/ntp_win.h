#include <stdio.h>
//#include <sys/types.h>
//#include <sys/socket.h>
//#include <netinet/in.h>
//#include <arpa/inet.h>
//#include <netdb.h>
#include <time.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <tchar.h>

#pragma comment(lib, "Ws2_32.lib")

#define	JAN_1970	2208988800UL	/* 1970 - 1900 in seconds */

struct l_fixedpt {		/* 64-bit fixed-point */
	UINT32	int_part;
	UINT32	fraction;
};

struct s_fixedpt {		/* 32-bit fixed-point */
  u_short	int_part;
  u_short	fraction;
};

struct ntpdata {		/* NTP header */
  u_char			status;
  u_char			stratum;
  u_char			ppoll;
  int				precision:8;
  struct s_fixedpt	distance;
  struct s_fixedpt	dispersion;
  UINT32			refid;
  struct l_fixedpt	reftime;
  struct l_fixedpt	org;
  struct l_fixedpt	rec;
  struct l_fixedpt	xmt;
};

#define	VERSION_MASK	0x38
#define	MODE_MASK		0x07

#define	MODE_CLIENT		3
#define	MODE_SERVER		4
#define	MODE_BROADCAST	5

void ntpdate();
/*
int main() {
    ntpdate();
    return 0;
}*/

