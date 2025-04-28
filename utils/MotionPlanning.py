import numpy as np
from scipy import signal
global Tf
Tf = 100

# Xd, Yd, Zd — desired position in X, Y, and Z.
# dXd, dYd, dZd — velocities in the X, Y, and Z directions.
# ddXd, ddYd, ddZd — accelerations in the X, Y, and Z directions.
# phid, Ttad, Psid — desired roll, pitch, and yaw angles.
# dphid, dTtad, dPsid — desired rates of the angles.
# ddphid, ddTtad, ddPsid — desired accelerations of the angles.

def CreateDesiredTrajectory(t):
    
    global Tf
    # ------- Static point
    Xd = 0;    Yd = 0;    Zd = 0;    
    dXd = 0;    dYd = 0;    dZd = 0;    
    ddXd = 0;    ddYd = 0;    ddZd = 0;
    
    phid = 0;   Ttad = 0;   Psid = 0;    
    dphid = 0;  dTtad = 0;  dPsid = 0;    
    ddphid = 0; ddTtad = 0; ddPsid = 0;
    
    ## -------- Square path
    # Xd = 1+signal.square(4 * np.pi / Tf * t);
    # Yd = 1+signal.square(4 * np.pi / Tf * (t- Tf/8 ));
    # Zd = 1;    
    # dXd = 0;    dYd = 0;    dZd = 0;    
    # ddXd = 0;    ddYd = 0;    ddZd = 0;
    
    # phid = 0;   Ttad = 0;   Psid = 0;    
    # dphid = 0;  dTtad = 0;  dPsid = 0;    
    # ddphid = 0; ddTtad = 0; ddPsid = 0;
    
    ## -------- Helical Path
    # r = 1; w = 4*np.pi/Tf;a = np.deg2rad(5);
    # Xd = r*np.cos(w*t);
    # Yd = r*np.sin(w*t);
    # Zd = 0.05*t;
    
    # dXd = -r*w*np.sin(w*t);
    # dYd = r*w*np.cos(w*t);
    # dZd = 0.05;
    
    # ddXd = -r*w**2*np.cos(w*t);
    # ddYd = -r*w**2*np.sin(w*t);
    # ddZd = 0;
    
    # phid = 0;    Ttad = 0;    Psid = 0;    
    # dphid = 0;    dTtad = 0;    dPsid = 0;    
    # ddphid = 0;    ddTtad = 0;    ddPsid = 0;

    # -------Sine Path
    # A = 1  # Amplitude in X direction
    # B = 1  # Amplitude in Y direction
    # C = 0.5  # Amplitude in Z direction
    # omega = 2 * np.pi / Tf  # Frequency for X and Y
    # k = 2 * np.pi / Tf  # Frequency for Z
        
    # Xd = A * np.sin(omega * t)
    # Yd = B * np.cos(omega * t)
    # Zd = C * np.sin(k * t)
        
    # dXd = A * omega * np.cos(omega * t)
    # dYd = -B * omega * np.sin(omega * t)
    # dZd = C * k * np.cos(k * t)
        
    # ddXd = -A * omega**2 * np.sin(omega * t)
    # ddYd = -B * omega**2 * np.cos(omega * t)
    # ddZd = -C * k**2 * np.sin(k * t)

    # phid = 0;    Ttad = 0;    Psid = 0;    
    # dphid = 0;    dTtad = 0;    dPsid = 0;    
    # ddphid = 0;    ddTtad = 0;    ddPsid = 0;


    # ------- Circular Path
    # radius = 1  # Radius of the circle
    # omega = 2 * np.pi / Tf  # Angular velocity
    # Zd = 1  # Constant altitude
        
    # Xd = radius * np.cos(omega * t)
    # Yd = radius * np.sin(omega * t)
    # dXd = -radius * omega * np.sin(omega * t)
    # dYd = radius * omega * np.cos(omega * t)
    # ddXd = -radius * omega**2 * np.cos(omega * t)
    # ddYd = -radius * omega**2 * np.sin(omega * t)
    # ddZd = 0  # No change in Z for circular path

    # phid = 0;    Ttad = 0;    Psid = 0;    
    # dphid = 0;    dTtad = 0;    dPsid = 0;    
    # ddphid = 0;    ddTtad = 0;    ddPsid = 0;


    # ------- Parabolic Path
    # alpha = 0.01  # X direction curvature
    # beta = 0.01   # Y direction curvature
    # gamma = 0.005 # Z direction curvature
        
    # Xd = alpha * t**2
    # Yd = beta * t**2
    # Zd = gamma * t**2
        
    # dXd = 2 * alpha * t
    # dYd = 2 * beta * t
    # dZd = 2 * gamma * t
        
    # ddXd = 2 * alpha
    # ddYd = 2 * beta
    # ddZd = 2 * gamma
    
    # phid = 0;    Ttad = 0;    Psid = 0;    
    # dphid = 0;    dTtad = 0;    dPsid = 0;    
    # ddphid = 0;    ddTtad = 0;    ddPsid = 0;

    
    DesAttitude = np.array([phid,dphid,ddphid,Ttad,dTtad,ddTtad,Psid,dPsid,ddPsid]);
    DesPosition = np.array([Zd,dZd,ddZd,Xd,dXd,ddXd,Yd,dYd,ddYd]);
    
    return DesPosition, DesAttitude