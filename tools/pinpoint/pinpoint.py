
def just(s, pad=0):
    return s.rjust(pad + len(s) + 3)


def write_pinpoint_def(path):
    # see https://naif.jpl.nasa.gov/pub/naif/utilities/PC_Linux_64bit/pinpoint.ug
    with open(path, 'r') as file:
        with open('pinpoint.defs', 'w') as o:
            # begin data
            o.write(f"\\begindata\n\n")

            o.write(f"{just('SITES = ( ')}")
            contents = ''
            for idx, line in enumerate(file):
                site = "".join(line.split(',')[0].upper().split())
                site = f"'{site}'"
                pad = -len(site) if idx == 0 else 10
                contents += f"{just(site, pad=pad)}, \n"
            contents = contents[:-3]
            o.write(contents + ')\n\n')

    with open(path, 'r') as file:
        with open('pinpoint.defs', 'a+') as o:
            contents = ''
            for idx, line in enumerate(file):
                site, lon, lat, alt = line.rstrip().split(',')

                site = "".join(site.upper().split())
                site_id = f"399{(idx+1):03}"

                contents += just(f"{site}_FRAME        = 'ITRF93'") + '\n'
                contents += just(f"{site}_IDCODE       = -{site_id}") + '\n'
                contents += just(f"{site}_LATLON       = ( {lat}, {lon}, {alt} )") + '\n'
                contents += just(f"{site}_CENTER       = 399") + '\n'
                contents += just(f"{site}_BOUNDS       = ( @2020-01-01, @2100-01-01 )") + '\n'
                contents += just(f"{site}_UP           = 'Z'") + '\n'
                contents += just(f"{site}_NORTH        = 'Y'") + '\n'
                contents += just(f"{site}_TOPO_FRAME   = '{site}_TOPO'") + '\n'
                contents += just(f"{site}_TOPO_ID      = -1{site_id}") + '\n\n'

            o.write(contents)

            # begin text
            o.write(f"\\begintext")


if __name__ == '__main__':
    write_pinpoint_def('ground_stations.csv')
