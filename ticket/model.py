"""Original editable parametric design of the Echo Hollow ticket.
Not a copy of Pino's 3D files or of any film artwork.
Two flat printable halves; turn both detailed faces UP, glue back-to-back.
"""
import cadquery as cq
from shapely.geometry import Point, LineString, Polygon
from shapely.affinity import scale, rotate
from pathlib import Path
import trimesh

OUT=Path(__file__).resolve().parent
W,H=74.0,42.0
PLATE=1.75
RAISE=0.48
BEVEL=4.0

def base():
    return cq.Workplane('XY').rect(W,H).extrude(PLATE).edges('|Z').fillet(BEVEL)

def raise_poly(shape, z=PLATE, height=RAISE):
    if shape.is_empty:return None
    if shape.geom_type=='MultiPolygon':
        solids=[raise_poly(p,z,height) for p in shape.geoms]
        a=solids[0]
        for q in solids[1:]:a=a.union(q)
        return a
    coords=list(shape.exterior.coords)
    return cq.Workplane('XY',origin=(0,0,z)).polyline(coords).close().extrude(height)

def raised_line(path, width=.78):
    return raise_poly(LineString(path).buffer(width/2,cap_style=1,join_style=1,resolution=12))

def txt(st, size, x,y, thick=RAISE, bold=False):
    return cq.Workplane('XY',origin=(x,y,PLATE)).text(st,size,thick,font='DejaVu Sans',kind='bold' if bold else 'regular',halign='center',valign='center',combine=True)

# Face: Pino's station name + restrained boarding-pass detailing
front=base()
front=front.union(txt('ECHO HOLLOW',6.7,0,7.0,bold=True))
front=front.union(txt('PLATFORM 00',3.7,0,-1.4))
front=front.union(txt('NO TIMETABLE',2.65,0,-11.2))
for p in [(-29,14),(29,14)]:
    front=front.union(raise_poly(Point(*p).buffer(1.25,resolution=16)))
for yy in (-6.0,-7.8):
    front=front.union(raised_line([(-25,yy),(25,yy)],.68))
front=front.union(raised_line([(-29,15),(29,15)],.62))
front=front.union(raised_line([(-29,-15),(29,-15)],.62))
# four small ties between two rails
for xx in (-19,-7,7,19):front=front.union(raised_line([(xx,-6.2),(xx,-7.6)],.78))

# Reverse: original, deliberately simple sleeping Dot + pond / printable relief.
back=base()
back=back.union(txt('DOT / BY THE POND',3.35,0,15.4))
# rounded sleeping curled body, head and upturned ears
body=scale(Point(5,1).buffer(1,resolution=32),11.2,6.55,origin=(5,1))
head=scale(Point(-6.9,1).buffer(1,resolution=32),5.2,5.3,origin=(-6.9,1))
ear1=Polygon([(-10.5,4),(-10.4,10.1),(-5.5,5.6)])
ear2=Polygon([(-5.3,4.8),(-3.1,9.1),(-1.7,3.8)])
for shape in (body,head,ear1,ear2):back=back.union(raise_poly(shape))
# curved tail curling towards body, made of connected printable rounded stroke
tail=[(12.3,3.1),(16.0,4.7),(18.8,4.0),(19.5,1.2),(18.8,-1.7),(16.8,-3.0),(14.7,-2.6)]
back=back.union(raised_line(tail,2.65))
# tiny rounded sleeping paw tucked at the front
back=back.union(raised_line([(-6,-3.6),(-3.2,-4.4),(0.5,-4.1)],1.25))
# Tiny sleeping eye and the fold of one paw cut only into the raised relief.
# These shallow grooves are decorative and never cut into the structural plate.
eye=raised_line([(-10.35,2.15),(-9.0,1.65),(-7.65,2.05)],0.75).translate((0,0,0.20))
back=back.cut(eye)
paw=raised_line([(-5.25,-3.0),(-3.4,-3.3)],0.58).translate((0,0,0.20))
back=back.cut(paw)
# pond ripples encircle the sleeping cat
back=back.union(raised_line([(-23,-10),(-13,-10.6),(-4,-10.7),(5,-10.3),(14,-9.7),(23,-10)],.82))
back=back.union(raised_line([(-19,-13),(-8,-13.5),(4,-13.4),(18,-13)],.75))
back=back.union(raised_line([(-12,-16.1),(0,-16.5),(12,-16.1)],.70))
# moon over the pond and a subtle original glyph, not a third-party copyrighted artwork
back=back.union(raise_poly(Point(25,9).buffer(1.4,resolution=20)))

for name,obj in [('echo_hollow_front.stl',front),('echo_hollow_dot_reverse.stl',back)]:
    path=OUT/name
    cq.exporters.export(obj,str(path),tolerance=.08,angularTolerance=.2)
    mesh=trimesh.load_mesh(str(path),force='mesh')
    print(name,round(mesh.extents[0],2),round(mesh.extents[1],2),round(mesh.extents[2],2),'watertight',mesh.is_watertight,'winding_consistent',mesh.is_winding_consistent,'components',len(mesh.split()),'volume',round(mesh.volume,2),'faces',len(mesh.faces))
    assert mesh.is_watertight and mesh.is_winding_consistent, f'{name} mesh invalid'
    assert len(mesh.split())==1,f'{name} detached parts'
    assert mesh.volume>0 and mesh.extents[2]>2,'unexpected geometry'

