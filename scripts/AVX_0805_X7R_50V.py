from KiCadLib import *
import Templates

def make_cap(id, fp, ds, mpn, val):
    pass
        
# AVX 0805 X7R 50V 10% ceramic capacitors
# part number = 0805 5 C XXY KAT2 
# XX = 2 digits of value in pF
# Y = number of zeros

values = [100, 150, 220, 270, 330, 101, 121, 181, 221, 271, 331, 391, 471, 561, 681, 821, 
          102, 122, 152, 182, 222, 272, 332, 392, 472, 502, 562, 682, 822, 
          ]
series = "AVX_0805_X7R_50V"
datasheet = "https://datasheets.kyocera-avx.com/X7RDielectric.pdf"

parts = []            

s = SymbolLib(symbols=parts)
f = open(f'{series}.kicad_sym','w')
f.write(s.to_sexp())
f.close()
