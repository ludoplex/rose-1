# FindSIP.py
#
# Copyright (c) 2007, Simon Edwards <simon@simonzone.com>
# Redistribution and use is allowed according to the terms of the BSD license.
# For details see the accompanying COPYING-CMAKE-SCRIPTS file.

import sys
import sipconfig

sipcfg = sipconfig.Configuration()
print("sip_version:%06.0x" % sipcfg.sip_version)
print(f"sip_version_str:{sipcfg.sip_version_str}")
print(f"sip_bin:{sipcfg.sip_bin}")
print(f"default_sip_dir:{sipcfg.default_sip_dir}")
print(f"sip_inc_dir:{sipcfg.sip_inc_dir}")
