import string

f = open('fir_channel_wide_tx.txt', 'w')

k =[    0,  -7,    12,    110,    319,    625,    958,    1203,    1216,  
    869,    83,  -1130,  -2643,  -4215,  -5514,  -6176,  -5866,  
  -4366,  -1645,    2098,    6419,    10668,    14071,    15850,  
    15367,    12262,    6568,  -1232,  -10211,  -19093,  -26414,  
  -30744,  -30927,  -26317,  -16955,  -3651,    12044,    27992,  
    41742,    50880,    53424,    48180,    35030,    15070,  -9431,  
  -35251,  -58614,  -75719,  -83325,  -79301,  -63067,  -35839,  
  -611,    38126,    74924,    104118,    120655,    120919,    103398,  
    69098,    21612,  -33194,  -87861,  -134317,  -165026,  -174148,  
  -158552,  -118490,  -57842,    16173,    93789,    163938,  
    215766,    240253,    231669,    188673,    114848,    18550,  
  -87943,  -189920,  -272195,  -321281,  -327472,  -286542,  
  -200773,  -79118,    63579,    208280,    334170,    421516,  
    454588,    424225,    329666,    179321,  -9697,  -213313,  
  -403339,  -551146,  -631672,  -627264,  -530806,  -347629,  
  -95874,    194877,    486657,    737562,    907128,    961999,  
    881152,    660008,    312782,  -127323,  -610271,  -1073586,  
  -1448605,  -1667943,  -1673361,  -1423134,  -898023,  -105088,  
    921177,    2120670,    3412334,    4701262,    5887507,    6875704,  
    7584452,    7954444,    7954444,    7584452,    6875704,    5887507,  
    4701262,    3412334,    2120670,    921177,  -105088,  -898023,  
  -1423134,  -1673361,  -1667943,  -1448605,  -1073586,  -610271,  
  -127323,    312782,    660008,    881152,    961999,    907128,  
    737562,    486657,    194877,  -95874,  -347629,  -530806,  
  -627264,  -631672,  -551146,  -403339,  -213313,  -9697,  
    179321,    329666,    424225,    454588,    421516,    334170,  
    208280,    63579,  -79118,  -200773,  -286542,  -327472,  
  -321281,  -272195,  -189920,  -87943,    18550,    114848,  
    188673,    231669,    240253,    215766,    163938,    93789,  
    16173,  -57842,  -118490,  -158552,  -174148,  -165026,  
  -134317,  -87861,  -33194,    21612,    69098,    103398,    120919,  
    120655,    104118,    74924,    38126,  -611,  -35839,  -63067,  
  -79301,  -83325,  -75719,  -58614,  -35251,  -9431,    15070,  
    35030,    48180,    53424,    50880,    41742,    27992,    12044,  
  -3651,  -16955,  -26317,  -30927,  -30744,  -26414,  -19093,  
  -10211,  -1232,    6568,    12262,    15367,    15850,    14071,  
    10668,    6419,    2098,  -1645,  -4366,  -5866,  -6176,  -5514,  
  -4215,  -2643,  -1130,    83,    869,    1216,    1203,    958,  
    625,    319,    110,    12,  -7,    0] 


for i in range (0,256):
    if k[i] >= 0:
        f.write('    "{0:024b}",\n'.format(k[i]))
    else:
        f.write('    "{0:024b}",\n'.format(16777216+k[i]))
#f.write( "%d\n" % k[i]
