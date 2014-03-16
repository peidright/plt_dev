#include "ntp.h"
#define USEC(x) (((x) >> 12) - 759 * ((((x) >> 10) + 32768) >> 16))
void ntpdate() {
char    *hostname="216.171.112.36";//"tick.usno.navy.mil";
int portno=123;     //NTP is port 123
int maxlen=1024;        //check our buffers
long i;          // misc var i
//struct ntpdata	msg;
char msg[48]={010,0,0,0,0,0,0,0,0};    // the packet we send
char  *buf = new char[1024]; // the buffer we get back
//struct in_addr ipaddr;        //  
struct protoent *proto;     //
struct sockaddr_in server_addr;
SOCKET s;  // socket
time_t tmit;   // the time -- This is a time_t sort of
//msg.status=(0<<6)|(3<<3)|MODE_CLIENT;

//=====================================================================================
//THIS IS WHAT IS MISSING MAJORILY  
//=====================================================================================
        //Initialise the winsock stack
        WSADATA wsaData;
        BYTE wsMajorVersion = 1;
        BYTE wsMinorVersion = 1;
        WORD wVersionRequested = MAKEWORD(wsMinorVersion, wsMajorVersion);   
        if (WSAStartup(wVersionRequested, &wsaData) != 0) 
        {
            _tprintf(_T("Failed to load winsock stack\n"));
            WSACleanup();
            return;
        }
        if (LOBYTE(wsaData.wVersion) != wsMajorVersion || HIBYTE(wsaData.wVersion) != wsMinorVersion)
        {
            _tprintf(_T("Winsock stack does not support version which this program requires\n"));
            WSACleanup();
            return;
        }
//=====================================================================================



//use Socket;
//
//#we use the system call to open a UDP socket
//socket(SOCKET, PF_INET, SOCK_DGRAM, getprotobyname("udp")) or die "socket: $!";
proto=getprotobyname("udp");
int err = GetLastError();
s=socket(PF_INET, SOCK_DGRAM, proto->p_proto);
if(s) {
    perror("asd");
    printf("socket=%d\n",s);
}
unsigned long ul;
ioctlsocket(s, FIONBIO, &ul); 
//
//#convert hostname to ipaddress if needed
//$ipaddr   = inet_aton($HOSTNAME);
memset( &server_addr, 0, sizeof( server_addr ));
server_addr.sin_family=AF_INET;
server_addr.sin_addr.s_addr = inet_addr(hostname);
//argv[1] );
//i   = inet_aton(hostname,&server_addr.sin_addr);
server_addr.sin_port=htons(portno);
//printf("ipaddr (in hex): %x\n",server_addr.sin_addr);

/*
 * build a message.  Our message is all zeros except for a one in the
 * protocol version field
 * msg[] in binary is 00 001 000 00000000 
 * it should be a total of 48 bytes long
*/

// send the data

//ioctlsocket(s, FIONBIO, &ul); 
printf("sending data.. %d\n",sizeof(msg));
i=sendto(s,(char*)&msg,sizeof(msg),0,(struct sockaddr *)&server_addr,sizeof(server_addr));
printf("gggg");
int iResult = -1;
    // Receive until the peer closes the connection
    //do {
again:
        iResult = recv(s, buf, 1024, 0);
        if ( iResult > 0 )
            printf("Bytes received: %d\n", iResult);
        else if ( iResult == 0 )
            printf("Connection closed\n");
		else if (iResult==SOCKET_ERROR) {
            printf("recv failed: %d\n", WSAGetLastError());
			goto again;
		}

    //} while( iResult > 0 );

/*
 * The high word of transmit time is the 10th word we get back
 * tmit is the time in seconds not accounting for network delays which
 * should be way less than a second if this is a local NTP server
 */

		tmit=ntohl(((UINT32*)buf)[10]);    //# get transmit time
//printf("tmit=%d\n",tmit);

/*
 * Convert time to unix standard time NTP is number of seconds since 0000
 * UT on 1 January 1900 unix time is seconds since 0000 UT on 1 January
 * 1970 There has been a trend to add a 2 leap seconds every 3 years.
 * Leap seconds are only an issue the last second of the month in June and
 * December if you don't try to set the clock then it can be ignored but
 * this is importaint to people who coordinate times with GPS clock sources.
 */

tmit -= 2208988800U; 
//printf("tmit=%d\n",tmit);
/* use unix library function to show me the local time (it takes care
 * of timezone issues for both north and south of the equator and places
 * that do Summer time/ Daylight savings time.
 */


//#compare to system time
printf("Time: %s",ctime(&tmit));
printf("useconds: %lu",USEC(((UINT32*)buf)[11]));
i=(int)time(0);
//printf("%d-%d=%d\n",i,tmit,i-tmit);
printf("System time is %lu seconds off\n",i-tmit);
}