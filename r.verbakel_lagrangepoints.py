from vpython import *
#GlowScript 2.7 VPython
def gforce(p1,p2):
    # Calculate the gravitational force exerted on p1 by p2.
    G = 1 # Change to 6.67e-11 to use real-world values.
    # Calculate distance vector between p1 and p2.
    r_vec = p1.pos-p2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calcualte unit vector of distance vector.
    r_hat = r_vec/r_mag
    # Calculate force magnitude.
    force_mag = G*p1.mass*p2.mass/r_mag**2
    # Calculate force vector.
    force_vec = -force_mag*r_hat
    
    return force_vec
    
star = sphere( pos=vector(0,0,0), radius=0.2, color=color.yellow,
               mass = 1000, momentum=vector(0,0,0), make_trail=True )
               
planet = sphere( pos=vector(1,0,0), radius=0.04, color=color.blue,
                  mass = 1, momentum=vector(0,32,0), make_trail=False )

l1 = vector( mag(planet.pos-star.pos)*(1-(planet.mass/(3*(planet.mass+star.mass)))**(1/3)) ,0,0 )
l2 = vector( mag(planet.pos-star.pos)*(1+(planet.mass/(3*(planet.mass+star.mass)))**(1/3)) ,0,0 )
l3 = vector( -mag(planet.pos-star.pos)*(1+5*12**-1*planet.mass/(planet.mass+star.mass)), 0, 0 )
l4 = vector(0.5*(star.pos.x+planet.pos.x),0,0)
l4.y = l4.x*tan(pi/3)
l5 = vector(l4.x,-l4.y,0)


lagrange1 = sphere( pos=l1, radius=0.030, color=color.white,
                    mass = 0.01, momentum=vector(0,0,0), make_trail=False )
lagrange2 = sphere( pos=l2, radius=0.030, color=color.white,
                    mass = 0.01, momentum=vector(0,0,0), make_trail=False )
lagrange3 = sphere( pos=l3, radius=0.030, color=color.white,
                    mass = 0.01, momentum=vector(0,0,0), make_trail=False )
lagrange4 = sphere( pos=l4, radius=0.030, color=color.red,
                  mass = 0.01, momentum=vector(0,0,0), make_trail=False )
lagrange5 = sphere( pos=l5, radius=0.030, color=color.red,
                  mass = 0.01, momentum=vector(0,0,0), make_trail=False )

lagrange1.momentum = planet.momentum/planet.mass*lagrange1.mass
lagrange1.momentum = lagrange1.momentum*mag(lagrange1.pos-star.pos)/mag(planet.pos-star.pos)
lagrange2.momentum = planet.momentum/planet.mass*lagrange2.mass
lagrange2.momentum = lagrange2.momentum*mag(lagrange2.pos-star.pos)/mag(planet.pos-star.pos)
lagrange3.momentum = -planet.momentum/planet.mass*lagrange3.mass
lagrange3.momentum = lagrange3.momentum*mag(lagrange3.pos-star.pos)/mag(planet.pos-star.pos)
lagrange4.momentum.x = -planet.momentum.y*sin(pi/3)/planet.mass*lagrange4.mass
lagrange4.momentum.y =  planet.momentum.y*cos(pi/3)/planet.mass*lagrange4.mass
lagrange5.momentum.x = -planet.momentum.y*sin(-pi/3)/planet.mass*lagrange5.mass
lagrange5.momentum.y =  planet.momentum.y*cos(-pi/3)/planet.mass*lagrange5.mass
   
dt = 0.000001
t = 0
while (True):
    rate(10000)
    
    # Calculate forces.
    star.force = gforce(star,planet)
    planet.force = gforce(planet,star)
    lagrange1.force = gforce(lagrange1,star)+gforce(lagrange1,planet)
    lagrange2.force = gforce(lagrange2,star)+gforce(lagrange2,planet)
    lagrange3.force = gforce(lagrange3,star)+gforce(lagrange3,planet)
    lagrange4.force = gforce(lagrange4,star)+gforce(lagrange4,planet)
    lagrange5.force = gforce(lagrange5,star)+gforce(lagrange5,planet)

    # Update momenta.
    star.momentum = star.momentum + star.force*dt
    planet.momentum = planet.momentum + planet.force*dt
    lagrange1.momentum = lagrange1.momentum + lagrange1.force*dt
    lagrange2.momentum = lagrange2.momentum + lagrange2.force*dt
    lagrange3.momentum = lagrange3.momentum + lagrange3.force*dt
    lagrange4.momentum = lagrange4.momentum + lagrange4.force*dt
    lagrange5.momentum = lagrange5.momentum + lagrange5.force*dt

    # Update positions.
    star.pos = star.pos + star.momentum/star.mass*dt
    planet.pos = planet.pos + planet.momentum/planet.mass*dt
    lagrange1.pos = lagrange1.pos + lagrange1.momentum/lagrange1.mass*dt
    lagrange2.pos = lagrange2.pos + lagrange2.momentum/lagrange2.mass*dt
    lagrange3.pos = lagrange3.pos + lagrange3.momentum/lagrange3.mass*dt
    lagrange4.pos = lagrange4.pos + lagrange4.momentum/lagrange4.mass*dt
    lagrange5.pos = lagrange5.pos + lagrange5.momentum/lagrange5.mass*dt
    
    t = t + dt

