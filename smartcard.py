# -*- coding: cp874 -*-
from smartcard.CardConnection import CardConnection
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString, toBytes

cardtype = AnyCardType()
cardrequest = CardRequest( timeout=1, cardType=cardtype )

cardservice = cardrequest.waitforcard()

cardservice.connection.connect()

SELECT = [0x00, 0xA4, 0x04, 0x00, 0x08]
THAI_ID_CARD = [0xA0, 0x00, 0x00, 0x00, 0x54, 0x48, 0x00, 0x01]
REQ_CID = [0x80, 0xb0, 0x00, 0x04, 0x02, 0x00, 0x0d]
REQ_THAI_NAME = [0x80, 0xb0, 0x00, 0x11, 0x02, 0x00, 0x64]
REQ_ENG_NAME = [0x80, 0xb0, 0x00, 0x75, 0x02, 0x00, 0x64]
REQ_GENDER = [0x80, 0xb0, 0x00, 0xE1, 0x02, 0x00, 0x01]
REQ_DOB = [0x80, 0xb0, 0x00, 0xD9, 0x02, 0x00, 0x08]
REQ_ADDRESS = [0x80, 0xb0, 0x15, 0x79, 0x02, 0x00, 0x64]
REQ_ISSUE_EXPIRE = [0x80, 0xb0, 0x01, 0x67, 0x02, 0x00, 0x12]

DATA = [REQ_CID,REQ_THAI_NAME,REQ_ENG_NAME,REQ_GENDER,REQ_DOB,
REQ_ADDRESS,REQ_ISSUE_EXPIRE]

apdu = SELECT+THAI_ID_CARD
f = open(‘temp.txt’,’w’)

response, sw1, sw2 = cardservice.connection.transmit( apdu )
#print ‘response: ‘, response, ‘ status words: ‘, “%x %x” % (sw1, sw2)

#print ‘response: ‘, response, ‘ status words: ‘, “%x %x” % (sw1, sw2)
for d in DATA:
response, sw1, sw2 = cardservice.connection.transmit( d )
print sw1
if sw1 == 0x61: