/*The service Com_SendSignal updates the signal 
object identified by SignalId with the signal 
referenced by the SignalDataPtr parameter.*/
uint8 Com_SendSignal( Com_SignalIdType 
SignalId, const void* SignalDataPtr )
/*the service Com_SendDynSignal updates the 
signal object identified by SignalId with the signal 
referenced by the SignalDataPtr parameter*/
uint8 Com_SendDynSignal( Com_SignalIdType 
SignalId, const void* SignalDataPtr, uint16 Length 
)
/*This service initializes internal and external 
interfaces and variables of the AUTO-SAR COM 
module layer for the further processing. After 
calling this function the inter-ECU communication 
is still disabled.*/
void Com_Init( const Com_ConfigType* config )
