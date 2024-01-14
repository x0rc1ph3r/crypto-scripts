from sympy.ntheory.modular import crt
from sympy import integer_nthroot
from Crypto.Util.number import long_to_bytes

##加密输出 1
c1 = 0x284C49D57F9B6589E32632E4221CE06EB9893794609A0CE8484317F87BF695A1AF938533CE292E5D6FC3A94BE1587C6F3D0B9C63FFCB08DC9D3406C428F5398A62CB9362F50A57F1A15AA9F291955DC87B597EE8FCF47D1E95B7D77668C1041457CDCAD6116D5B3895CE11088479CC62E19DE7260F2B21098BD971EF0151CE21

n1 = 0xEBC238B14DBA3DCCDA59EE85F189DF049F93D57CE4686C6DE5EC7B618AA315784227C498D64B11F2D804B52A5855D4B9806D5EBBF3610AC641DA84A39EECB94CFFE8574F6424656C8E60B04ADE87391AF7D1DB33ED7FCB4C17A07A05D3B32309557D24E8D1C7E2193AE4FE10107F5914ADC33192DFA8E684B447F3523916E129

##加密输出 2
c2= 0x8F0CAB681FFEC55BD664E33D2EB2B51D64C404E84B2D96D8FC5D18D36643E7F2AF9FCAF76D008CDB2A1CB1A1F48C8E6555B3D9909D7EFE7B886ABA67021F1B6D12EEC46AC9AB5A868EA7F677DC1E7322D72DC2D9460887348E72F43C4268268D16DE501B13A20072DCE7DB9B9A2DD8868408A40530F574B395DAB6EDB1487564

n2=0x90EFDD26C9F14F76FC9439F964044D0BB5AE973C9ADFE2E74CFCBBFB76DB992A2A93D47C9A79ECF3E4D6ADD576EC396057DA3D9B2426E92B55F8DC7E9C3330A70A21EF366CA00AFA90988A88D308B458A89C58191E7B74A38680898B06C97955A9430C39CC1D0C2A644152FED5D85820D28331D47839C337866CCB331D4A7845

##加密输出 3
c3 = 0x12E3112FADB4279CF7936781AFD179E39F7B3848F0C0313B49E015B651890A178C791AF5A295A2E21801BB23197EB945617E0707462127463B793CF18E2AB4D1A13FA27A53FE4FF92154067456DA1378A9C5A1E704031D2FF8E3CF9DEC6E8E34F22D70CE356FF9CD4E2D8BF57A2F7660AAAA92A87E9E352F2CB3760F478B966F

n3 = 0xC456D31C4B04E68BE0A143196EA313DB2BB9E49C0270D290B905C3D407E65D2E47EF98CDAF3225DF93B159EB203B4D6D6B89E07BD6536CC5C46120668D0A9C272C15FCC86D2AA4AC7457A57CB730D530F1B5D45B8B18CB41E737D605A09EBBC4016089634F3BE96E228BE3823D48C85857E8C1F35BC083B8190FA46B801B1EB5

##使用中国余数定理计算m的e次方
x = crt([n1, n2, n3], [c1, c2, c3], check=True)
# print("x=", x)

##开e次方求解m
m = integer_nthroot(x[0], 5)
# print("m=", m)

##输出明文
flag = long_to_bytes(m[0])
print(flag)
