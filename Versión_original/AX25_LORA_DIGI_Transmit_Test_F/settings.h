#define LORA_ENABLED true             // Set to true if you want LoRa transmissions (You can use Both LoRa and RTTY or only one of the two)
#define LORA_PAYLOAD_ID  "LW-LORA-2"   // Payload ID for LoRa protocol
#define LORA_FREQUENCY  434.448      // Can be different from RTTY frequency
//#define LORA_BANDWIDTH 62.5
#define LORA_BANDWIDTH 125
#define LORA_SPREADFACTOR 8
#define LORA_CODERATE 5
#define LORA_PREFIX "$$"             // Some older LoRa software does not accept a prefix of more than 2x "$"
#define LORA_SYNCWORD 0x18           // for sx1278
// #define LORA_SYNCWORD 0x1424      // for sx1262 (currently not supported)
#define LORA_POWER 10                // in dBm between 2 and 17. 10 = 10mW (recommended)
#define LORA_CURRENTLIMIT 100
#define LORA_PREAMBLELENGTH 8
#define LORA_GAIN 0
#define DEVMODE
