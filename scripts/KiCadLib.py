import sexpdata
import datetime

class PinNumbersStyle:
    def __init__(self, hide=False):
        self.pin_numbers = hide
        
    def eval(self):
        if self.pin_numbers:
            return ['pin_numbers', 'hide']
            
class PinNamesStyle:
    def __init__(self, hide=False):
        self.pin_names = hide
        
    def eval(self):
        if self.pin_names:
            return ['pin_names', 'hide']

class InBom:
    def __init__(self, val=True):
        self.val = val
        
    def eval(self):
        if self.val:
            return ['in_bom', 'yes']
        else:
            return ['in_bom', 'no']

class OnBoard:
    def __init__(self, val=True):
        self.val = val
        
    def eval(self):
        if self.val:
            return ['on_board', 'yes']
        else:
            return ['on_board', 'no']

class Id:
    def __init__(self,id):
        self.id = id
        
    def eval(self):
        return ['id', self.id]
        
class PositionIdentifier:
    def __init__(self, x, y, angle=0):
        self.x = x
        self.y = y
        self.angle = angle
        
    def eval(self):
        return ['at', self.x, self.y, self.angle]
        
class Font:
    def __init__(self, height, width, thickness=None, bold=None, italic=None):
        self.height = height
        self.width = width
        self.thickness = thickness
        self.bold = bold
        self.italic = italic
        
    def eval(self):
        r = ['font', ['size', self.height, self.width]]
        if(self.thickness):
            r.append(['thickness', self.thickness])
        if(self.bold):
            r.append('bold')
        if(self.italic):
            r.append('italic')
        return r
        
class Justify:
    def __init__(self,align):
        self.algin = align
        
    def eval(self):
        return ['justify', self.align]
        
class TextEffects:
        def __init__(self, font, justify=None, hide=None):
            self.font = font
            self.justify = justify
            self.hide = hide
            
        def eval(self):
            r = ['effects', self.font.eval()]
            if(self.justify):
                r.append(self.justify.eval())
            if(self.hide):
                r.append('hide')
            return r

class Property:
    def __init__(self, key, value, id, position, text_effects):
        self.key = key
        self.value = value
        self.id = id
        self.position = position
        self.text_effects = text_effects
        
    def eval(self):
        return ['property', f'\"{self.key}\"', f'\"{self.value}\"', self.id.eval(), self.position.eval(), self.text_effects.eval()]

class TopSymbol:
    def __init__(self, library_id, pin_numbers, pin_names, in_bom, on_board, properties, graphic_items=[], pins=[], subunits=[]):
        self.library_id = library_id
        self.pin_numbers = pin_numbers
        self.pin_names = pin_names
        self.in_bom = in_bom
        self.on_board = on_board
        self.properties = properties
        self.graphic_items = graphic_items
        self.pins = pins
        self.subunits = subunits
        
    def eval(self):
        r = []
        r.append('symbol')
        r.append(f'\"{self.library_id}\"')
        r.append(self.pin_numbers.eval()) if self.pin_numbers.eval() else None
        r.append(self.pin_names.eval()) if self.pin_names.eval() else None
        r.append(self.in_bom.eval())
        r.append(self.on_board.eval())
        for prop in self.properties:
            r.append(prop.eval())
        for item in self.graphic_items:
            r.append(item.eval())
        for pin in self.pins:
            r.append(pin.eval())
        for unit in self.subunits:
            r.append(unit.eval())    
        return r
        
    def get_properties(self):
        return self.properties

class Stroke:
    def __init__(self, width, type, r, g, b, a):
        self.width = width
        self.type = type
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        
    def eval(self):
        return ['stroke', ['width', self.width], ['type', self.type], ['color', self.r, self.g, self.b, self.a]]
        
class Fill:
    def __init__(self, type='outline'):
        self.type = type
        
    def eval(self):
        return ['fill', ['type', f'{self.type}'] ]
        
class Start:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eval(self):
        return ['start', x, y]
        
class Mid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eval(self):
        return ['mid', x, y]

class End:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eval(self):
        return ['end', x, y]

class Center:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eval(self):
        return ['center', x, y]

