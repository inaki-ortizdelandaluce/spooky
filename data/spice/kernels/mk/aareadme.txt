Spooky MK files
===========================================================================

     This ``aareadme.txt'' file describes the contents of the kernels/spk
     directory of the Spooky SPICE Kernel Dataset.


Brief Summary
------------------------------------------------------------------------

   This directory contains the SPICE Meta-Kernel files for the Spooky
   SPICE Kernel Dataset. Meta-kernels (also known as ``FURNSH kernel'') 
   are used to name a collection of kernels that are to be loaded into a 
   user's application at run-time. Meta-kernels are appropriate to group 
   kernels that correspond to a certain study group, phase or kernel state 
   of the mission.


File naming conventions
------------------------------------------------------------------------

   Naming Scheme for MKs:

     The naming scheme for the MKs is:

          spooky[_DESC][_vXXX][_TAG][_NNN].tm

     where

           DESC      a brief description of the scope of study of the
                     scenario (optional);

           vXXX      version number that corresponds to the version of the
                     meta-kernel or the SPICE Kernel Dataset release number
                     (optional; e.g. v121 for Release 1.2.1)

           TAG       a time tag of the MK generation time (optional;
                     e.g. 20160928);

           NNN       a count of the MK version generated for a given TAG
                     (mandatory if TAG is included; e.g 001)



Other directory contents
------------------------------------------------------------------------

     aareadme.txt         This file.

     former_versions      Directory where versions no longer valid are
                          stored for archive purposes.


Particulars
------------------------------------------------------------------------

     Nothing to report.


Kernel File Details
------------------------------------------------------------------------

    Name                         Comments
    ---------------------------------------------------------------------

    spooky_ops.tm                Contains the latest available historic data
                                 kernels.

    spooky_ops_vXXX_YYYYMMDD_NNN.tm

                                 Is a duplicate of the study MK that
                                 derived from release vXXX. If multiple
                                 study MK files are generated on the
                                 same date the version NNN is increased
                                 starting from 001. 


Contact Information
------------------------------------------------------------------------

     If you have any questions regarding this directory or its
     contents, please contact:

             Inaki Ortiz de Landaluce
             (+34) 605 18 47 32
             inaki.ortizdelandaluce@gmail.com


References and required readings
------------------------------------------------------------------------

     1. ``Kernel Required Reading'', NAIF Document


End of aareadme file.