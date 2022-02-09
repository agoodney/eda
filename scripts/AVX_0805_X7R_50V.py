from KiCadLib import *
import Templates

def make_cap(id, fp, ds, mpn, val):
    c = Templates.Capacitor(id)
    props = c.get_properties()
    for p in props:
        if p.key == "Footprint":
            p.value = fp
        if p.key == "Datasheet":
            p.value = ds
            
    vp = Property("Val", val, Id(4), PositionIdentifier(0, -2.54, 0), TextEffects(Font(1.27, 1.27)))
    mp = Property("MPN", mpn, Id(5), PositionIdentifier(0, 5.715, 0), TextEffects(Font(1.27, 1.27), hide=True))
    props.append(vp)
    props.append(mp)
    return c
        
# AVX 0805 X7R 50V 10% ceramic capacitors
# part number = 0805 5 C XXY KAT2 
# XX = 2 digits of value in pF
# Y = number of zeros

values = [100, 150, 220, 270, 330, 101, 121, 181, 221, 271, 331, 391, 471, 561, 681, 821, 
          102, 122, 152, 182, 222, 272, 332, 392, 472, 502, 562, 682, 822, 103, 123, 153,
          183, 203, 223, 273, 333, 393, 473, 563, 683, 823, 104, 124, 154, 224, 274, 334,
          474, 105, 225]
series = "AVX_0805_X7R_50V"
datasheet = "https://datasheets.kyocera-avx.com/X7RDielectric.pdf"

skus = []            

for v in values:
    p = v % 10
    picof = v//10*pow(10,p)
    mpn = f'08055C{v}KAT2A'
    if picof < 10000:
        val = f'{picof} pf'
    else:
        val = f'{picof/1000000} uf'
    skus.append({'MPN':mpn, 'val':val})


parts = []            
for part in skus:
    p = make_cap(part['MPN'], "", datasheet, part['MPN'], part['val'])
    parts.append(p)

s = SymbolLib(symbols=parts)
f = open(f'{series}.kicad_sym','w')
f.write(s.to_sexp())
f.close()
