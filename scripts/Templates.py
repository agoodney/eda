from KiCadLib import *

def Resistor(id):
    #these 4 properties are required per the KiCad documentation
    prop = [ Property("Reference", "R", Id(0), PositionIdentifier(-1.905,1.905,0), TextEffects(Font(1.27, 1.27))),
    Property("Value", id, Id(1), PositionIdentifier(0, 12.065, 0), TextEffects(Font(1.27, 1.27), hide=True)),
    Property("Footprint", "", Id(2), PositionIdentifier(0,0), TextEffects(Font(1.27, 1.27), hide=True)),
    Property("Datasheet", "", Id(3), PositionIdentifier(0, 8.89, 0), TextEffects(Font(1.27, 1.27), hide=True))]

    pts = PointsList([XY(-2.54,0), XY(-1.905,0.635), XY(-1.27,-0.635), XY(-0.635,0.635), XY(0,-0.635), XY(0.635,0.635), XY(1.27,-0.635), XY(1.905,0)])
    stroke = Stroke(width=0, type='default', r=0, g=0, b=0, a=0)
    fill = Fill(type='none')
    line = SymbolLine(pts, stroke, fill)
    g = GrUnit(library_id=id, unit=0, style=1, elements=[line])

    pin1 = Pin('passive', 'line', PositionIdentifier(-3.81, 0, 0), 1.27, PinName("~", TextEffects(Font(1.27, 1.27))), PinNumber("1",TextEffects(Font(1.27, 1.27))))
    pin2 = Pin('passive', 'line', PositionIdentifier(3.175, 0, 180), 1.27, PinName("~", TextEffects(Font(1.27, 1.27))), PinNumber("2",TextEffects(Font(1.27, 1.27))))

    pins = PinUnit(library_id=id, unit=1, style=1, elements=[pin1, pin2])

    return TopSymbol(id, PinNumbersStyle(hide=True), PinNamesStyle(hide=True), InBom(), OnBoard(), prop, subunits=[g,pins])
    