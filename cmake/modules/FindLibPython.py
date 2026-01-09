
# Copyright (c) 2007, Simon Edwards <simon@simonzone.com>
# Redistribution and use is allowed according to the terms of the BSD license.
# For details see the accompanying COPYING-CMAKE-SCRIPTS file.

import sys
import distutils.sysconfig

print(f"exec_prefix:{sys.exec_prefix}")
print(f"short_version:{sys.version[:3]}")
print(f"long_version:{sys.version.split()[0]}")
print(f"py_inc_dir:{distutils.sysconfig.get_python_inc()}")
print("site_packages_dir:%s" % distutils.sysconfig.get_python_lib(plat_specific=1))
