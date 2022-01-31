from KiCadLib import *
import Templates

def make_resistor(id, fp, ds, mpn, val):
    r = Templates.Resistor(id)
    props = r.get_properties()
    for p in props:
        if p.key == "Footprint":
            p.value = fp
        if p.key == "Datasheet":
            p.value = ds
            
    vp = Property("Val", val, Id(4), PositionIdentifier(0, -1.905, 0), TextEffects(Font(1.27, 1.27)))
    mp = Property("MPN", mpn, Id(5), PositionIdentifier(0, 5.715, 0), TextEffects(Font(1.27, 1.27), hide=True))
    props.append(vp)
    props.append(mp)
    return r
        
#part number ERJ-6ENF = thick film, 1%, 0805, 0.125W
# ERJ-6ENF XXX Y V
# XXX = three digits of value
# Y = number of '0s' after value
# R used to indicate decimal place in low values
# V = 4mm pitch, 5000/reel
# 10 ohm to 2.2M ohm
# e24 + e96 values
e24 = set([100,110,120,130,150,160,180,200,220,240,270,300,330,360,390,430,470,510,560,620,680,750,820,910])

e96 = set([100,102,105,107,110,113,115,118,121,124,127,130,133,137,140,143,147,150,154,158,162,165,169,174,
       178,182,187,191,196,200,205,210,215,221,226,232,237,243,249,255,261,267,274,280,287,294,301,309,
       316,324,332,340,348,357,365,374,383,392,402,412,422,432,442,453,464,475,487,499,511,523,536,549,
       562,576,590,604,619,634,649,665,681,698,715,732,750,768,787,806,825,845,866,887,909,931,953,976])


rvals = sorted(list(e24 | e96))

series = "ERJ-6ENF"
datasheet = "https://industrial.panasonic.com/cdbs/www-data/pdf/RDA0000/AOA0000C304.pdf"

part_numbers = []
#generate first decade
for i in rvals:
    v = str(i)[0:2]+"R"+str(i)[2]
    part_number = series+v+"V"
    val = i/10
    part = {'MPN':part_number, 'val': v}
    part_numbers.append(part)
    
#generate 'decades' 0 to 4:
for decade in range(0,5):
    for i in rvals:
        part_number = f'{series}{i}{decade}V'
        val = (i*pow(10,decade))
        if val >= 1000 and val < 1000000:
            val = f'{val/1000}'.replace('.','K')
        elif val >= 1000000:
            val = f'{val/1000000}'.replace('.','M')
        part = {'MPN':part_number, 'val':val}
        part_numbers.append(part)
        if decade == 4 and i == 220:
            break

parts = []            
for part in part_numbers:
    p = make_resistor(part['MPN'], "", datasheet, part['MPN'], part['val'])
    parts.append(p)
    
s = SymbolLib(symbols=parts)
f = open("ERJ-6ENF_0805_E24_E96.kicad_sym",'w')
f.write(s.to_sexp())
f.close()
