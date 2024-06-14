# Use Debian slim image
FROM --platform=linux/amd64 debian:bullseye-slim

# Install necessary packages
RUN apt-get update && apt-get install -y wget

# Set the version of the CSPICE toolkit to download
ENV CSPICE_VERSION "N0066"
ENV CSPICE_PLATFORM "PC_Linux_GCC"

# Download and extract the CSPICE toolkit
RUN wget -q https://naif.jpl.nasa.gov/pub/naif/toolkit//C/PC_Linux_GCC_64bit/packages/cspice.tar.Z -O /tmp/cspice.tar.Z && \
    tar -xzf /tmp/cspice.tar.Z -C /usr/local/ && \
    rm /tmp/cspice.tar.Z

RUN wget https://naif.jpl.nasa.gov/pub/naif/utilities/PC_Linux_64bit/pinpoint -O /usr/local/cspice/exe/pinpoint
RUN chmod +x /usr/local/cspice/exe/pinpoint

# Set environment variables
ENV PATH="/usr/local/cspice/bin:/usr/local/cspice/exe:$PATH"
ENV C_INCLUDE_PATH="/usr/local/cspice/include:$C_INCLUDE_PATH"
ENV LIBRARY_PATH="/usr/local/cspice/lib:$LIBRARY_PATH"
ENV LD_LIBRARY_PATH="/usr/local/cspice/lib:$LD_LIBRARY_PATH"

# Set the default command to bash
CMD ["/bin/bash"]
