import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage import transform
import math


palawan = imread('ImageTestPtut1.png')
imshow(palawan);

imgMatrice = asarray(palawan)




area_of_interestRed = [(0, 0),
                    (424, 0),
                    (424, 600),
                    (0, 600)]
area_of_projectionRed = [(0, 50),
                      (424, 150),
                      (424, 400),
                      (0, 500)]

area_of_interestBlue = [(424, 0),
                    (848, 0),
                    (848, 600),
                    (424, 600)]
area_of_projectionBlue = [(424, 150),
                      (848, 50),
                      (848, 500),
                      (424, 400)]

area_of_interestYellow = [(0, 600),
                    (0, 1200),
                    (424, 1200),
                    (424, 600)]
area_of_projectionYellow = [(0, 650),
                      (424, 750),
                      (424, 1000),
                      (0, 1100)]

area_of_interestGreen = [(424, 600),
                    (424, 1200),
                    (848, 1200),
                    (848, 600)]

area_of_projectionGreen = [(424, 750),
                      (848, 650),
                      (848, 1100),
                      (424, 1000)]

def project_planesRed(image, src, dst):

    x_src = [val[0] for val in src] + [src[0][0]]
    y_src = [val[1] for val in src] + [src[0][1]]
    x_dst = [val[0] for val in dst] + [dst[0][0]]
    y_dst = [val[1] for val in dst] + [dst[0][1]]

    fig, ax = plt.subplots(1,2, figsize=(13,6))

    new_image = image.copy() 
    projection = np.zeros_like(new_image)
    ax[0].imshow(new_image);
    ax[0].plot(x_src, y_src, 'r--')
    ax[0].set_title('Area of Interest Red')
    ax[1].imshow(projection)
    ax[1].plot(x_dst, y_dst, 'r--')
    ax[1].set_title('Area of Projection Red')
 
def project_planesBlue(image, src, dst):
    x_src = [val[0] for val in src] + [src[0][0]]
    y_src = [val[1] for val in src] + [src[0][1]]
    x_dst = [val[0] for val in dst] + [dst[0][0]]
    y_dst = [val[1] for val in dst] + [dst[0][1]]

    fig, ax = plt.subplots(1,2, figsize=(13,6))

    new_image = image.copy() 
    projection = np.zeros_like(new_image)
    ax[0].imshow(new_image);
    ax[0].plot(x_src, y_src, 'r--')
    ax[0].set_title('Area of Interest Blue')
    ax[1].imshow(projection)
    ax[1].plot(x_dst, y_dst, 'r--')
    ax[1].set_title('Area of Projection Blue')  

def project_planesYellow(image, src, dst):
    x_src = [val[0] for val in src] + [src[0][0]]
    y_src = [val[1] for val in src] + [src[0][1]]
    x_dst = [val[0] for val in dst] + [dst[0][0]]
    y_dst = [val[1] for val in dst] + [dst[0][1]]

    fig, ax = plt.subplots(1,2, figsize=(13,6))

    new_image = image.copy() 
    projection = np.zeros_like(new_image)
    ax[0].imshow(new_image);
    ax[0].plot(x_src, y_src, 'r--')
    ax[0].set_title('Area of Interest Yellow')
    ax[1].imshow(projection)
    ax[1].plot(x_dst, y_dst, 'r--')
    ax[1].set_title('Area of Projection Yellow')   
    
def project_planesGreen(image, src, dst):
    x_src = [val[0] for val in src] + [src[0][0]]
    y_src = [val[1] for val in src] + [src[0][1]]
    x_dst = [val[0] for val in dst] + [dst[0][0]]
    y_dst = [val[1] for val in dst] + [dst[0][1]]

    fig, ax = plt.subplots(1,2, figsize=(13,6))

    new_image = image.copy() 
    projection = np.zeros_like(new_image)
    ax[0].imshow(new_image);
    ax[0].plot(x_src, y_src, 'r--')
    ax[0].set_title('Area of Interest Green')
    ax[1].imshow(projection)
    ax[1].plot(x_dst, y_dst, 'r--')
    ax[1].set_title('Area of Projection Green')     
    
#project_planesRed(palawan, area_of_interestRed, area_of_projectionRed)
#project_planesBlue(palawan, area_of_interestBlue, area_of_projectionBlue)
#project_planesYellow(palawan, area_of_interestYellow, area_of_projectionYellow)
#project_planesGreen(palawan, area_of_interestGreen, area_of_projectionGreen)


def project_transform(image, src, dst):
    x_dst = [val[0] for val in dst] + [dst[0][0]]
    y_dst = [val[1] for val in dst] + [dst[0][1]]
    
    tform = transform.estimate_transform('projective', 
                                         np.array(src), 
                                         np.array(dst))
    
    transformed = transform.warp(image, tform.inverse)
    
    plt.figure(figsize=(6,6))
    plt.imshow(transformed)
    plt.plot(x_dst, y_dst, 'r--')
    
#project_transform(palawan, area_of_interestRed,area_of_interestBlue, area_of_projectionRed,area_of_projectionBlue)
project_transform(palawan, area_of_interestGreen, area_of_projectionGreen)
project_transform(palawan, area_of_interestYellow, area_of_projectionYellow)


def transformation_point (Xi,Yi,Zi, dm, f):
    
    f = 132 #premiere valeure brut trouvee / disantce focal miroir
    
    Rho = math.sqrt((Xi^2)+(Yi^2)+(Zi^2))
    Phi = np.arctan(Yi/Xi)
    Teta = np.arccos(Zi/Rho)
    
    
def callibrage ():
    
    Mi(xi,yi,zi) : xi/x1 = f/dm <=> x1 = (xidm)/f y1 = (yidm)/f

    M1 =(x1,y1, dO+dm)
    O'M1=(x1,y1,-dm)
    O'M2= Delta O'M1 = Alpha ((x1,y1,-dm))
    CM2 = CO' + O'M2 = (Delta (xi * dm))/f, Delta (yi * dm))/f, dO+2dm-Deltadm)
    
    Alpha = Delta
    a = dm²(1+ xi²+yi²/f²)
    b= -2dm(dO+2dm)
    c= (dO+ 2dm)²-R²
    
    Alpha 1 = -b + sqrt(b²-4ac)/2a
    
    Zm2 > R-h
    
    N = 1/rCM2
    V1 = M2M1/Norme(M2M1), V2= 2(NV1)N-V1 (R cours ASI)
    CM= CM2+M2M = CM2+ T*V2
    
    MplanX = -dxmax/2 -> t 
    
    Yt et Zt : Pz <= Zt<=Pz+dzMax
    -dymax/2 <=yt<=dymax/2
                
    return callibrateMatrice
    

    

    

    

    