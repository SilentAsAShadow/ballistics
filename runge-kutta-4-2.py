# Python script to impletement Runge-Kutta 4th
# Order Method to determine the trajectory of
# a projectile with air resistance.


def f(t, v, g, m, k):
    kmv = np.linalg.norm(v)*(k/m)
    return (g - kmv*v)


def RK4(tn, xn, vn, h, g, m, k):

    k1 = f(tn, vn, g, m, k)
    k2 = f(tn + h/2, vn + k1*h/2, g, m, k)
    k3 = f(tn + h/2, vn + k2*h/2, g, m, k)
    k4 = f(tn + h, vn + k3*h, g, m, k)
    vn1 = vn + (k1 + 2*k2 + 2*k3 + k4)*(h/6)

    k1x = vn
    k2x = vn + k1x*h/2
    k3x = vn + k2x*h/2
    k4x = vn + k3x*h
    xn1 = xn + (k1x + 2*k2x + 2*k3x + k4x)*(h/6)

    return vn1, xn1


theta = math.radians(30)
 v0 = np.array([math.cos(theta), math.sin(theta)])
 x0 = np.array([0, 0])
 t0 = 0
 x = []
 v = []
 t = []
 x.append(x0)
 v.append(v0)
 t.append(t0)

 m = 1
 k = 0.01
 g = np.array([0, -9.81])
 h = 0.01

 tn = t0
 vn = v0
 xn = x0
 maxt = 1

 while (t < maxt):
   vn, xn = RK4(tn, xn, vn, h, g, m, k)
   tn = tn + h
   t.append(tn)
   x.append(xn)
   v.append(vn)

 print t[-1]
 print x[-1]
 print v[-1]
 
