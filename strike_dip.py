import math

# The appropriate input for this function is a list of tuples in the format
# [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)]
def calc_strikedip(pts):
    ptA, ptB, ptC = pts[0], pts[1], pts[2]
    x1, y1, z1 = float(ptA[0]), float(ptA[1]), float(ptA[2])
    x2, y2, z2 = float(ptB[0]), float(ptB[1]), float(ptB[2])
    x3, y3, z3 = float(ptC[0]), float(ptC[1]), float(ptC[2])


    u1 = float(((y1 - y2) * (z3 - z2) - (y3 - y2) * (z1 - z2)))
    u2 = float((-((x1 - x2) * (z3 - z2) - (x3 - x2) * (z1 - z2))))
    u3 = float(((x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2)))

    '''
    Calculate pseudo eastings and northings from origin
    these are actually coordinates of a new point that represents
    the normal from the plane's origin defined as (0,0,0).
    
    If the z value (u3) is above the plane we first reverse the easting
    then we check if the z value (u3) is below the plane, if so
    we reverse the northing. 
    
    This is to satisfy the right hand rule in geology where dip is always
    to the right if looking down strike. 
    '''
    if u3 < 0:
        easting = u2
    else:
        easting = -u2

    if u3 > 0:
        northing = u1
    else:
        northing = -u1
    
    if easting >= 0:
        partA_strike = math.pow(easting, 2) + math.pow(northing, 2)
        strike = math.degrees(math.acos(northing / math.sqrt(partA_strike)))
    else:
        partA_strike = northing / math.sqrt(math.pow(easting, 2) + math.pow(northing, 2))
        strike = math.degrees(2 * math.pi - math.acos(partA_strike))

    # determine dip
    print(strike, 'strike')
    part1_dip = math.sqrt(math.pow(u2, 2) + math.pow(u1, 2))
    part2_dip = math.sqrt(math.pow(u1,2) + math.pow(u2,2) + math.pow(u3,2))
    dip = math.degrees(math.asin(part1_dip / part2_dip))

    return strike, dip

