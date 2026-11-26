import bpy, math, random, sys, os
from mathutils import Vector
def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
reset()
sc=bpy.context.scene
random.seed(7)

def mat(name, base, rough=0.8, rust=None, moss=None, scale=14, bump=0.4):
    m=bpy.data.materials.new(name); m.use_nodes=True
    nt=m.node_tree; nt.nodes.clear()
    out=nt.nodes.new('ShaderNodeOutputMaterial'); bs=nt.nodes.new('ShaderNodeBsdfPrincipled')
    bs.inputs['Roughness'].default_value=rough
    tc=nt.nodes.new('ShaderNodeTexCoord')
    n1=nt.nodes.new('ShaderNodeTexNoise'); n1.inputs['Scale'].default_value=scale; n1.inputs['Detail'].default_value=8
    nt.links.new(tc.outputs['Object'], n1.inputs['Vector'])
    cr=nt.nodes.new('ShaderNodeValToRGB')
    cr.color_ramp.elements[0].color=(*[c*0.6 for c in base],1); cr.color_ramp.elements[1].color=(*[min(1,c*1.25) for c in base],1)
    nt.links.new(n1.outputs['Fac'], cr.inputs['Fac'])
    col=cr.outputs['Color']
    if rust:
        n2=nt.nodes.new('ShaderNodeTexNoise'); n2.inputs['Scale'].default_value=scale*0.7; n2.inputs['Detail'].default_value=10
        nt.links.new(tc.outputs['Object'], n2.inputs['Vector'])
        r=nt.nodes.new('ShaderNodeValToRGB'); r.color_ramp.elements[0].position=0.42; r.color_ramp.elements[1].position=0.55
        r.color_ramp.elements[0].color=(0,0,0,1); r.color_ramp.elements[1].color=(1,1,1,1)
        nt.links.new(n2.outputs['Fac'], r.inputs['Fac'])
        mx=nt.nodes.new('ShaderNodeMix'); mx.data_type='RGBA'
        nt.links.new(r.outputs['Color'], mx.inputs['Factor']); nt.links.new(col, mx.inputs[6]); mx.inputs[7].default_value=(*rust,1)
        col=mx.outputs[2]
    if moss:
        n3=nt.nodes.new('ShaderNodeTexNoise'); n3.inputs['Scale'].default_value=5; n3.inputs['Detail'].default_value=6
        nt.links.new(tc.outputs['Object'], n3.inputs['Vector'])
        r=nt.nodes.new('ShaderNodeValToRGB'); r.color_ramp.elements[0].position=0.55; r.color_ramp.elements[1].position=0.65
        nt.links.new(n3.outputs['Fac'], r.inputs['Fac'])
        mx=nt.nodes.new('ShaderNodeMix'); mx.data_type='RGBA'
        nt.links.new(r.outputs['Color'], mx.inputs['Factor']); nt.links.new(col, mx.inputs[6]); mx.inputs[7].default_value=(*moss,1)
        col=mx.outputs[2]
    nt.links.new(col, bs.inputs['Base Color'])
    bp=nt.nodes.new('ShaderNodeBump'); bp.inputs['Strength'].default_value=bump
    nt.links.new(n1.outputs['Fac'], bp.inputs['Height']); nt.links.new(bp.outputs['Normal'], bs.inputs['Normal'])
    nt.links.new(bs.outputs['BSDF'], out.inputs['Surface'])
    return m

def lin(h): return tuple((int(h[i:i+2],16)/255)**2.2 for i in (1,3,5))
root=bpy.data.objects.new('raft',None); sc.collection.objects.link(root); root.scale=(0.9,0.9,0.9); root.location=(0,0,-0.2)
def put(o,m,parent=root):
    o.data.materials.append(m); o.parent=parent; return o
def box(loc,size,m,rot=0):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.scale=size; o.rotation_euler[2]=rot
    return put(o,m)
def cyl(loc,r,d,m,rot=(0,0,0),v=24):
    bpy.ops.mesh.primitive_cylinder_add(radius=r,depth=d,location=loc,vertices=v,end_fill_type='TRIFAN'); o=bpy.context.object; o.rotation_euler=rot
    bpy.ops.object.shade_smooth_by_angle(angle=0.6); return put(o,m)

wood=[mat('w%d'%i,lin(c),0.9,moss=lin('#5c7a2e'),scale=10) for i,c in enumerate(['#7a6446','#6e5a3e','#85704f','#5f4d35'])]
blue=mat('blue',lin('#35609a'),0.55,rust=lin('#8a4220'),scale=7,bump=0.0)
redb=mat('redb',lin('#8c4a28'),0.6,rust=lin('#6f3418'),scale=9,bump=0.0)
cloth=mat('cloth',lin('#d9d3c2'),0.95,scale=8)
patch=mat('patch',lin('#6f86a8'),0.95,scale=8)
crate=mat('crate',lin('#7a5a38'),0.9,scale=12)
red=mat('red',lin('#a02a24'),0.5,rust=lin('#6a2418'),scale=10)
green=mat('green',lin('#4f7a34'),0.5,rust=lin('#4a4020'),scale=10)
rope=mat('rope',lin('#8a6e48'),0.95,scale=30)

