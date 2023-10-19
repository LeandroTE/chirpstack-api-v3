# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/gw/gw.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63hirpstack-api/gw/gw.proto\x12\x02gw\x1a\"chirpstack-api/common/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\xa3\x01\n\nModulation\x12,\n\x04lora\x18\x03 \x01(\x0b\x32\x16.gw.LoRaModulationInfoH\x00R\x04loRa\x12$\n\x03\x66sk\x18\x04 \x01(\x0b\x32\x15.gw.FSKModulationInfoH\x00\x12\x33\n\x07lr_fhss\x18\x05 \x01(\x0b\x32\x18.gw.LRFHSSModulationInfoH\x00R\x06lrFHSSB\x0c\n\nparameters\"\xb1\x02\n\x0cUplinkTXInfo\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12&\n\nmodulation\x18\x02 \x01(\x0e\x32\x12.common.Modulation\x12J\n\x14lora_modulation_info\x18\x03 \x01(\x0b\x32\x16.gw.LoRaModulationInfoH\x00R\x12loRaModulationInfo\x12\x34\n\x13\x66sk_modulation_info\x18\x04 \x01(\x0b\x32\x15.gw.FSKModulationInfoH\x00\x12Q\n\x17lr_fhss_modulation_info\x18\x05 \x01(\x0b\x32\x18.gw.LRFHSSModulationInfoH\x00R\x14lrFHSSModulationInfoB\x11\n\x0fmodulation_info\"t\n\x12LoRaModulationInfo\x12\x11\n\tbandwidth\x18\x01 \x01(\r\x12\x18\n\x10spreading_factor\x18\x02 \x01(\r\x12\x11\n\tcode_rate\x18\x03 \x01(\t\x12\x1e\n\x16polarization_inversion\x18\x04 \x01(\x08\"B\n\x11\x46SKModulationInfo\x12\x1b\n\x13\x66requency_deviation\x18\x01 \x01(\r\x12\x10\n\x08\x64\x61tarate\x18\x02 \x01(\r\"^\n\x14LRFHSSModulationInfo\x12\x1f\n\x17operating_channel_width\x18\x01 \x01(\r\x12\x11\n\tcode_rate\x18\x02 \x01(\t\x12\x12\n\ngrid_steps\x18\x03 \x01(\r\"k\n\x16\x45ncryptedFineTimestamp\x12\x15\n\raes_key_index\x18\x01 \x01(\r\x12!\n\x0c\x65ncrypted_ns\x18\x02 \x01(\x0cR\x0b\x65ncryptedNS\x12\x17\n\x07\x66pga_id\x18\x03 \x01(\x0cR\x06\x66pgaID\">\n\x12PlainFineTimestamp\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xbd\x07\n\x0cGatewayStats\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\n\n\x02ip\x18\t \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x08location\x18\x03 \x01(\x0b\x32\x10.common.Location\x12\x16\n\x0e\x63onfig_version\x18\x04 \x01(\t\x12\x1b\n\x13rx_packets_received\x18\x05 \x01(\r\x12\x33\n\x16rx_packets_received_ok\x18\x06 \x01(\rR\x13rxPacketsReceivedOK\x12\x1b\n\x13tx_packets_received\x18\x07 \x01(\r\x12\x1a\n\x12tx_packets_emitted\x18\x08 \x01(\r\x12\x31\n\tmeta_data\x18\n \x03(\x0b\x32\x1e.gw.GatewayStats.MetaDataEntry\x12\x19\n\x08stats_id\x18\x0b \x01(\x0cR\x07statsID\x12M\n\x18tx_packets_per_frequency\x18\x0c \x03(\x0b\x32+.gw.GatewayStats.TxPacketsPerFrequencyEntry\x12M\n\x18rx_packets_per_frequency\x18\r \x03(\x0b\x32+.gw.GatewayStats.RxPacketsPerFrequencyEntry\x12\x39\n\x19tx_packets_per_modulation\x18\x0e \x03(\x0b\x32\x16.gw.PerModulationCount\x12\x39\n\x19rx_packets_per_modulation\x18\x0f \x03(\x0b\x32\x16.gw.PerModulationCount\x12G\n\x15tx_packets_per_status\x18\x10 \x03(\x0b\x32(.gw.GatewayStats.TxPacketsPerStatusEntry\x1a/\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a<\n\x1aTxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a<\n\x1aRxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17TxPacketsPerStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"G\n\x12PerModulationCount\x12\"\n\nmodulation\x18\x01 \x01(\x0b\x32\x0e.gw.Modulation\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"\xcd\x04\n\x0cUplinkRXInfo\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12J\n\x14time_since_gps_epoch\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x11timeSinceGPSEpoch\x12\x0c\n\x04rssi\x18\x05 \x01(\x05\x12\x19\n\x08lora_snr\x18\x06 \x01(\x01R\x07loRaSNR\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\r\x12\x10\n\x08rf_chain\x18\x08 \x01(\r\x12\r\n\x05\x62oard\x18\t \x01(\r\x12\x0f\n\x07\x61ntenna\x18\n \x01(\r\x12\"\n\x08location\x18\x0b \x01(\x0b\x32\x10.common.Location\x12\x32\n\x13\x66ine_timestamp_type\x18\x0c \x01(\x0e\x32\x15.gw.FineTimestampType\x12>\n\x18\x65ncrypted_fine_timestamp\x18\r \x01(\x0b\x32\x1a.gw.EncryptedFineTimestampH\x00\x12\x36\n\x14plain_fine_timestamp\x18\x0e \x01(\x0b\x32\x16.gw.PlainFineTimestampH\x00\x12\x0f\n\x07\x63ontext\x18\x0f \x01(\x0c\x12\x1b\n\tuplink_id\x18\x10 \x01(\x0cR\x08uplinkID\x12,\n\ncrc_status\x18\x11 \x01(\x0e\x32\r.gw.CRCStatusR\tcrcStatusB\x10\n\x0e\x66ine_timestamp\"\x9b\x04\n\x0e\x44ownlinkTXInfo\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\x11\n\tfrequency\x18\x05 \x01(\r\x12\r\n\x05power\x18\x06 \x01(\x05\x12&\n\nmodulation\x18\x07 \x01(\x0e\x32\x12.common.Modulation\x12J\n\x14lora_modulation_info\x18\x08 \x01(\x0b\x32\x16.gw.LoRaModulationInfoH\x00R\x12loRaModulationInfo\x12\x34\n\x13\x66sk_modulation_info\x18\t \x01(\x0b\x32\x15.gw.FSKModulationInfoH\x00\x12\r\n\x05\x62oard\x18\n \x01(\r\x12\x0f\n\x07\x61ntenna\x18\x0b \x01(\r\x12\"\n\x06timing\x18\x0c \x01(\x0e\x32\x12.gw.DownlinkTiming\x12<\n\x17immediately_timing_info\x18\r \x01(\x0b\x32\x19.gw.ImmediatelyTimingInfoH\x01\x12\x30\n\x11\x64\x65lay_timing_info\x18\x0e \x01(\x0b\x32\x13.gw.DelayTimingInfoH\x01\x12\x37\n\x15gps_epoch_timing_info\x18\x0f \x01(\x0b\x32\x16.gw.GPSEpochTimingInfoH\x01\x12\x0f\n\x07\x63ontext\x18\x10 \x01(\x0c\x42\x11\n\x0fmodulation_infoB\r\n\x0btiming_info\"\x17\n\x15ImmediatelyTimingInfo\";\n\x0f\x44\x65layTimingInfo\x12(\n\x05\x64\x65lay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"`\n\x12GPSEpochTimingInfo\x12J\n\x14time_since_gps_epoch\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x11timeSinceGPSEpoch\"h\n\x0bUplinkFrame\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTXInfo\x12!\n\x07rx_info\x18\x03 \x01(\x0b\x32\x10.gw.UplinkRXInfo\"k\n\x0eUplinkFrameSet\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTXInfo\x12!\n\x07rx_info\x18\x03 \x03(\x0b\x32\x10.gw.UplinkRXInfo\"\xbe\x01\n\rDownlinkFrame\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12#\n\x07tx_info\x18\x02 \x01(\x0b\x32\x12.gw.DownlinkTXInfo\x12\r\n\x05token\x18\x03 \x01(\r\x12\x1f\n\x0b\x64ownlink_id\x18\x04 \x01(\x0cR\ndownlinkID\x12$\n\x05items\x18\x05 \x03(\x0b\x32\x15.gw.DownlinkFrameItem\x12\x1d\n\ngateway_id\x18\x06 \x01(\x0cR\tgatewayID\"M\n\x11\x44ownlinkFrameItem\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12#\n\x07tx_info\x18\x02 \x01(\x0b\x32\x12.gw.DownlinkTXInfo\"\x93\x01\n\rDownlinkTXAck\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\r\n\x05token\x18\x02 \x01(\r\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1f\n\x0b\x64ownlink_id\x18\x04 \x01(\x0cR\ndownlinkID\x12$\n\x05items\x18\x05 \x03(\x0b\x32\x15.gw.DownlinkTXAckItem\"4\n\x11\x44ownlinkTXAckItem\x12\x1f\n\x06status\x18\x01 \x01(\x0e\x32\x0f.gw.TxAckStatus\"\xa5\x01\n\x14GatewayConfiguration\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\x0f\n\x07version\x18\x02 \x01(\t\x12*\n\x08\x63hannels\x18\x03 \x03(\x0b\x32\x18.gw.ChannelConfiguration\x12\x31\n\x0estats_interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x96\x02\n\x14\x43hannelConfiguration\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12&\n\nmodulation\x18\x02 \x01(\x0e\x32\x12.common.Modulation\x12P\n\x16lora_modulation_config\x18\x03 \x01(\x0b\x32\x18.gw.LoRaModulationConfigH\x00R\x14loRaModulationConfig\x12\x38\n\x15\x66sk_modulation_config\x18\x04 \x01(\x0b\x32\x17.gw.FSKModulationConfigH\x00\x12\r\n\x05\x62oard\x18\x05 \x01(\r\x12\x13\n\x0b\x64\x65modulator\x18\x06 \x01(\rB\x13\n\x11modulation_config\"D\n\x14LoRaModulationConfig\x12\x11\n\tbandwidth\x18\x01 \x01(\r\x12\x19\n\x11spreading_factors\x18\x02 \x03(\r\"9\n\x13\x46SKModulationConfig\x12\x11\n\tbandwidth\x18\x01 \x01(\r\x12\x0f\n\x07\x62itrate\x18\x02 \x01(\r\"\xeb\x01\n\x19GatewayCommandExecRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12\x16\n\x06\x45xecId\x18\x03 \x01(\x0cR\x06\x65xecID\x12\r\n\x05stdin\x18\x04 \x01(\x0c\x12\x43\n\x0b\x65nvironment\x18\x05 \x03(\x0b\x32..gw.GatewayCommandExecRequest.EnvironmentEntry\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x83\x01\n\x1aGatewayCommandExecResponse\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\x17\n\x07\x65xec_id\x18\x02 \x01(\x0cR\x06\x65xecID\x12\x0e\n\x06stdout\x18\x03 \x01(\x0c\x12\x0e\n\x06stderr\x18\x04 \x01(\x0c\x12\r\n\x05\x65rror\x18\x05 \x01(\t\"`\n\x17RawPacketForwarderEvent\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\x15\n\x06raw_id\x18\x02 \x01(\x0cR\x05rawID\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"b\n\x19RawPacketForwarderCommand\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\x15\n\x06raw_id\x18\x02 \x01(\x0cR\x05rawID\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"p\n\tConnState\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\"\n\x05state\x18\x02 \x01(\x0e\x32\x13.gw.ConnState.State\" \n\x05State\x12\x0b\n\x07OFFLINE\x10\x00\x12\n\n\x06ONLINE\x10\x01*;\n\x0e\x44ownlinkTiming\x12\x0f\n\x0bIMMEDIATELY\x10\x00\x12\t\n\x05\x44\x45LAY\x10\x01\x12\r\n\tGPS_EPOCH\x10\x02*7\n\x11\x46ineTimestampType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tENCRYPTED\x10\x01\x12\t\n\x05PLAIN\x10\x02*0\n\tCRCStatus\x12\n\n\x06NO_CRC\x10\x00\x12\x0b\n\x07\x42\x41\x44_CRC\x10\x01\x12\n\n\x06\x43RC_OK\x10\x02*\xbc\x01\n\x0bTxAckStatus\x12\x0b\n\x07IGNORED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0c\n\x08TOO_LATE\x10\x02\x12\r\n\tTOO_EARLY\x10\x03\x12\x14\n\x10\x43OLLISION_PACKET\x10\x04\x12\x14\n\x10\x43OLLISION_BEACON\x10\x05\x12\x0b\n\x07TX_FREQ\x10\x06\x12\x0c\n\x08TX_POWER\x10\x07\x12\x10\n\x0cGPS_UNLOCKED\x10\x08\x12\x0e\n\nQUEUE_FULL\x10\t\x12\x12\n\x0eINTERNAL_ERROR\x10\nBR\n\x14io.chirpstack.api.gwB\x0cGatewayProtoP\x01Z*github.com/brocaar/chirpstack-api/go/v3/gwb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.gw.gw_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024io.chirpstack.api.gwB\014GatewayProtoP\001Z*github.com/brocaar/chirpstack-api/go/v3/gw'
  _GATEWAYSTATS_METADATAENTRY._options = None
  _GATEWAYSTATS_METADATAENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_options = b'8\001'
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._options = None
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._serialized_options = b'8\001'
  _DOWNLINKTIMING._serialized_start=5368
  _DOWNLINKTIMING._serialized_end=5427
  _FINETIMESTAMPTYPE._serialized_start=5429
  _FINETIMESTAMPTYPE._serialized_end=5484
  _CRCSTATUS._serialized_start=5486
  _CRCSTATUS._serialized_end=5534
  _TXACKSTATUS._serialized_start=5537
  _TXACKSTATUS._serialized_end=5725
  _MODULATION._serialized_start=136
  _MODULATION._serialized_end=299
  _UPLINKTXINFO._serialized_start=302
  _UPLINKTXINFO._serialized_end=607
  _LORAMODULATIONINFO._serialized_start=609
  _LORAMODULATIONINFO._serialized_end=725
  _FSKMODULATIONINFO._serialized_start=727
  _FSKMODULATIONINFO._serialized_end=793
  _LRFHSSMODULATIONINFO._serialized_start=795
  _LRFHSSMODULATIONINFO._serialized_end=889
  _ENCRYPTEDFINETIMESTAMP._serialized_start=891
  _ENCRYPTEDFINETIMESTAMP._serialized_end=998
  _PLAINFINETIMESTAMP._serialized_start=1000
  _PLAINFINETIMESTAMP._serialized_end=1062
  _GATEWAYSTATS._serialized_start=1065
  _GATEWAYSTATS._serialized_end=2022
  _GATEWAYSTATS_METADATAENTRY._serialized_start=1792
  _GATEWAYSTATS_METADATAENTRY._serialized_end=1839
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_start=1841
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_end=1901
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_start=1903
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_end=1963
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_start=1965
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_end=2022
  _PERMODULATIONCOUNT._serialized_start=2024
  _PERMODULATIONCOUNT._serialized_end=2095
  _UPLINKRXINFO._serialized_start=2098
  _UPLINKRXINFO._serialized_end=2687
  _DOWNLINKTXINFO._serialized_start=2690
  _DOWNLINKTXINFO._serialized_end=3229
  _IMMEDIATELYTIMINGINFO._serialized_start=3231
  _IMMEDIATELYTIMINGINFO._serialized_end=3254
  _DELAYTIMINGINFO._serialized_start=3256
  _DELAYTIMINGINFO._serialized_end=3315
  _GPSEPOCHTIMINGINFO._serialized_start=3317
  _GPSEPOCHTIMINGINFO._serialized_end=3413
  _UPLINKFRAME._serialized_start=3415
  _UPLINKFRAME._serialized_end=3519
  _UPLINKFRAMESET._serialized_start=3521
  _UPLINKFRAMESET._serialized_end=3628
  _DOWNLINKFRAME._serialized_start=3631
  _DOWNLINKFRAME._serialized_end=3821
  _DOWNLINKFRAMEITEM._serialized_start=3823
  _DOWNLINKFRAMEITEM._serialized_end=3900
  _DOWNLINKTXACK._serialized_start=3903
  _DOWNLINKTXACK._serialized_end=4050
  _DOWNLINKTXACKITEM._serialized_start=4052
  _DOWNLINKTXACKITEM._serialized_end=4104
  _GATEWAYCONFIGURATION._serialized_start=4107
  _GATEWAYCONFIGURATION._serialized_end=4272
  _CHANNELCONFIGURATION._serialized_start=4275
  _CHANNELCONFIGURATION._serialized_end=4553
  _LORAMODULATIONCONFIG._serialized_start=4555
  _LORAMODULATIONCONFIG._serialized_end=4623
  _FSKMODULATIONCONFIG._serialized_start=4625
  _FSKMODULATIONCONFIG._serialized_end=4682
  _GATEWAYCOMMANDEXECREQUEST._serialized_start=4685
  _GATEWAYCOMMANDEXECREQUEST._serialized_end=4920
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._serialized_start=4870
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._serialized_end=4920
  _GATEWAYCOMMANDEXECRESPONSE._serialized_start=4923
  _GATEWAYCOMMANDEXECRESPONSE._serialized_end=5054
  _RAWPACKETFORWARDEREVENT._serialized_start=5056
  _RAWPACKETFORWARDEREVENT._serialized_end=5152
  _RAWPACKETFORWARDERCOMMAND._serialized_start=5154
  _RAWPACKETFORWARDERCOMMAND._serialized_end=5252
  _CONNSTATE._serialized_start=5254
  _CONNSTATE._serialized_end=5366
  _CONNSTATE_STATE._serialized_start=5334
  _CONNSTATE_STATE._serialized_end=5366
# @@protoc_insertion_point(module_scope)