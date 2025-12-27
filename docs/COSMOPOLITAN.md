# Cosmopolitan Build Support

This document describes how to build components of this repository using
[Cosmopolitan Libc](https://github.com/jart/cosmopolitan) to create Actually
Portable Executables (APE) that run on multiple operating systems and
architectures.

## What is Cosmopolitan?

Cosmopolitan Libc is a C library that enables building portable executables
that can run unmodified on:

**Operating Systems:**
- Linux (2.6.18+)
- macOS (10.13+)
- Windows 10+
- FreeBSD (13+)
- NetBSD (9.2+)
- OpenBSD (7+)

**Architectures:**
- x86_64 (AMD64)
- ARM64 (aarch64)

## Prerequisites

### Installing Cosmopolitan Toolchain

1. Download the cosmocc toolchain from the [Cosmopolitan releases](https://github.com/jart/cosmopolitan/releases).

2. Extract and add to your PATH:
   ```bash
   # Example installation (replace VERSION with specific version like 3.3.2)
   COSMO_VERSION="3.3.2"
   mkdir -p /opt/cosmo
   cd /opt/cosmo
   wget "https://github.com/jart/cosmopolitan/releases/download/${COSMO_VERSION}/cosmocc-${COSMO_VERSION}.zip"
   unzip "cosmocc-${COSMO_VERSION}.zip"
   export PATH="/opt/cosmo/bin:$PATH"
   ```

3. Verify installation:
   ```bash
   cosmocc --version
   ```

## Building

### Using Makefile.cosmo

The `Makefile.cosmo` provides build targets for creating portable executables:

```bash
# Build all targets
make -f Makefile.cosmo

# Check if toolchain is available
make -f Makefile.cosmo check-toolchain

# Clean build artifacts
make -f Makefile.cosmo clean

# Run tests
make -f Makefile.cosmo test

# Show help
make -f Makefile.cosmo help
```

### Custom Configuration

You can customize the build using environment variables:

```bash
# Specify custom cosmocc path
make -f Makefile.cosmo CC=/custom/path/to/cosmocc

# Add debug symbols
make -f Makefile.cosmo CFLAGS='-g'

# Specify cosmopolitan installation path
make -f Makefile.cosmo COSMO_PATH=/custom/cosmo/path
```

## Output

Successful builds produce `.com` files in the `build-cosmo/` directory. These
are Actually Portable Executables that can run on any supported platform:

```bash
# The same binary works everywhere
./build-cosmo/RC_1096b.com      # On Unix-like systems
build-cosmo\RC_1096b.com        # On Windows
```

## Code Guidelines

When writing code for cosmopolitan compatibility:

1. **Use standard C**: Stick to C99/C11 standards for maximum compatibility.

2. **Conditional includes**: Use `__COSMOPOLITAN__` macro for platform-specific
   code:
   ```c
   #ifdef __COSMOPOLITAN__
   #include "cosmopolitan.h"
   #else
   #include <stdlib.h>
   #endif
   ```

3. **Avoid switch on errno**: Some system constants aren't compile-time
   constants in cosmopolitan. Use if-else chains instead:
   ```c
   // Instead of: switch(errno) { case EINVAL: ... }
   if (errno == EINVAL) { ... }
   ```

4. **Static linking only**: Cosmopolitan uses static linking. Avoid dependencies
   on dynamic libraries.

5. **Standard function prototypes**: Ensure `main()` has the proper signature:
   ```c
   int main(void) { ... }
   // or
   int main(int argc, char *argv[]) { ... }
   ```

## Limitations

- **C++ support**: Cosmopolitan primarily supports C. C++ support is limited.
- **Dynamic linking**: Not supported; all dependencies must be statically linked.
- **Binary size**: Portable executables are larger than platform-specific ones.
- **OS-specific features**: Some OS-specific APIs may not be available.

## Full ROSE Compiler

The main ROSE compiler infrastructure is a complex C++ project with dependencies
on Boost, EDG, and other libraries. Full cosmopolitan support for the complete
ROSE compiler would require significant porting effort. The cosmopolitan build
support currently targets:

1. Simple C test files (like `RC_1096b.c`)
2. Standalone utility programs written in C

## Resources

- [Cosmopolitan Libc](https://github.com/jart/cosmopolitan)
- [Actually Portable Executable](https://justine.lol/ape.html)
- [Cosmopolitan Documentation](https://justine.lol/cosmopolitan/)

## Contributing

To add cosmopolitan support for additional components:

1. Ensure the code is written in standard C
2. Add appropriate conditional compilation guards
3. Update `Makefile.cosmo` with new targets
4. Test on multiple platforms if possible
