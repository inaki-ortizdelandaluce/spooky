Spooky FK files
===========================================================================

     This ``aareadme.txt'' file describes the contents of the kernels/spk
     directory of the Spooky SPICE Kernel Dataset.


Contact Information
--------------------------------------------------------

     If you have any questions regarding this directory or its
     contents, please contact:

             Inaki Ortiz de Landaluce
             (+34) 605 18 47 32
             inaki.ortizdelandaluce@gmail.com

     
References and required readings
--------------------------------------------------------

     1. ``Frames Required Reading'', NAIF Document

     2. ``Kernel Pool Required Reading'', NAIF

     3. ``C-Kernel Required Reading'', NAIF

          
Brief Summary
--------------------------------------------------------

     This directory contains the SPICE Frames Definition Kernel files for the
     Ground Earth Stations. 
   

File naming conventions
--------------------------------------------------------

     The following table provides information on which file contains which
     frames, their file naming conventions and some particular details:
   
         File                         Contents
        ---------------------------  -----------------------------------------
        estrack_vNN.tf               ESA Ground Stations topocentric frames.
       
        earthfixeditrf93.tf          Makes the ITRF93 frame coincide with
                                     the Earth fixed reference frame.

        earth_topo_YYMMDD.tf         NASA DSN Ground Stations topocentric
                                     frames.

        rssd0002.tf                  Cross-mission frames kernel that defines
                                     frames of interest not ``built'' in the
                                     SPICE toolkit.

        earthstns_jaxa_YYYYMMDD.tf   JAXA Ground Stations topocentric
                                     frames.

     where
    
         YYMMDD         product creation time (required);

         NN             version number -- two digits (required)

                        If multiple versions of a Frames Kernel file are
                        provided, always use the latest version (unless
                        earlier version is needed for some special reasons).


Current FK Kernels Set
--------------------------------------------------------

   earthfixeditrf93.tf

      SPICE FK file that makes the ITRF93 frame coincide with the Earth
      fixed reference frame. Created by NAIF, JPL.


   estrack_vNN.tf

      SPICE FK file that provides topocentric frames for the ESA Ground
      Stations. Created by the ESA SPICE Service (ESS).


   earth_topo_YYMMDD.tf

      SPICE FK kernel for the topocentric reference frames for the Deep Space
      Network (DSN) stations. This kernel was released on the date indicated
      in the filename. Created by NAIF, JPL.


   earthstns_jaxa_YYYYMMDD.tf

      SPICE FK kernel for the topocentric reference frames for the JAXA Deep 
      Space stations. Created by the ESA SPICE Service (ESS).


Other directory contents
--------------------------------------------------------

     aareadme.txt         This file.
   

Particulars
--------------------------------------------------------
                             
     Nothing to report.


Kernel File Details
--------------------------------------------------------
 
     The most detailed description of the data in an FK file is provided in
     metadata included inside the descriptive text areas of the file. This
     information can be viewed using any text editor.


End of aareadme file.