KPL/MK

Meta-kernel for Spooky SPICE Kernel Dataset v001 -- Operational 20240521_001
============================================================================

   This meta-kernel lists the Spooky SPICE kernels
   that provide information for the Operational scenario.

   The kernels listed in this meta-kernel and the order in which
   they are listed are picked to provide the best data available and
   the most complete coverage for the GNSS Operational scenario.



Usage of the Meta-kernel
---------------------------------------------------------------------------

   This file is used by the SPICE system as follows: programs that make use
   of this kernel must "load" the kernel normally during program
   initialization. Loading the kernel associates the data items with
   their names in a data structure called the "kernel pool". The SPICELIB
   routine FURNSH loads a kernel into the pool.


Implementation Notes
---------------------------------------------------------------------------

   It is recommended that users make a local copy of this file and
   modify the value of the PATH_VALUES keyword to point to the actual
   location of the GNSS SPICE data set's ``data'' directory on
   their system. Replacing ``/'' with ``\'' and converting line
   terminators to the format native to the user's system may also be
   required if this meta-kernel is to be used on a non-UNIX workstation.


-------------------


   \begindata

     PATH_VALUES       = ( '..' )

     PATH_SYMBOLS      = ( 'KERNELS' )

     KERNELS_TO_LOAD   = (

                           '$KERNELS/fk/earth_topo_201023.tf'
                           '$KERNELS/fk/earthfixeditrf93.tf'
                           '$KERNELS/fk/spooky_earthstns_20240618.tf'

                           '$KERNELS/lsk/naif0012.tls'

                           '$KERNELS/pck/de403_masses.tpc'
                           '$KERNELS/pck/pck00011.tpc'

                           '$KERNELS/pck/earth_070425_370426_predict.bpc'
                           '$KERNELS/pck/earth_000101_240810_240517.bpc'

                           '$KERNELS/spk/de432s.bsp'

                           '$KERNELS/spk/spooky_earthstns_20240618.bsp'

                         )

   \begintext


SPICE Kernel Dataset Version
--------------------------------------------------------------------------

   The SPICE Kernel Dataset version of the kernels present in this
   meta-kernel is provided by the following keyword (please note that
   this might not be the last version of the SPICE Kernel Dataset):

   \begindata

      SKD_VERSION = 'v001_20240521_001'

   \begintext

   The unique identifier for this meta-kernel is provided by the following
   keyword:

   \begindata

      MK_IDENTIFIER = 'spooky_v001_20240521_001'

   \begintext


Contact Information
--------------------------------------------------------------------------

   If you have any questions regarding this directory or its
   contents, please contact:

            Inaki Ortiz de Landaluce
            (+34) 605 18 47 32
            inaki.ortizdelandaluce@gmail.com

End of MK file.