L,W=3.0,2.0; ZD=0.30
# deck: planks along X
n=14; pw=(W-0.1)/n
for i in range(n):
    y=-W/2+0.05+pw*(i+0.5)
    ln=L-0.15-random.uniform(0,0.12)
    box((random.uniform(-0.04,0.04),y,ZD),(ln,pw*0.96,0.07),random.choice(wood))
# beams under
for x in (-1.0,0,1.0): box((x,0,ZD-0.07),(0.12,W-0.1,0.07),wood[3])
# barrels around perimeter, axis perpendicular to edge, pointing outward
bd=0.36; bl=0.5
def barrel(x,y,axis):
    m=random.choice([blue,blue,blue,redb])
    rot=(math.pi/2,0,0) if axis=='y' else (0,math.pi/2,0)
    cyl((x,y,ZD-0.04),bd/2,bl,m,rot)
    for sg in (-1,1):
        o=(0,sg*(bl/2+0.006),0) if axis=='y' else (sg*(bl/2+0.006),0,0)
        cyl((x+o[0],y+o[1],ZD-0.04),bd/2*0.98,0.012,redb,rot,v=24)
nL=8; 
for i in range(nL):
    x=-L/2+bd/2+i*(L-bd)/(nL-1)
    barrel(x,W/2+0.02,'y'); barrel(x,-W/2-0.02,'y')
nW=4
for i in range(nW):
    y=-0.585+i*0.39
    barrel(L/2+0.02,y,'x'); barrel(-L/2-0.02,y,'x')

# schiuma sul pelo dell'acqua attorno a ogni barile (piano a z=0.002, alpha = sfumo del bordo x rumore)
fm=bpy.data.materials.new('foam'); fm.use_nodes=True; nt=fm.node_tree; nt.nodes.clear()
o_=nt.nodes.new('ShaderNodeOutputMaterial'); em=nt.nodes.new('ShaderNodeEmission'); tr=nt.nodes.new('ShaderNodeBsdfTransparent'); mx=nt.nodes.new('ShaderNodeMixShader')
tc=nt.nodes.new('ShaderNodeTexCoord'); sp=nt.nodes.new('ShaderNodeSeparateXYZ'); nt.links.new(tc.outputs['Generated'],sp.inputs[0])
def mth(op,a=None,b=None,clamp=False):
    n=nt.nodes.new('ShaderNodeMath'); n.operation=op; n.use_clamp=clamp
    if a is not None: nt.links.new(a,n.inputs[0]) if not isinstance(a,float) else setattr(n.inputs[0],'default_value',a)
    if b is not None: nt.links.new(b,n.inputs[1]) if not isinstance(b,float) else setattr(n.inputs[1],'default_value',b)
    return n.outputs[0]
du=mth('ABSOLUTE',mth('SUBTRACT',sp.outputs[0],0.5)); dv=mth('ABSOLUTE',mth('SUBTRACT',sp.outputs[1],0.5))
u2=mth('MULTIPLY',du,2.0); v2=mth('MULTIPLY',dv,2.0)
d=mth('SQRT',mth('ADD',mth('MULTIPLY',u2,u2),mth('MULTIPLY',v2,v2)))
mr=nt.nodes.new('ShaderNodeMapRange'); mr.inputs[1].default_value=0.45; mr.inputs[2].default_value=1.0; mr.inputs[3].default_value=1.0; mr.inputs[4].default_value=0.0; mr.clamp=True
nt.links.new(d,mr.inputs[0])
nz=nt.nodes.new('ShaderNodeTexNoise'); nz.inputs['Scale'].default_value=9; nz.inputs['Detail'].default_value=6; nt.links.new(tc.outputs['Object'],nz.inputs['Vector'])
nm=nt.nodes.new('ShaderNodeMapRange'); nm.inputs[1].default_value=0.35; nm.inputs[2].default_value=0.60; nm.inputs[3].default_value=0.15; nm.inputs[4].default_value=1.0; nm.clamp=True; nt.links.new(nz.outputs['Fac'],nm.inputs[0])
a=mth('MULTIPLY',mr.outputs[0],nm.outputs[0]); a=mth('MULTIPLY',a,1.0)
nt.links.new(a,mx.inputs[0]); nt.links.new(tr.outputs[0],mx.inputs[1]); nt.links.new(em.outputs[0],mx.inputs[2]); nt.links.new(mx.outputs[0],o_.inputs['Surface'])
em.inputs['Color'].default_value=(0.86,0.95,0.97,1); em.inputs['Strength'].default_value=1.0
def foam_plane(x,y,axis):
    bpy.ops.mesh.primitive_plane_add(size=1,location=(x,y,0.0)); o=bpy.context.object
    # dimensioni in locale della zattera (root scala 0.9, z abbassato): z locale per avere z mondo 0.002
    o.location=(x,y,(0.002+0.2)/0.9)
    ln,wd=bl+0.36,bd+0.34
    o.scale=(wd,ln,1) if axis=='y' else (ln,wd,1)
    o.data.materials.append(fm); o.parent=root
