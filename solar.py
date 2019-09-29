from vpython import *
from tkinter import *


def gforce(p1,p2):
    # Calculate the gravitational force exerted on p1 by p2.
    G = 1 
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
def system(sun_m, orbit_rate):
    scene1 = canvas(title='Solar System',
         width=1000, height=1000,
         center=vector(0,0,0))
    force_graph = graph(xtitle="X-PLANE", ytitle = "Z-PLANE",title='<b>Pluto and Neptune crossed orbit</b>')
    force_graph = gcurve(color=color.blue, label='PLUTO ANGULAR ORBIT')
    force_graph_2 = gcurve(color=color.red, label='NEPTUNE ANGULAR ORBIT')

    astroid_graph = graph(xtitle="time", ytitle = "force",title='<b>Force Acting on Astroid By The Sun</b>')
    astroid_graph = gcurve(color=color.blue, label='Force On Astroid')
    star = sphere( pos=vector(0,0,0), radius=2.5, color=color.yellow,
                   mass = sun_m, momentum=vector(0,0,0), make_trail=True,retain= 3500,texture='sun.jpg' )
    earth = sphere( pos=vector(9,0,0), radius=0.6, color=color.white,
                   mass = 1, momentum=vector(0,26,0), make_trail=True,retain= 3500,texture='earth.jpg'  )
    venus = sphere( pos=vector(7,0,0), radius=0.5, color=color.white,
                   mass = 1.1, momentum=vector(0,31,0), make_trail=True,retain= 3500,texture='venus.jpg'  )

    mercury = sphere( pos=vector(5,0,0), radius=0.4, color=color.white,
                   mass = 1.0, momentum=vector(0,31,0), make_trail=True,retain= 3500,texture='mercury.jpg'  )


    mars = sphere( pos=vector(11,0,0), radius=0.5, color=color.white,
                   mass = 1.3, momentum=vector(0,31,0), make_trail=True,retain= 3500,texture='mars.jpg'  )

    jupiter = sphere( pos=vector(13,0,0), radius=2, color=color.white,
                   mass = 1.4, momentum=vector(0,31.5,0), make_trail=True,retain= 3500,texture='jupiter.jpg'  )

    saturn = sphere( pos=vector(17,0,0), radius=1.9, color=color.white,
                   mass = 2.0, momentum=vector(0,40,0), make_trail=True,retain= 3050,texture='saturn.jpg'  )

    uranus = sphere( pos=vector(21,0,0), radius=1.3, color=color.white,
                   mass = 2.2, momentum=vector(0,40,0), make_trail=True,retain= 3050,texture='uranus.jpg'  )

    neptune = sphere( pos=vector(26,0,0), radius=1.4, color=color.white,
                   mass = 2.53, momentum=vector(0,40,0), make_trail=True,retain= 3050,texture='neptune.jpg'  )

    pluto = sphere( pos=vector(27,0,0), radius=0.4, color=color.blue,
                   mass = 2.64, momentum=vector(0,40,20), make_trail=True,retain= 3050,texture='pluto.jpg'  )


    met = sphere( pos=vector(-100,0,-30), radius=2, color=color.red,
                   mass = 2.64, momentum=vector(50,15,9), make_trail=True,retain= 3050,texture='pluto.jpg'  )

    dt = 0.0009
    t = 0

    
    asteroids = []
    rmin = 6
    rmax = 30
    mmin = 0.1
    mmax = 0.3
    for i in range(0,40):
        r = rmin + random()*(rmax-rmin)
        theta = random()*2*pi
        mass = mmin + random()*(mmax-mmin)
        momentum = mass*sqrt(star.mass/r)
        ecc = 0.8+random()*(1.2-0.8)
        asteroids.append( sphere( pos=r*vector(cos(theta),sin(theta),0),
                                  momentum=ecc*momentum*vector(-sin(theta),cos(theta),0),
                                  mass=mass, color=color.white, radius=0.15 ) )
        asteroids.append( sphere( pos=r*vector(cos(theta),sin(theta),0),
                                  momentum=ecc*momentum*vector(-sin(theta),cos(theta),-sin(theta)),
                                  mass=mass, color=color.white, radius=0.15 ) )

    while (True):
        rate(orbit_rate)

        # Calculate force
        star.force = gforce(star,earth)
        earth.force = gforce(earth,star)
        venus.force = gforce(venus,star)
        mercury.force = gforce(mercury,star)
        mars.force = gforce(mars,star)
        jupiter.force = gforce(jupiter,star)
        saturn.force = gforce(saturn,star)
        uranus.force = gforce(uranus,star)
        neptune.force = gforce(neptune,star)
        pluto.force = gforce(pluto,star)
        met.force = gforce(met,star)*2

        for a in asteroids:
            a.force = gforce(a,star)+gforce(a,earth)+gforce(a,venus)+gforce(a,mercury)
            +gforce(a,mars)+gforce(a,jupiter)+gforce(a,saturn)+gforce(a,uranus)+gforce(a,neptune)+gforce(a,pluto)                 

        # Update momentum
        star.momentum = star.momentum + star.force*dt
        earth.momentum = earth.momentum + earth.force*dt
        venus.momentum = venus.momentum + venus.force*dt
        mercury.momentum = mercury.momentum + mercury.force*dt
        mars.momentum = mars.momentum + mars.force*dt
        jupiter.momentum = jupiter.momentum + jupiter.force*dt
        saturn.momentum = saturn.momentum + saturn.force*dt
        uranus.momentum = uranus.momentum + uranus.force*dt
        neptune.momentum = neptune.momentum + neptune.force*dt
        pluto.momentum = pluto.momentum + pluto.force*dt
        met.momentum = met.momentum + met.force*dt


        for a in asteroids:
            a.momentum = a.momentum + a.force*dt


        # Update positions
        star.pos = star.pos + star.momentum/star.mass*dt
        earth.pos = earth.pos + earth.momentum/earth.mass*dt
        venus.pos = venus.pos + venus.momentum/venus.mass*dt
        mercury.pos = mercury.pos + mercury.momentum/mercury.mass*dt
        mars.pos = mars.pos + mars.momentum/mars.mass*dt
        jupiter.pos = jupiter.pos + jupiter.momentum/jupiter.mass*dt
        saturn.pos = saturn.pos + saturn.momentum/saturn.mass*dt
        uranus.pos = uranus.pos + uranus.momentum/uranus.mass*dt
        neptune.pos = neptune.pos + neptune.momentum/neptune.mass*dt
        pluto.pos = pluto.pos + pluto.momentum/pluto.mass*dt
        met.pos = met.pos + met.momentum/met.mass*dt

        force_graph.plot(pos=(pluto.momentum.x, pluto.momentum.z))
        force_graph_2.plot(pos=(neptune.momentum.x, neptune.momentum.z))
        astroid_graph.plot(pos=(t, met.force.y))

        for a in asteroids:
            a.pos = a.pos + a.momentum/a.mass*dt
        t = t + dt

