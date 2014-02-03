#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#   Filename:  test_axisem.py
#   Purpose:   run the AXISEM tests automatically
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#-------------------------------------------------------------------

import subprocess
import sys
import os
import argparse

parser = argparse.ArgumentParser(description=
    'Run some automated tests for the axisem solver.')

parser.add_argument('-a', help='run all tests', action='store_const',
                    const=True, default=False)
args = parser.parse_args()

if not args.a:
    print '=========================================='
    test_no = \
        raw_input('Please enter the test number(s): \n' + \
            'Elastic tests (PREM)\n' + \
            '1.  test01: explosion\n' + \
            '2.  test02: dipole (mxz)\n' + \
            '3.  test03: quadpole (mxy)\n' + \
            '4.  test04: CMT (location: north pole)\n' + \
            '5.  test05: CMT (location: 70N 50E)\n' + \
            '6.  test06: like test05, but with NetCDF\n' + \
            '7.  test07: like test05, but with 1 CPU\n' + \
            '8.  test08: like test05, but with radial slicing\n' + \
            '9.  test09: explosion, 4x4 mesh\n' + \
            '10. test10: dipole, 4x4 mesh\n' + \
            'Anelastic tests, coarse grained (PREM)\n' + \
            '11. test11: explosion\n' + \
            '12. test12: dipole (mxz)\n' + \
            '13. test13: quadpole (mxy)\n' + \
            'Anelastic tests, memory variables (PREM)\n' + \
            '14. test14: explosion\n' + \
            '15. test15: dipole (mxz)\n' + \
            '16. test16: quadpole (mxy)\n' + \
            '17. test17: external mesh (PREM)\n' + \
            '\n(format = 01,02 OR 1,2,3)' + \
            '\n')
else:
    test_no = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17'

print '=========================================='
print 'Requested Test numbers:'

for i in range(0, len(test_no.split(','))):
    num = test_no.split(',')[i]
    num = num.strip()
    if len(num) == 1:
        num = '0' + num
    print 'test' + num
print '=========================================='

for i in range(0, len(test_no.split(','))):
    num = test_no.split(',')[i]
    num = num.strip()
    if len(num) == 1:
        num = '0' + num
    
    print '======================='
    print 'test' + num + ' starts!'
    print '======================='
    
    address = os.path.join('.', 'automated', 'test_' + num, 'inpython.cfg')
    address_stas = os.path.join('.', 'automated', 'test_' + num, 'STATIONS')
    output = subprocess.check_call(['python', 'PyAxi.py', address, address_stas])
    if output != 0: print output_print
    print '=========================================='
