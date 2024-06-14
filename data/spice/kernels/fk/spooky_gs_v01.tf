KPL/FK
 
   FILE: /tmp/spooky_gs_v01.tf
 
   This file was created by PINPOINT.
 
   PINPOINT Version 3.3.0 --- December 13, 2021
   PINPOINT RUN DATE/TIME:    2024-06-14T09:18:58
   PINPOINT DEFINITIONS FILE: /tmp/pinpoint.defs
   PINPOINT PCK FILE:         /tmp/pck00011.tpc
   PINPOINT SPK FILE:         /tmp/spooky_gs_v01.bsp
 
   The input definitions file is appended to this
   file as a comment block.
 
 
   Body-name mapping follows:
 
\begindata
 
   NAIF_BODY_NAME                      += 'HOGS'
   NAIF_BODY_CODE                      += -399001
 
   NAIF_BODY_NAME                      += 'GRAZ'
   NAIF_BODY_CODE                      += -399002
 
   NAIF_BODY_NAME                      += 'XINGLONG'
   NAIF_BODY_CODE                      += -399003
 
   NAIF_BODY_NAME                      += 'NANSHAN'
   NAIF_BODY_CODE                      += -399004
 
   NAIF_BODY_NAME                      += 'DELINGHA'
   NAIF_BODY_CODE                      += -399005
 
   NAIF_BODY_NAME                      += 'LIJIANG'
   NAIF_BODY_CODE                      += -399006
 
   NAIF_BODY_NAME                      += 'NGARI'
   NAIF_BODY_CODE                      += -399007
 
   NAIF_BODY_NAME                      += 'SHANGAI'
   NAIF_BODY_CODE                      += -399008
 
   NAIF_BODY_NAME                      += 'BEIJING'
   NAIF_BODY_CODE                      += -399009
 
   NAIF_BODY_NAME                      += 'JINAN'
   NAIF_BODY_CODE                      += -399010
 
   NAIF_BODY_NAME                      += 'WEIHAI'
   NAIF_BODY_CODE                      += -399011
 
   NAIF_BODY_NAME                      += 'MOHE'
   NAIF_BODY_CODE                      += -399012
 
