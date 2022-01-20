

from pyHIARD.common_functions import download_cube,create_masks
from astropy.io import fits
import os

galaxy_parameters = {'Galaxy': 'NGC_2903', 'DHIkpc': 51.9   ,'Distance': 8.7, 'Original_Model': 'Tir', 'RMS': 0.0033  , 'MHI': 3.9e9   }


def get_data():
    '''Download the data for this galaxy and prepare the cube for usage'''
    succes= False
    outdir = os.path.dirname(os.path.abspath(__file__))
    try:
        Cube = fits.open(f"{outdir}/NGC_2903.fits",uint = False, do_not_scale_image_data=True,ignore_blank = True)
    except FileNotFoundError:
        url = 'https://github.com/PeterKamphuis/pyFAT-astro/raw/main/pyFAT_astro/Installation_Check/NGC_2903.fits'
        name = 'NGC_2903'
        sizes=[[0,-1],[0,-1],[0,-1]]
        Cube = download_cube(name,url,sizes,outdir)

    #place_disclaimer(dir_to_place)
    return Cube
get_data.__doc__=f'''
NAME:
   get_data

PURPOSE:
   Download the data for this galaxy and prepare the cube for usage

CATEGORY:
   agc

INPUTS:

OPTIONAL INPUTS:


OUTPUTS:
   Cube = Cube in astropy format

OPTIONAL OUTPUTS:

PROCEDURES CALLED:
   Unspecified

NOTE:
'''

def get_masks(dir_to_place,sofia_call='sofia2'):
    '''Get or create the masks for a galaxy'''
    name = 'NGC_2903'
    outdir = os.path.dirname(os.path.abspath(__file__))
    try:
        for type in ['inner','outer']:
            if type == 'inner':
                Mask_Inner = fits.open(f"{outdir}/Inner_{name}_mask.fits", uint=False,
                               do_not_scale_image_data=True, ignore_blank=True)
            else:
                Mask_Outer = fits.open(f"{outdir}/Outer_{name}_mask.fits", uint=False,
                               do_not_scale_image_data=True, ignore_blank=True)
    except FileNotFoundError:
        Mask_Inner, Mask_Outer = create_masks(outdir,dir_to_place,name,sofia_call=sofia_call)
    return Mask_Inner,Mask_Outer
get_masks.__doc__=f'''
NAME:
   get_masks

PURPOSE:
   Get or create the masks for a galaxy

CATEGORY:
   agc

INPUTS:
    dir_to_place = The directory where the galaxy is to be created.

OPTIONAL INPUTS:
    sofia_call = command name for sofia

OUTPUTS:
   Inner Mask = the inner edge mask
   Outer Mask = the Outer edge mask

OPTIONAL OUTPUTS:

PROCEDURES CALLED:
   Unspecified

NOTE:
'''


def place_disclaimer(dir_to_place):
    disclaimer = '''----- NCG 2903 -----

  This galaxy is from the WHISP survey.
  The data for this galaxy were take as part of the WHISP program. This survey is decribed in van der Hulst et al. (2001) and the data can be found at Westerbork on the Web or the WHISP page.

  The model used here is the previous GDL FAT Release of v2.0.1 where it is used as an Installation check.
  Other models can be found in

  https://arxiv.org/pdf/1601.01689.pdf

  and the SPARC database  (http://astroweb.cwru.edu/SPARC/)
'''
    with open(f'{dir_to_place}/ACKNOWLEDGE_WHISP.txt', 'w') as file:
        file.writelines(disclaimer)
place_disclaimer.__doc__=f'''
NAME:
   place_disclaimer

PURPOSE:
   Place a disclaimer about the source, models and acknowledgements in the directory.

CATEGORY:
   agc

INPUTS:
    dir_to_place = The directory where the galaxy is cretated.

OPTIONAL INPUTS:


OUTPUTS:

OPTIONAL OUTPUTS:

PROCEDURES CALLED:
   Unspecified

NOTE:
'''
