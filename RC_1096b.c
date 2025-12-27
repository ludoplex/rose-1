// RC_1096b.c - Test file for ROSE compiler infrastructure
// This file is designed to be compilable with jart/cosmopolitan for maximum
// portability across x86_64 and ARM64 on Linux, macOS, Windows, FreeBSD,
// NetBSD, and OpenBSD.

#ifdef __COSMOPOLITAN__
#include "cosmopolitan.h"
#else
#include <stdlib.h>
#include <alloca.h>
#endif

int main(void) {
  // Use alloca to allocate stack memory
  // Note: alloca is supported by cosmopolitan libc
  void* p = alloca(20);
  
  // Prevent unused variable warning and ensure the allocation is used
  if (p) {
    // Simple use of allocated memory to prevent optimization away
    ((char*)p)[0] = 0;
  }
  
  return 0;
}

// Reproduce issue with: codethorn RC-1096.c --normalize-level=2 --unparse
// shows wrong return type
