/*The service Com_SendSignal updates the signal 
object identified by SignalId with the signal 
referenced by the SignalDataPtr parameter.*/
Unit8 Com_SendSignal();
/*the service Com_SendDynSignal updates the 
signal object identified by SignalId with the signal 
referenced by the SignalDataPtr parameter*/
Unit8 Com_SendDynSignal();
/*This service initializes internal and external 
interfaces and variables of the AUTO-SAR COM 
module layer for the further processing. After 
calling this function the inter-ECU communication 
is still disabled.*/
void Com_Init();