class Radius:
    def __init__(self,radius):
        self.radius = radius
        
    def eval(self):
        return ['radius', self.radius]

class Arc:
    def __init__(self, start, mid, end, stroke, fill):
        self.start = start
        self.mid = mid
        self.end = end
        self.stroke = stroke
        self.fill = fill
        
    def eval(self):
        r = []
        r.append('arc')
        r.append(self.start.eval())
        r.append(self.mid.eval())
        r.append(self.end.eval())
        r.append(self.stroke.eval())
        r.append(self.fill.eval())

class Circle:
    def __init__(self, center, radius, stroke, fill):
        self.center = center
        self.radius = radius
        self.stroke = stroke
        self.fill = fill
    
    def eval(self):
        return ['circle', self.center.eval(), self.radius.eval(), self.stroke.eval(), self.fill.eval()]
            
class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eval(self):
        return ['xy', self.x, self.y]
        
class PointsList:
    def __init__(self, points=[]):
        self.points = points
    
    def eval(self):
        r = ['pts']
        for p in self.points:
            r.append(p.eval())
        return r
            
class SymbolCurve:
    def __init__(self, points, stroke, fill):
        self.points = points
        self.stroke = stroke
        self.fill = fill
        
    def eval(self):
        return ['gr_curve', self.points.eval(), self.stroke.eval(), self.fill.eval()]
        
class SymbolLine:
    def __init__(self, points, stroke, fill):
        self.points = points
        self.stroke = stroke
        self.fill = fill
        
    def eval(self):
        return ['polyline', self.points.eval(), self.stroke.eval(), self.fill.eval()]
              
class SymbolRectangle:
    def __init__(self, start, end, stroke, fill):
        self.start = start
        self.end = end
        self.stroke = stroke
        self.fill = fill
        
    def eval(self):
        return ['rectangle', self.start.eval(), self.end.eval(), self.stroke.eval(), self.fill.eval()]

class SymbolText:
    def __init__(self, text, position, effects):
        self.text = text
        self.position = position
        self.effects = effects
        
    def eval(self):
        return ['text', f'\"{self.text}\"', self.position.eval(), self.effects.eval()]
                
class GrUnit:
    def __init__(self, library_id, unit, style, elements=[]):
        self.library_id = library_id
        self.unit = unit
        self.style = style
        self.elements = elements
        
    def eval(self):
        r = ['symbol', f'\"{self.library_id}_{self.unit}_{self.style}\"']
        for element in self.elements:
            r.append(element.eval())
        return r

class PinName:
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects
        
    def eval(self):
        return ['name', f'\"{self.name}\"', self.effects.eval()]
        
class PinNumber:
    def __init__(self, number, effects):
        self.number = number
        self.effects = effects
        
    def eval(self):
        return ['number', f'\"{self.number}\"', self.effects.eval()]
         
class Pin:
    def __init__(self, electrical_type, graphical_style, position, length, name, number):
        self.electrical_type = electrical_type
        self.graphical_style = graphical_style
        self.length = length
        self.position = position
        self.name = name 
        self.number = number
        
    def eval(self):
        return ['pin', self.electrical_type, self.graphical_style, self.position.eval(), ['length', self.length], self.name.eval(), self.number.eval()]

class PinUnit:
    def __init__(self, library_id, unit, style, elements = []):
        self.library_id = library_id
        self.unit = unit
        self.style = style
        self.elements = elements
        
    def eval(self):
        r = ['symbol', f'\"{self.library_id}_{self.unit}_{self.style}\"']
        for element in self.elements:
            r.append(element.eval())
        return r
                
class SymbolLib:
    def __init__(self,version=None,generator="KiCadLib_py",symbols=[]):
        if not version:
            self.version = 20211014
        else:
            self.version = version
        self.generator = generator
        self.symbols = symbols
            
    def eval(self):
        r = []
        r.append('kicad_symbol_lib')
        r.append(['version', f'{self.version}'])
        r.append(['generator', f'{self.generator}'])
        for sym in self.symbols:
            r.append(sym.eval())
            
        return r
        
    def to_sexp(self):
        l = self.eval()
        return sexpdata.dumps(l,str_as='symbol')
