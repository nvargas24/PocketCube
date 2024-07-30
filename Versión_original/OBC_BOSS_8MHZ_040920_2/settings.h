
#define TX_FREQ  437.125
#define RADIO_POWER  0x05// 25 mW
#define loggcount 1008// = 256-16
#define CALL 10

struct t_mtab { char c, pat; } ;

struct t_mtab morsetab[] = {
  {'.', 106},
  {',', 115},
  {'?', 76},
  {'/', 41},
  {'A', 6},
  {'B', 17},
  {'C', 21},
  {'D', 9},
  {'E', 2},
  {'F', 20},
  {'G', 11},
  {'H', 16},
  {'I', 4},
  {'J', 30},
  {'K', 13},
  {'L', 18},
  {'M', 7},
  {'N', 5},
  {'O', 15},
  {'P', 22},
  {'Q', 27},
  {'R', 10},
  {'S', 8},
  {'T', 3},
  {'U', 12},
  {'V', 24},
  {'W', 14},
  {'X', 25},
  {'Y', 29},
  {'Z', 19},
  {'1', 62},
  {'2', 60},
  {'3', 56},
  {'4', 48},
  {'5', 32},
  {'6', 33},
  {'7', 35},
  {'8', 39},
  {'9', 47},
  {'0', 63},
  
} ;

#define N_MORSE  (sizeof(morsetab)/sizeof(morsetab[0]))

#define SPEED  (25)
#define DOTLEN  (1200/SPEED)
#define DASHLEN  (3*(1200/SPEED))
#define disk1 0x50    //Address of 24LC32 eeprom chip



#define DOT_DURATION   200               // Duration of a Morse Code "dot" (in milliseconds)
#define DASH_DURATION  DOT_DURATION * 3  // Duration of a Morse Code "dash" (in milliseconds)
#define SIGNAL_GAP     DOT_DURATION      // Gap between dots/dashes of a single letter (in ms)
#define LETTER_GAP     DOT_DURATION * 3  // Gap between two letters (in milliseconds)
#define WORD_GAP       DOT_DURATION * 7  // Gap between two words (in milliseconds)
#define DOT             1                // DOT identifier
#define DASH            2                // DASH identifier
#define NONE            0                // Neither DOT nor DASH

String F ="";
String X ="";


char Q[3];
int QSL;
int QSO;
int t;
int l_;
int battVolts;
int CBat;
int CBor;
int CTx;
int CRx;
int t_cpu;
byte MCUSRX;

char txbuffer [150];
char superbuffer[150];

byte rdata[15];
char wdata[15];

char Z[8]="";
char T [70];
int n, j, q, d;

int b;
byte aux;

boolean _SMeter = false;
float rssi_floor;

int bc = 0;

unsigned int XOR;
unsigned int i;
unsigned int c;
int Index;
int endofstring;

byte value;
boolean sch = false;
boolean flg1;
int address = 0;
int addr = 0;
int _status = 0;
int _EEx;

int count = 0;

char Input [7];
char SDR [7];

char cadenaTemporal[7];
char cadenaTemporal_1[7];
char cadenaTemporal_2[7];
char cadenaTemporal_3[7];
char  RM[30]="";

boolean buttonWasPressed = false;        // Indicator of whether button was pressed in the last cycle
long lastTimestamp = 0;                  // Last recorded timestamp  (used for mesuring duration)
byte inputSignal[5];                     // Input signal buffer
int inputSignalIndex = 0;                // Index into the input signal buffer
int _RSC;
int _V;
byte _FR;

int w;
//int j;
int G;
int _P;

String command = "";
String ID = "CONDOR";
String ID2="";

const float VccMin   = 3.0;           // Minimum expected Vcc level, in Volts.
const float VccMax   = 4.15;           // Maximum expected Vcc level, in Volts.
const float VccCorrection = 4.00/4.12;  // Measured Vcc by multimeter divided by reported Vcc

//long interval = 60000;
unsigned long currentMillis;
