KPL/FK
 
   FILE: /tmp/spooky_gs_v00.tf
 
   This file was created by PINPOINT.
 
   PINPOINT Version 3.3.0 --- December 13, 2021
   PINPOINT RUN DATE/TIME:    2024-05-23T12:14:25
   PINPOINT DEFINITIONS FILE: /tmp/pinpoint.defs
   PINPOINT PCK FILE:         /tmp/pck00011.tpc
   PINPOINT SPK FILE:         /tmp/spooky_gs_v00.bsp
 
   The input definitions file is appended to this
   file as a comment block.
 
 
   Body-name mapping follows:
 
\begindata
 
   NAIF_BODY_NAME                      += 'GS0001'
   NAIF_BODY_CODE                      += -399001
 
   NAIF_BODY_NAME                      += 'GS0002'
   NAIF_BODY_CODE                      += -399002
 
   NAIF_BODY_NAME                      += 'DSA2'
   NAIF_BODY_CODE                      += -399003
 
\begintext
 
 
   Reference frame specifications follow:
 
 
   Topocentric frame GS0001_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame GS0001_TOPO is centered at the
      site GS0001, which has Cartesian coordinates
 
         X (km):                  0.5440261112998E+04
         Y (km):                 -0.3140936218051E+04
         Z (km):                  0.1100248473419E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       -30.0000000000000
         Latitude  (deg):        10.0000000000000
         Altitude   (km):         0.1617056308623E-11
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_GS0001_TOPO                   =  -1399001
   FRAME_-1399001_NAME                 =  'GS0001_TOPO'
   FRAME_-1399001_CLASS                =  4
   FRAME_-1399001_CLASS_ID             =  -1399001
   FRAME_-1399001_CENTER               =  -399001
 
   OBJECT_-399001_FRAME                =  'GS0001_TOPO'
 
   TKFRAME_-1399001_RELATIVE           =  'ITRF93'
   TKFRAME_-1399001_SPEC               =  'ANGLES'
   TKFRAME_-1399001_UNITS              =  'DEGREES'
   TKFRAME_-1399001_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399001_ANGLES             =  ( -330.0000000000001,
                                             -80.0000000000000,
                                             180.0000000000000 )
 
 
\begintext
 
   Topocentric frame GS0002_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame GS0002_TOPO is centered at the
      site GS0002, which has Cartesian coordinates
 
         X (km):                  0.5440261112998E+04
         Y (km):                  0.3140936218051E+04
         Z (km):                  0.1100248473419E+04
 
      and planetodetic coordinates
 
         Longitude (deg):        30.0000000000000
         Latitude  (deg):        10.0000000000000
         Altitude   (km):         0.1617056308623E-11
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_GS0002_TOPO                   =  -1399002
   FRAME_-1399002_NAME                 =  'GS0002_TOPO'
   FRAME_-1399002_CLASS                =  4
   FRAME_-1399002_CLASS_ID             =  -1399002
   FRAME_-1399002_CENTER               =  -399002
 
   OBJECT_-399002_FRAME                =  'GS0002_TOPO'
 
   TKFRAME_-1399002_RELATIVE           =  'ITRF93'
   TKFRAME_-1399002_SPEC               =  'ANGLES'
   TKFRAME_-1399002_UNITS              =  'DEGREES'
   TKFRAME_-1399002_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399002_ANGLES             =  (  -30.0000000000000,
                                             -80.0000000000000,
                                             180.0000000000000 )
 
 
\begintext
 
   Topocentric frame DSA2_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame DSA2_TOPO is centered at the
      site DSA2, which has Cartesian coordinates
 
         X (km):                  0.4846725590115E+04
         Y (km):                 -0.3701740804073E+03
         Z (km):                  0.4116887886692E+04
 
      and planetodetic coordinates
 
         Longitude (deg):        -4.3675499000000
         Latitude  (deg):        40.4528000000000
         Altitude   (km):         0.7940000000010E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_DSA2_TOPO                     =  -1399003
   FRAME_-1399003_NAME                 =  'DSA2_TOPO'
   FRAME_-1399003_CLASS                =  4
   FRAME_-1399003_CLASS_ID             =  -1399003
   FRAME_-1399003_CENTER               =  -399003
 
   OBJECT_-399003_FRAME                =  'DSA2_TOPO'
 
   TKFRAME_-1399003_RELATIVE           =  'ITRF93'
   TKFRAME_-1399003_SPEC               =  'ANGLES'
   TKFRAME_-1399003_UNITS              =  'DEGREES'
   TKFRAME_-1399003_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399003_ANGLES             =  ( -355.6324501000000,
                                             -49.5472000000000,
                                             180.0000000000000 )
 
\begintext
 
 
Definitions file /tmp/pinpoint.defs
--------------------------------------------------------------------------------
 
begindata
 
   SITES = ( 'GS0001',
             'GS0002',
             'DSA2')
 
   GS0001_FRAME        = 'ITRF93'
   GS0001_IDCODE       = -399001
   GS0001_LATLON       = ( 10.0, -30.0, 0.0 )
   GS0001_CENTER       = 399
   GS0001_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   GS0001_UP           = 'Z'
   GS0001_NORTH        = 'X'
   GS0001_TOPO_FRAME   = 'GS0001_TOPO'
   GS0001_TOPO_ID      = -1399001
 
   GS0002_FRAME        = 'ITRF93'
   GS0002_IDCODE       = -399002
   GS0002_LATLON       = ( 10.0, 30.0, 0.0 )
   GS0002_CENTER       = 399
   GS0002_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   GS0002_UP           = 'Z'
   GS0002_NORTH        = 'X'
   GS0002_TOPO_FRAME   = 'GS0002_TOPO'
   GS0002_TOPO_ID      = -1399002
 
   DSA2_FRAME        = 'ITRF93'
   DSA2_IDCODE       = -399003
   DSA2_LATLON       = ( 40.4528, -4.3675499, 0.794 )
   DSA2_CENTER       = 399
   DSA2_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   DSA2_UP           = 'Z'
   DSA2_NORTH        = 'X'
   DSA2_TOPO_FRAME   = 'DSA2_TOPO'
   DSA2_TOPO_ID      = -1399003
 
begintext
 
begintext
 
[End of definitions file]
 
