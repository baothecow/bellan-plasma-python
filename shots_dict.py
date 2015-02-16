# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 09:04:59 2014

@author: bao

A dictionary whose keys are constructed from a strapping field and  a letter which
corresponds to configuration of the external inductor.

N.E - Null strapping field configuration at max inductance.

A - No inductance.
B - Small inductance.
C - Medium inductance.
D - Large inductance.
E - Maximum inductance

In addition, there are keys of the form 'A.info' which contains the
list of strapping voltages associated with the A shots.

Updated: 10/09/14 - Updated to remove incorrect shotnumbers and shots where the
strapping bank did not properly trigger.

Updated: 12/31/14 - Updated to include shots taken on 10/13/14 & 10/14/14

"""

shots_dict = {


    'N.E.info' : [0, 15, 30, 45, 60],
    ### No strap configuration on 7/30/14 Probe @ center.
    'N.E.0' : range(2129, 2140),
    ### 15V Null Field Max Ind on 10/13/14
    'N.E.15' : range(2413, 2419),
    ### 30V Null Field Max Ind on 10/13/14
    'N.E.30' : range(2407, 2413),
    ### 45V Null Field Max Ind on 10/13/14
    'N.E.45' : range(2419, 2425),
    ### 60V Null Field Max Ind on 10/13/14
    'N.E.60' : range(2425, 2431),


    'E.info' : ['neg90', 'neg75', 'neg60', 'neg45', 'neg30', 'neg15', 0, 15, 30, 40, 45, 50, 60, 70, 80, 90], 
    ### -90V Max Ind on 8/21/14,
    'E.neg90' : range(2270, 2280), 
    ### -75V Max Ind on 8/21/14
    'E.neg75' : range(2290, 2295), 
    ### -60V Max Ind on 8/21/14
    'E.neg60' : range(2250, 2260), 
    ### -30V Max Ind on 8/21/14 & 10/13/14
    'E.neg45' : range(2285, 2290) + range(2351, 2357),  
    ### -30V Max Ind on 8/21/14
    'E.neg30' : range(2260, 2270), 
    ### -15V Max Ind on 8/21/14 & 10/13/14
    'E.neg15' : range(2280, 2285) + range(2345, 2351),
    ## 0V Max Ind on 5/25/14 and 10/14/14
    'E.0' : range(1554, 1574) + range(1581, 1585) + range(1592, 1604) + [1634, 1655, 1656] + range(1657, 1660)+range(1785, 1790) + range(2238, 2260) +\
            range(2449, 2455) + range(2473, 2479) + range(2498, 2504), 
    ### 15V Max Ind on 5/25/14 and 10/14/14
    'E.15' : [1635] + range(1780, 1785) + range(2479, 2485) + range(2431, 2437) + range(2455, 2461),
    ### 30V Max Ind on 5/25/14 and 10/14/14
    'E.30' : [1620, 1621, 1633] + range(1755, 1762) + range(2443, 2449) + range(2467, 2473) + range(2491, 2498),
    ### 40V Max Ind on 5/25/14
    'E.40' : [1654] + range(1703, 1709),
    ### 45V Max Ind on 5/25/14 and 10/14/14
    'E.45' : range(1698, 1702) + range(1776, 1780) + range(2437, 2443) + range(2461, 2467) + range(2485, 2491),
    ### 50V Max Ind on 5/25/14
    'E.50' : [1646, 1653] + range(1661, 1665) + range(1691, 1698) + [1709] + range(1790, 1796),
    ### 60V Max Ind on 5/25/14
    'E.60' : range(1605, 1618) + [1637, 1644, 1645, 1652] + range(1665, 1669) + range(1763, 1769),
    #### 70V Max Ind on 5/25/14
    'E.70' : [1624, 1625, 1631, 1641, 1642, 1643, 1651] + range(1670, 1675),
    ### 80V Max Ind on 5/25/14
    'E.80' : [1638, 1639, 1640, 1650],
    ## 90V Max Ind on 5/25/14
    'E.90' : [1618, 1619, 1629, 1647, 1648, 1649]+ range(1769, 1773),
    
    
    'D.info' : [0, 30, 50, 60, 90],
    ### 0V Large Ind on 6/08/14.  3.5kV
    'D.0' : range(1888, 1899),
    ### 30V Large Ind on 6/08/14.  3.5kV
    'D.30' : range(1912, 1917),
    ### 50V Large Ind on 6/08/14.  3.5kV
    'D.50' : range(1899, 1912),
    ## 60V Large Ind on 6/08/14.  3.5kV
    'D.60' : range(1917, 1922),
    ## 90V Large Ind on 6/08/14.  3.5kV
    'D.90' : range(1922, 1927),
    
    
    'C.info' : ['neg60', 'neg45', 'neg30', 'neg15', 0, 30, 45, 60, 75, 90, 105],
    ### -60V Med Ind on 10/13/14
    'C.neg60' : range(2377, 2383),
    ### -45V Med Ind on 10/13/14
    'C.neg45' : range(2363, 2371),
    ### -45V Med Ind on 10/13/14
    'C.neg30' : range(2371, 2377),
    ### -15V Med Ind on 10/13/14
    'C.neg15' : range(2357, 2363),
    # 0V Medium Ind on 7/10/14.  3.3kV
    'C.0' : range(2056, 2068),
    ## 30V Medium Ind on 7/10/14.  3.3kV
    'C.30' : range(2088, 2098),
    ## 45V Medium Ind on 7/10/14.  3.3kV
    'C.45' : range(2118, 2128),
    ## 60V Medium Ind on 7/10/14.  3.3kV
    'C.60' : range(2068, 2076) + [2077],
    ## 75V Medium Ind on 7/10/14.  3.3kV
    'C.75' : range(2098, 2108),
    ## 90V Medium Ind on 7/10/14.  3.3kV
    'C.90' : range(2078, 2088),
    ## 105V Medium Ind on 7/10/14.  3.3kV
    'C.105' : range(2108, 2118),
    
    
    'B.info' : [0, 30, 50, 60, 90],
    ## 0V Small Ind on 6/08/14.  3.13kV
    'B.0' : range(1823, 1833) + range(1879, 1882),
    # 30V Small Ind on 6/08/14.  3.13kV
    'B.30' : range(1833, 1842),
    ### 50V Small Ind on 6/08/14
    'B.50' : range(1868, 1879),
    ### 60V Small Ind on 6/08/14.  3.13kV
    'B.60' : range(1842, 1853),
    ### 90V Small Ind on 6/08/14.  3.13kV
    'B.90' : range(1853, 1867),
    
    
    'A.info' : ['neg60', 'neg45', 'neg30', 'neg15', 0, 15, 30, 45, 60, 75, 90],
    ### -60V No Ind on 10/13/14.  2.69kV
    'A.neg60' : range(2401, 2407),
    ### -45V No Ind on 10/13/14.  2.69kV
    'A.neg45' : range(2389, 2395),
    ### -30V No Ind on 10/13/14.  2.69kV
    'A.neg30' : range(2395, 2401),
    ### -15V No Ind on 10/13/14.  2.69kV
    'A.neg15' : range(2383, 2389),
    ## 0V No Extra Ind on 7/08 & 7/09.  2.7kV
    'A.0' : range(1969, 1978) + range(2044, 2054),
    ## 15V No Extra Ind on 7/08 & 7/09.  2.7kV
    'A.15' : range(2034, 2044),
    ## 30V No Extra Ind on 7/08 & 7/09.  2.7kV
    'A.30' : range(2002, 2010),
    ## 45V No Extra Ind on 7/08 & 7/09.  2.7kV
    'A.45' : range(2013, 2023),
    ## 60V No Extra Ind on 7/08 & 7/09.  2.7kV
    'A.60' : range(1979, 1992) + [2012],
    ## 75V No Extra Ind on 7/08 & 7/09.  2.7kV
    'A.75' : range(2023,2029) + range(2030, 2034),
    ## 90V No Extra Ind on 7/08 & 7/09.  2.7kV
    'A.90' : range(1992, 2002) + [2011]


}