\begintext
 
 
   Reference frame specifications follow:
 
 
   Topocentric frame HOGS_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame HOGS_TOPO is centered at the
      site HOGS, which has Cartesian coordinates
 
         X (km):                  0.3577162768563E+04
         Y (km):                 -0.2075104362526E+03
         Z (km):                  0.5258822862913E+04
 
      and planetodetic coordinates
 
         Longitude (deg):        -3.3199950000000
         Latitude  (deg):        55.9097230000000
         Altitude   (km):         0.9999999999804E-02
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_HOGS_TOPO                     =  -1399001
   FRAME_-1399001_NAME                 =  'HOGS_TOPO'
   FRAME_-1399001_CLASS                =  4
   FRAME_-1399001_CLASS_ID             =  -1399001
   FRAME_-1399001_CENTER               =  -399001
 
   OBJECT_-399001_FRAME                =  'HOGS_TOPO'
 
   TKFRAME_-1399001_RELATIVE           =  'ITRF93'
   TKFRAME_-1399001_SPEC               =  'ANGLES'
   TKFRAME_-1399001_UNITS              =  'DEGREES'
   TKFRAME_-1399001_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399001_ANGLES             =  ( -356.6800050000000,
                                             -34.0902770000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame GRAZ_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame GRAZ_TOPO is centered at the
      site GRAZ, which has Cartesian coordinates
 
         X (km):                  0.4194372512435E+04
         Y (km):                  0.1162633033740E+04
         Z (km):                  0.4647232646079E+04
 
      and planetodetic coordinates
 
         Longitude (deg):        15.4927770000000
         Latitude  (deg):        47.0675000000000
         Altitude   (km):         0.4830000000007E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_GRAZ_TOPO                     =  -1399002
   FRAME_-1399002_NAME                 =  'GRAZ_TOPO'
   FRAME_-1399002_CLASS                =  4
   FRAME_-1399002_CLASS_ID             =  -1399002
   FRAME_-1399002_CENTER               =  -399002
 
   OBJECT_-399002_FRAME                =  'GRAZ_TOPO'
 
   TKFRAME_-1399002_RELATIVE           =  'ITRF93'
   TKFRAME_-1399002_SPEC               =  'ANGLES'
   TKFRAME_-1399002_UNITS              =  'DEGREES'
   TKFRAME_-1399002_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399002_ANGLES             =  (  -15.4927770000000,
                                             -42.9325000000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame XINGLONG_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame XINGLONG_TOPO is centered at the
      site XINGLONG, which has Cartesian coordinates
 
         X (km):                 -0.2277295094875E+04
         Y (km):                  0.4299103666380E+04
         Z (km):                  0.4112136711961E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       117.9107920000000
         Latitude  (deg):        40.3958660000000
         Altitude   (km):         0.8900000000012E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_XINGLONG_TOPO                 =  -1399003
   FRAME_-1399003_NAME                 =  'XINGLONG_TOPO'
   FRAME_-1399003_CLASS                =  4
   FRAME_-1399003_CLASS_ID             =  -1399003
   FRAME_-1399003_CENTER               =  -399003
 
   OBJECT_-399003_FRAME                =  'XINGLONG_TOPO'
 
   TKFRAME_-1399003_RELATIVE           =  'ITRF93'
   TKFRAME_-1399003_SPEC               =  'ANGLES'
   TKFRAME_-1399003_UNITS              =  'DEGREES'
   TKFRAME_-1399003_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399003_ANGLES             =  ( -117.9107920000000,
                                             -49.6041340000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame NANSHAN_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame NANSHAN_TOPO is centered at the
      site NANSHAN, which has Cartesian coordinates
 
         X (km):                  0.2284127544150E+03
         Y (km):                  0.4631611180619E+04
         Z (km):                  0.4367378810256E+04
 
      and planetodetic coordinates
 
         Longitude (deg):        87.1766860000000
         Latitude  (deg):        43.4754610000000
         Altitude   (km):         0.2028000000000E+01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_NANSHAN_TOPO                  =  -1399004
   FRAME_-1399004_NAME                 =  'NANSHAN_TOPO'
   FRAME_-1399004_CLASS                =  4
   FRAME_-1399004_CLASS_ID             =  -1399004
   FRAME_-1399004_CENTER               =  -399004
 
   OBJECT_-399004_FRAME                =  'NANSHAN_TOPO'
 
   TKFRAME_-1399004_RELATIVE           =  'ITRF93'
   TKFRAME_-1399004_SPEC               =  'ANGLES'
   TKFRAME_-1399004_UNITS              =  'DEGREES'
   TKFRAME_-1399004_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399004_ANGLES             =  (  -87.1766860000000,
                                             -46.5245390000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame DELINGHA_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame DELINGHA_TOPO is centered at the
      site DELINGHA, which has Cartesian coordinates
 
         X (km):                 -0.6826239938521E+03
         Y (km):                  0.5030973909431E+04
         Z (km):                  0.3852815886190E+04
 
      and planetodetic coordinates
 
         Longitude (deg):        97.7269480000000
         Latitude  (deg):        37.3790080000000
         Altitude   (km):         0.3153000000001E+01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_DELINGHA_TOPO                 =  -1399005
   FRAME_-1399005_NAME                 =  'DELINGHA_TOPO'
   FRAME_-1399005_CLASS                =  4
   FRAME_-1399005_CLASS_ID             =  -1399005
   FRAME_-1399005_CENTER               =  -399005
 
   OBJECT_-399005_FRAME                =  'DELINGHA_TOPO'
 
   TKFRAME_-1399005_RELATIVE           =  'ITRF93'
   TKFRAME_-1399005_SPEC               =  'ANGLES'
   TKFRAME_-1399005_UNITS              =  'DEGREES'
   TKFRAME_-1399005_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399005_ANGLES             =  (  -97.7269480000000,
                                             -52.6209920000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame LIJIANG_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame LIJIANG_TOPO is centered at the
      site LIJIANG, which has Cartesian coordinates
 
         X (km):                 -0.9935517193758E+03
         Y (km):                  0.5617910717830E+04
         Z (km):                  0.2849407164292E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       100.0293000000000
         Latitude  (deg):        26.6939000000000
         Altitude   (km):         0.3233000000002E+01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_LIJIANG_TOPO                  =  -1399006
   FRAME_-1399006_NAME                 =  'LIJIANG_TOPO'
   FRAME_-1399006_CLASS                =  4
   FRAME_-1399006_CLASS_ID             =  -1399006
   FRAME_-1399006_CENTER               =  -399006
 
   OBJECT_-399006_FRAME                =  'LIJIANG_TOPO'
 
   TKFRAME_-1399006_RELATIVE           =  'ITRF93'
   TKFRAME_-1399006_SPEC               =  'ANGLES'
   TKFRAME_-1399006_UNITS              =  'DEGREES'
   TKFRAME_-1399006_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399006_ANGLES             =  ( -100.0293000000000,
                                             -63.3061000000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame NGARI_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame NGARI_TOPO is centered at the
      site NGARI, which has Cartesian coordinates
 
         X (km):                  0.9351224687298E+03
         Y (km):                  0.5317539704446E+04
         Z (km):                  0.3393640320996E+04
 
      and planetodetic coordinates
 
         Longitude (deg):        80.0261610000000
         Latitude  (deg):        32.3250190000000
         Altitude   (km):         0.5047000000003E+01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_NGARI_TOPO                    =  -1399007
   FRAME_-1399007_NAME                 =  'NGARI_TOPO'
   FRAME_-1399007_CLASS                =  4
   FRAME_-1399007_CLASS_ID             =  -1399007
   FRAME_-1399007_CENTER               =  -399007
 
   OBJECT_-399007_FRAME                =  'NGARI_TOPO'
 
   TKFRAME_-1399007_RELATIVE           =  'ITRF93'
   TKFRAME_-1399007_SPEC               =  'ANGLES'
   TKFRAME_-1399007_UNITS              =  'DEGREES'
   TKFRAME_-1399007_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399007_ANGLES             =  (  -80.0261610000000,
                                             -57.6749810000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame SHANGAI_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame SHANGAI_TOPO is centered at the
      site SHANGAI, which has Cartesian coordinates
 
         X (km):                 -0.2858790672027E+04
         Y (km):                  0.4657382553154E+04
         Z (km):                  0.3277901132916E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       121.5424000000000
         Latitude  (deg):        31.1263000000000
         Altitude   (km):         0.2500000000081E-01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_SHANGAI_TOPO                  =  -1399008
   FRAME_-1399008_NAME                 =  'SHANGAI_TOPO'
   FRAME_-1399008_CLASS                =  4
   FRAME_-1399008_CLASS_ID             =  -1399008
   FRAME_-1399008_CENTER               =  -399008
 
   OBJECT_-399008_FRAME                =  'SHANGAI_TOPO'
 
   TKFRAME_-1399008_RELATIVE           =  'ITRF93'
   TKFRAME_-1399008_SPEC               =  'ANGLES'
   TKFRAME_-1399008_UNITS              =  'DEGREES'
   TKFRAME_-1399008_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399008_ANGLES             =  ( -121.5424000000000,
                                             -58.8737000000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame BEIJING_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame BEIJING_TOPO is centered at the
      site BEIJING, which has Cartesian coordinates
 
         X (km):                 -0.2175421882702E+04
         Y (km):                  0.4391708550214E+04
         Z (km):                  0.4068298069858E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       116.3514000000000
         Latitude  (deg):        39.8853000000000
         Altitude   (km):         0.1200000000004E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_BEIJING_TOPO                  =  -1399009
   FRAME_-1399009_NAME                 =  'BEIJING_TOPO'
   FRAME_-1399009_CLASS                =  4
   FRAME_-1399009_CLASS_ID             =  -1399009
   FRAME_-1399009_CENTER               =  -399009
 
   OBJECT_-399009_FRAME                =  'BEIJING_TOPO'
 
   TKFRAME_-1399009_RELATIVE           =  'ITRF93'
   TKFRAME_-1399009_SPEC               =  'ANGLES'
   TKFRAME_-1399009_UNITS              =  'DEGREES'
   TKFRAME_-1399009_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399009_ANGLES             =  ( -116.3514000000000,
                                             -50.1147000000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame JINAN_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame JINAN_TOPO is centered at the
      site JINAN, which has Cartesian coordinates
 
         X (km):                 -0.2334972823528E+04
         Y (km):                  0.4558325756288E+04
         Z (km):                  0.3788738293526E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       117.1235000000000
         Latitude  (deg):        36.6768000000000
         Altitude   (km):         0.8499999999987E-01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_JINAN_TOPO                    =  -1399010
   FRAME_-1399010_NAME                 =  'JINAN_TOPO'
   FRAME_-1399010_CLASS                =  4
   FRAME_-1399010_CLASS_ID             =  -1399010
   FRAME_-1399010_CENTER               =  -399010
 
   OBJECT_-399010_FRAME                =  'JINAN_TOPO'
 
   TKFRAME_-1399010_RELATIVE           =  'ITRF93'
   TKFRAME_-1399010_SPEC               =  'ANGLES'
   TKFRAME_-1399010_UNITS              =  'DEGREES'
   TKFRAME_-1399010_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399010_ANGLES             =  ( -117.1235000000000,
                                             -53.3232000000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame WEIHAI_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame WEIHAI_TOPO is centered at the
      site WEIHAI, which has Cartesian coordinates
 
         X (km):                 -0.2687430982581E+04
         Y (km):                  0.4292232199121E+04
         Z (km):                  0.3864584958378E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       122.0513000000000
         Latitude  (deg):        37.5340000000000
         Altitude   (km):         0.4600000000039E-01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_WEIHAI_TOPO                   =  -1399011
   FRAME_-1399011_NAME                 =  'WEIHAI_TOPO'
   FRAME_-1399011_CLASS                =  4
   FRAME_-1399011_CLASS_ID             =  -1399011
   FRAME_-1399011_CENTER               =  -399011
 
   OBJECT_-399011_FRAME                =  'WEIHAI_TOPO'
 
   TKFRAME_-1399011_RELATIVE           =  'ITRF93'
   TKFRAME_-1399011_SPEC               =  'ANGLES'
   TKFRAME_-1399011_UNITS              =  'DEGREES'
   TKFRAME_-1399011_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399011_ANGLES             =  ( -122.0513000000000,
                                             -52.4660000000000,
                                             270.0000000000000 )
 
 
\begintext
 
   Topocentric frame MOHE_TOPO
 
      The Z axis of this frame points toward the zenith.
      The Y axis of this frame points North.
 
      Topocentric frame MOHE_TOPO is centered at the
      site MOHE, which has Cartesian coordinates
 
         X (km):                 -0.2035472805601E+04
         Y (km):                  0.3213128169958E+04
         Z (km):                  0.5103098283809E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       122.3537000000000
         Latitude  (deg):        53.4852000000000
         Altitude   (km):         0.3000000000021E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_MOHE_TOPO                     =  -1399012
   FRAME_-1399012_NAME                 =  'MOHE_TOPO'
   FRAME_-1399012_CLASS                =  4
   FRAME_-1399012_CLASS_ID             =  -1399012
   FRAME_-1399012_CENTER               =  -399012
 
   OBJECT_-399012_FRAME                =  'MOHE_TOPO'
 
   TKFRAME_-1399012_RELATIVE           =  'ITRF93'
   TKFRAME_-1399012_SPEC               =  'ANGLES'
   TKFRAME_-1399012_UNITS              =  'DEGREES'
   TKFRAME_-1399012_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1399012_ANGLES             =  ( -122.3537000000000,
                                             -36.5148000000000,
                                             270.0000000000000 )
 
\begintext
 
 
Definitions file /tmp/pinpoint.defs
--------------------------------------------------------------------------------
 
begindata
 
   SITES = ( 'HOGS',
             'GRAZ',
             'XINGLONG',
             'NANSHAN',
             'DELINGHA',
             'LIJIANG',
             'NGARI',
             'SHANGAI',
             'BEIJING',
             'JINAN',
             'WEIHAI',
             'MOHE')
 
   HOGS_FRAME        = 'ITRF93'
   HOGS_IDCODE       = -399001
   HOGS_LATLON       = ( 55.909723, -3.319995, 0.010 )
   HOGS_CENTER       = 399
   HOGS_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   HOGS_UP           = 'Z'
   HOGS_NORTH        = 'Y'
   HOGS_TOPO_FRAME   = 'HOGS_TOPO'
   HOGS_TOPO_ID      = -1399001
 
   GRAZ_FRAME        = 'ITRF93'
   GRAZ_IDCODE       = -399002
   GRAZ_LATLON       = ( 47.0675, 15.492777, 0.483 )
   GRAZ_CENTER       = 399
   GRAZ_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   GRAZ_UP           = 'Z'
   GRAZ_NORTH        = 'Y'
   GRAZ_TOPO_FRAME   = 'GRAZ_TOPO'
   GRAZ_TOPO_ID      = -1399002
 
   XINGLONG_FRAME        = 'ITRF93'
   XINGLONG_IDCODE       = -399003
   XINGLONG_LATLON       = ( 40.395866, 117.910792, 0.890 )
   XINGLONG_CENTER       = 399
   XINGLONG_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   XINGLONG_UP           = 'Z'
   XINGLONG_NORTH        = 'Y'
   XINGLONG_TOPO_FRAME   = 'XINGLONG_TOPO'
   XINGLONG_TOPO_ID      = -1399003
 
   NANSHAN_FRAME        = 'ITRF93'
   NANSHAN_IDCODE       = -399004
   NANSHAN_LATLON       = ( 43.475461, 87.176686, 2.028 )
   NANSHAN_CENTER       = 399
   NANSHAN_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   NANSHAN_UP           = 'Z'
   NANSHAN_NORTH        = 'Y'
   NANSHAN_TOPO_FRAME   = 'NANSHAN_TOPO'
   NANSHAN_TOPO_ID      = -1399004
 
   DELINGHA_FRAME        = 'ITRF93'
   DELINGHA_IDCODE       = -399005
   DELINGHA_LATLON       = ( 37.379008, 97.726948, 3.153 )
   DELINGHA_CENTER       = 399
   DELINGHA_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   DELINGHA_UP           = 'Z'
   DELINGHA_NORTH        = 'Y'
   DELINGHA_TOPO_FRAME   = 'DELINGHA_TOPO'
   DELINGHA_TOPO_ID      = -1399005
 
   LIJIANG_FRAME        = 'ITRF93'
   LIJIANG_IDCODE       = -399006
   LIJIANG_LATLON       = ( 26.6939, 100.0293, 3.233 )
   LIJIANG_CENTER       = 399
   LIJIANG_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   LIJIANG_UP           = 'Z'
   LIJIANG_NORTH        = 'Y'
   LIJIANG_TOPO_FRAME   = 'LIJIANG_TOPO'
   LIJIANG_TOPO_ID      = -1399006
 
   NGARI_FRAME        = 'ITRF93'
   NGARI_IDCODE       = -399007
   NGARI_LATLON       = ( 32.325019, 80.026161, 5.047 )
   NGARI_CENTER       = 399
   NGARI_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   NGARI_UP           = 'Z'
   NGARI_NORTH        = 'Y'
   NGARI_TOPO_FRAME   = 'NGARI_TOPO'
   NGARI_TOPO_ID      = -1399007
 
   SHANGAI_FRAME        = 'ITRF93'
   SHANGAI_IDCODE       = -399008
   SHANGAI_LATLON       = ( 31.1263, 121.5424, 0.025 )
   SHANGAI_CENTER       = 399
   SHANGAI_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   SHANGAI_UP           = 'Z'
   SHANGAI_NORTH        = 'Y'
   SHANGAI_TOPO_FRAME   = 'SHANGAI_TOPO'
   SHANGAI_TOPO_ID      = -1399008
 
   BEIJING_FRAME        = 'ITRF93'
   BEIJING_IDCODE       = -399009
   BEIJING_LATLON       = ( 39.8853, 116.3514, 0.120 )
   BEIJING_CENTER       = 399
   BEIJING_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   BEIJING_UP           = 'Z'
   BEIJING_NORTH        = 'Y'
   BEIJING_TOPO_FRAME   = 'BEIJING_TOPO'
   BEIJING_TOPO_ID      = -1399009
 
   JINAN_FRAME        = 'ITRF93'
   JINAN_IDCODE       = -399010
   JINAN_LATLON       = ( 36.6768, 117.1235, 0.085 )
   JINAN_CENTER       = 399
   JINAN_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   JINAN_UP           = 'Z'
   JINAN_NORTH        = 'Y'
   JINAN_TOPO_FRAME   = 'JINAN_TOPO'
   JINAN_TOPO_ID      = -1399010
 
   WEIHAI_FRAME        = 'ITRF93'
   WEIHAI_IDCODE       = -399011
   WEIHAI_LATLON       = ( 37.5340, 122.0513, 0.046 )
   WEIHAI_CENTER       = 399
   WEIHAI_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   WEIHAI_UP           = 'Z'
   WEIHAI_NORTH        = 'Y'
   WEIHAI_TOPO_FRAME   = 'WEIHAI_TOPO'
   WEIHAI_TOPO_ID      = -1399011
 
   MOHE_FRAME        = 'ITRF93'
   MOHE_IDCODE       = -399012
   MOHE_LATLON       = ( 53.4852, 122.3537, 0.300 )
   MOHE_CENTER       = 399
   MOHE_BOUNDS       = ( @2020-01-01, @2100-01-01 )
   MOHE_UP           = 'Z'
   MOHE_NORTH        = 'Y'
   MOHE_TOPO_FRAME   = 'MOHE_TOPO'
   MOHE_TOPO_ID      = -1399012
 
begintext
 
begintext
 
[End of definitions file]
 
