# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime

today = datetime.date.today()
print( today )

from datetime import date
print( date.today() )

import time
print( time.time() )

from time import time
print( time )

import camelcase
camel = camelcase.CamelCase()

text = "eat a dick"
print( camel.hump(text) )

