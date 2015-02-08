#!/usr/bin/python

__author__ = "Brandon Bianchi"
__copyright__ = "2015 - Brandon Bianchi"
__version__ = "1.0"
__maintainer__ = "Brandon Bianchi"
__email__ = "brandon@brandonbianchi.com"
__status__ = "Production"

# Imports

from config import *
import time

# Set time in desired format
serial = time.strftime('%Y%m%d')
print (serial)

# Grab domain information, store values
domain = raw_input('Enter new domain name (no www): \n')
domain.rstrip('\n')

prefix, tld = domain.split('.')[-2:]
prefix.rstrip('\n')

# Print output for debug
print("\n")
print(domain, prefix, tld)
print("\n")

# Get IP information for DNS
ipWWW = raw_input('Enter www IP (I am %s): \n' % ipWebMe) 
ipMail = raw_input('Enter mail IP (I am %s): \n' % ipMailMe)

# Print output for debug
print("\n")
print(ipWWW, ipMail)
print("\n")

# Create zone file for bind
# zoneFile = ('/etc/bind/%s' % domain) 
zoneFile = ('/home/brandon/tmp/%s' % domain) 
print('Creating...')
print(zoneFile)
zonePopulate = open(zoneFile, 'a')
zonePopulate.write("""\n
$TTL    14400
@               IN      SOA     %s. hostmaster.%s. (
                                %s00        ;serial
                                14400           ;refresh
                                1800            ;retry
                                864000          ;expire
                                10800           ;minimum
                                )
                IN      NS      a.root-survers.net.
                IN      NS      ns1.he.net.

$ORIGIN %s.
                IN      A       %s
                IN      MX      0 mail.%s.
mail            IN      A       %s
webmail         IN      A       %s
www             IN      A       %s \n \n""" % (domain, domain, serial, domain, ipWWW, domain, ipMail, ipWWW, ipWWW))