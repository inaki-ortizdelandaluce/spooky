KPL/FK

Topocentric Frame kernel for the JAXA deep space stations
=========================================================

   This is a frame kernel defining a topocentric reference frame for the JAXA
   deep space stations. Location data used to define this frame are taken from
   the JAXA web pages.


Version and Date
-----------------------------------------------------------------------------

    Version 0.0 -- September 4, 2023 -- Rafael Andres Blasco, ESAC/ESA

       Added Usuda Deep Space Center and Misasa Deep Space Station.


References
-----------------------------------------------------------------------------

   1. ``Frames Required Reading'', NAIF

   2. ``Kernel Pool Required Reading'', NAIF

   3. ``C-Kernel Required Reading'', NAIF

   4. https://www.isas.jaxa.jp/en/about/facilities/usuda.html

   5. https://www.isas.jaxa.jp/home/great/english/profile1001en.html


Contact Information
-----------------------------------------------------------------------------

   If you have any questions regarding this file contact the ESA SPICE
   Service at ESAC:

           Alfredo Escalante Lopez
           (+34) 91-8131-429
           spice@sciops.esa.int


Implementation Notes
-----------------------------------------------------------------------------

   This file is used by the SPICE system as follows: programs that make use
   of this frame kernel must "load" the kernel normally during program
   initialization. Loading the kernel associates the data items with
   their names in a data structure called the "kernel pool".  The SPICELIB
   routine FURNSH loads a kernel into the pool as shown below:

     FORTRAN: (SPICELIB)

       CALL FURNSH ( frame_kernel_name )

     C: (CSPICE)

       furnsh_c ( frame_kernel_name );

     IDL: (ICY)

       cspice_furnsh, frame_kernel_name

     MATLAB: (MICE)

          cspice_furnsh ( 'frame_kernel_name' )

     PYTHON: (SPICEYPY)*

          furnsh( frame_kernel_name )

   In order for a program or routine to extract data from the pool, the
   SPICELIB routines GDPOOL, GIPOOL, and GCPOOL are used.  See [2] for
   more details.

   This file was created and may be updated with a text editor or word
   processor.

   * SPICEYPY is a non-official, community developed Python wrapper for the
     NAIF SPICE toolkit. Its development is managed on Github.
     It is available at: https://github.com/AndrewAnnex/SpiceyPy


JAXA Deep Space Stations Frames
-----------------------------------------------------------------------------

   The topocentric frame defines the z axis as the normal outward at the
   station site, the x axis points at local north (geographic) with the
   y axis completing the right handed frame.  Positive azimuth is measured
   counter clockwise from the x axis.

   The equatorial radius and flattening factor for the ITRF93
   reference ellipsoid are

      radius      = 6378.1363
      flattening  = 1.0/298.257

   Please note that all rotations mean the rotation of the coordinate
   frames about an axis and not of the vectors.

   The rotation defined in this file transforms vectors from
   the topocentric frame defined as

      z - normal to the surface at the site
      x - local north
      y - local west

   to an earth-fixed frame defined as

      x - along the line of zero longitude intersecting the equator
      z - along the spin axis
      y - completing the right hand coordinate frame

   This is a 3-2-3 rotation with angles defined as the negative of the site
   longitude, the negative of the site colatitude, 180 degrees.

   This file uses the reference frame alias EARTH_FIXED.
   In order to use this file in a SPICE-based program,
   the alias must be mapped to the frames ITRF93 or IAU_EARTH
   by a text kernel.  An example of the text kernel assignments
   mapping EARTH_FIXED to ITRF93 is:

      TKFRAME_EARTH_FIXED_RELATIVE = 'ITRF93'
      TKFRAME_EARTH_FIXED_SPEC     = 'MATRIX'
      TKFRAME_EARTH_FIXED_MATRIX   = ( 1   0   0
                                       0   1   0
                                       0   0   1 )


   These assignments must be preceded by the \begindata marker
   alone on a line.

   See the Frames Required Reading for details.

   The ITRF93 frame should be used for high-accuracy work.  A binary
   high-precision earth PCK file should be used to convert the station
   location from terrestrial to inertial coordinates.

   Disclaimer:
   ~~~~~~~~~~~

      Please note that the accuracy of these coordinates is in accordance with
      the public information provided by JAXA.

   Body-name mapping follows:
 
   \begindata

      NAIF_BODY_NAME                      += 'USUDA'
      NAIF_BODY_CODE                      += 399700

      NAIF_BODY_NAME                      += 'MISASA'
      NAIF_BODY_CODE                      += 399701

   \begintext
 
   The data for the ground stations topocentric frames is defined as follows.
 
   \begindata
 
      FRAME_USUDA_TOPO                    =  1399700
      FRAME_1399700_NAME                  =  'USUDA_TOPO'
      FRAME_1399700_CLASS                 =  4
      FRAME_1399700_CLASS_ID              =  1399700
      FRAME_1399700_CENTER                =  399700

      OBJECT_399700_FRAME                 =  'USUDA_TOPO'

      TKFRAME_1399700_RELATIVE            =  'EARTH_FIXED'
      TKFRAME_1399700_SPEC                =  'ANGLES'
      TKFRAME_1399700_UNITS               =  'DEGREES'
      TKFRAME_1399700_AXES                =  ( 3, 2, 3 )
      TKFRAME_1399700_ANGLES              =  ( -138.3629000000000,
                                             -53.8676400000000,
                                             180.0000000000000 )


      FRAME_MISASA_TOPO                   =  1399701
      FRAME_1399701_NAME                  =  'MISASA_TOPO'
      FRAME_1399701_CLASS                 =  4
      FRAME_1399701_CLASS_ID              =  1399701
      FRAME_1399701_CENTER                =  399701

      OBJECT_399701_FRAME                 =  'MISASA_TOPO'

      TKFRAME_1399701_RELATIVE            =  'EARTH_FIXED'
      TKFRAME_1399701_SPEC                =  'ANGLES'
      TKFRAME_1399701_UNITS               =  'DEGREES'
      TKFRAME_1399701_AXES                =  ( 3, 2, 3 )
      TKFRAME_1399701_ANGLES              =  ( -138.3528600000000,
                                             -53.8583900000000,
                                             180.0000000000000 )


   \begintext


End of FK file.