#system()

window = Tk()
window.title("Solar System Simulation")
window.geometry('700x600')

simulation_txt = Label(window, text="Solar System", font=("Arial Bold", 15))
simulation_txt.grid(column=0, row=0)

orbit_rate_label = Label(window, text="Orbit Rate: ") # Label for entry box(orbit rate)
orbit_rate_label.grid(column=0, row = 8) # Grid positioning for label
orbit_rate_default = StringVar(window, value='400')  # Sets default value for orbit rate entry
orbit_rate_entry = Entry(window,width=10,textvariable=orbit_rate_default) # Creats orbit rate entry field
orbit_rate_entry.grid(column=1, row=8)  # Grid positioning for entry field

sun_m_label = Label(window, text="Mass - Sun: ")
sun_m_label.grid(column=0, row=1)
sun_m_default = StringVar(window, value='5000')
sun_m_entry = Entry(window,width=10,textvariable=sun_m_default)
sun_m_entry.grid(column=1, row=1)

earth_tilt_label = Label(window, text="Tilt - Earth: ")
earth_tilt_label.grid(column=2, row=1)
earth_tilt_default = StringVar(window, value='0')
earth_tilt_entry = Entry(window,width=10,textvariable=earth_tilt_default)
earth_tilt_entry.grid(column=3, row=1)

def passToSimulation(): # Function passes parameters so simulation, converts paramter to integer
    
    orbit_rate = int(orbit_rate_entry.get())
    sun_m = int(sun_m_entry.get())
    
    system(sun_m, orbit_rate)

def returnToMenu():
    
    window.destroy()
    import main_menu
 
begin_simulation = Button(window, text="Begin Simulation: ", command=passToSimulation)
begin_simulation.grid(column=0, row=11)

return_btn = Button(window, text="Return to Simulations: ", command=returnToMenu)
return_btn.grid(column=0, row=12)

window.mainloop()