for i in range(nL):
    x=-L/2+bd/2+i*(L-bd)/(nL-1)
    foam_plane(x,W/2+0.02,'y'); foam_plane(x,-W/2-0.02,'y')
for i in range(nW):
    foam_plane(L/2+0.02,-0.585+i*0.39,'x'); foam_plane(-L/2-0.02,-0.585+i*0.39,'x')
# tent
tm=bpy.data.meshes.new('tent'); 
vs=[(-0.45,-0.35,0),(0.45,-0.35,0),(0.45,0.35,0),(-0.45,0.35,0),(-0.45,0,0.55),(0.45,0,0.55)]
fs=[(0,1,5,4),(2,3,4,5),(0,4,3),(1,2,5)]
tm.from_pydata(vs,[],fs); tm.update()
to=bpy.data.objects.new('tent',tm); sc.collection.objects.link(to); to.location=(-0.85,-0.45,ZD+0.04)
to.rotation_euler[2]=0.35; to.data.materials.append(cloth); to.parent=root
bpy.context.view_layer.objects.active=to
for p in [(-0.1,-0.2,0.28),(0.2,-0.18,0.15)]:
    bpy.ops.mesh.primitive_cube_add(size=1,location=(0,0,0)); o=bpy.context.object; o.scale=(0.2,0.01,0.18)
    o.location=(-0.85+p[0],-0.45-0.2+0.0,ZD+0.04+p[2]); o.rotation_euler=(-0.7,0,0.35); put(o,patch)
# crate, cans, mast
box((-0.15,-0.5,ZD+0.28),(0.36,0.36,0.36),crate,0.2)
box((0.35,-0.6,ZD+0.24),(0.26,0.12,0.36),red,0.3)
box((0.55,-0.55,ZD+0.24),(0.26,0.12,0.36),green,0.15)
cyl((1.05,0.5,ZD+0.55),0.09,1.0,cloth,v=16)
for z in (0.2,0.45,0.7): cyl((1.05,0.5,ZD+z),0.105,0.05,rope,v=16)
cyl((1.05,0.5,ZD+1.12),0.07,0.25,crate,v=12)
# acqua: piano holdout a z=0, la parte immersa sparisce
bpy.ops.mesh.primitive_plane_add(size=20,location=(0,0,0)); wp=bpy.context.object; wp.is_holdout=True
# camera
cam=bpy.data.cameras.new('c'); cam.type='ORTHO'; cam.ortho_scale=704/181.0
co=bpy.data.objects.new('c',cam); sc.collection.objects.link(co); sc.camera=co
el=math.radians(30); az=math.radians(45); d=20
co.location=(d*math.cos(el)*math.sin(az)*-1+0, -d*math.cos(el)*math.cos(az), d*math.sin(el))
co.location=(d*math.cos(el)*math.cos(az), -d*math.cos(el)*math.sin(az), d*math.sin(el))
co.rotation_euler=(math.radians(90)-el,0,math.radians(90)-az)
cam.shift_y=80/704.0
# light
sun=bpy.data.lights.new('s','SUN'); sun.energy=4.5; sun.angle=math.radians(8)
so=bpy.data.objects.new('s',sun); sc.collection.objects.link(so); so.rotation_euler=(math.radians(50),math.radians(10),math.radians(-35))
w=bpy.data.worlds.new('w'); sc.world=w; w.use_nodes=True
w.node_tree.nodes['Background'].inputs[0].default_value=(0.55,0.62,0.7,1); w.node_tree.nodes['Background'].inputs[1].default_value=0.9
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=int(os.environ.get('SMP','40')); sc.cycles.use_denoising=True
sc.render.resolution_x=704; sc.render.resolution_y=512; sc.render.film_transparent=True
sc.render.image_settings.file_format='PNG'; sc.render.image_settings.color_mode='RGBA'
sc.view_settings.view_transform='Standard'
angs=[float(a) for a in os.environ.get('ANG','0').split(',')]
for a in angs:
    root.rotation_euler[2]=math.radians(a)
    sc.render.filepath=os.environ.get('OUT','/home/claude/blender3d/out')+'/raft_%05.1f.png'%a
    bpy.ops.render.render(write_still=True)
