# Agent Instructions - ROSE Compiler Infrastructure

This file provides context and documentation references for AI agents working on this project.

## Project Profile

- **Type**: Compiler Infrastructure / Static Analysis
- **Description**: Source-to-source program transformation and analysis tools from LLNL
- **Languages**: C, C++, Fortran, OpenMP, UPC, Python, Java, PHP
- **Profile ID**: `rose-compiler`

## Key Components

### COMPASS - Static Analysis Framework

Location: `projects/compass/`

COMPASS provides 100+ code quality and security checkers including:

| Category | Key Checkers |
|----------|--------------|
| Memory Safety | nullDeref, bufferOverflowFunctions, setPointersToNull, newDelete |
| Security | forbiddenFunctions, asynchronousSignalHandler, noVfork, noRand |
| Code Quality | magicNumber, deepNesting, cyclomaticComplexity, noGoto |
| Type Safety | constCast, doNotUseCstyleCasts, voidStar, explicitCharSign |
| Best Practices | oneLinePerDeclaration, functionDocumentation, preferAlgorithms |

### CERT Secure Coding Rules

Location: `projects/CertSecureCodeProject/`

Implements 220 CERT C Secure Coding rules:
- 57 Complete implementations
- 45 Partial implementations
- 29 Potential (could be added)
- 32 Undoable (ROSE limitations)
- 48 Unenforceable (requires runtime analysis)

Categories: ARR (Array), DCL (Declarations), ENV (Environment), ERR (Error Handling), EXP (Expressions), FIO (File I/O), FLP (Floating Point), INT (Integers), MEM (Memory), MSC (Miscellaneous), POS (POSIX), PRE (Preprocessor), SIG (Signals), STR (Strings)

### CodeThorn - Advanced Analysis

Location: `projects/CodeThorn/`

Model checking and data flow analysis with 1400+ source files.

## Documentation

| Resource | URL |
|----------|-----|
| ROSE Wiki | https://github.com/rose-compiler/rose/wiki |
| ROSE API (Doxygen) | http://doxygen.rosecompiler.org |
| ROSE Homepage | http://www.rosecompiler.org/ |
| CERT C Standard | https://wiki.sei.cmu.edu/confluence/display/c |

## Build Instructions

```bash
# From source tree
./build

# Navigate to build tree
../src/configure --prefix=/path/for/install \
                 --enable-languages=c,c++ \
                 --with-boost=/path/to/boost

make -j${NUM_PROCESSORS}
make install -j${NUM_PROCESSORS}
make check -j${NUM_PROCESSORS}
```

### Ubuntu Quick Install

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:rosecompiler/rose-development
sudo apt-get install rose rose-tools
```

## Key Source Directories

| Directory | Purpose |
|-----------|---------|
| `src/` | Core ROSE infrastructure |
| `src/frontend/` | Language frontends (C, C++, Fortran) |
| `src/backend/` | Code generation backends |
| `src/midend/` | Analysis and transformation passes |
| `projects/` | Analysis tools and applications |
| `tools/` | Production-ready tools |
| `tutorial/` | Example code for learning ROSE |
| `tests/` | Test suites |

## AST Node Types

Common ROSE AST nodes (Sg* prefix = Sage):

| Node | Description |
|------|-------------|
| `SgProject` | Top-level project node |
| `SgSourceFile` | Source file container |
| `SgGlobal` | Global scope |
| `SgFunctionDeclaration` | Function declaration |
| `SgFunctionDefinition` | Function body |
| `SgBasicBlock` | Statement block |
| `SgExprStatement` | Expression statement |
| `SgIfStmt` | If statement |
| `SgForStatement` | For loop |
| `SgWhileStmt` | While loop |
| `SgVariableDeclaration` | Variable declaration |
| `SgAssignOp` | Assignment operator |
| `SgFunctionCallExp` | Function call |
| `SgBinaryOp` | Binary operator |
| `SgUnaryOp` | Unary operator |

## Development Patterns

### AST Traversal

```cpp
#include "rose.h"

class MyAnalysis : public AstSimpleProcessing {
public:
    void visit(SgNode* node) override {
        if (SgFunctionDeclaration* func = isSgFunctionDeclaration(node)) {
            // Process function
        }
    }
};

int main(int argc, char* argv[]) {
    SgProject* project = frontend(argc, argv);
    MyAnalysis analysis;
    analysis.traverse(project, preorder);
    return 0;
}
```

### Node Construction

```cpp
#include "rose.h"

// Build a function call
SgFunctionCallExp* buildCall(SgFunctionSymbol* sym, SgExprListExp* args) {
    return SageBuilder::buildFunctionCallExp(sym, args);
}

// Insert statement
void insertBefore(SgStatement* target, SgStatement* newStmt) {
    SageInterface::insertStatementBefore(target, newStmt);
}
```

## Cross-Project References

Related ludoplex repositories:

| Repository | Relevance |
|------------|-----------|
| [docs-registry](../docs-registry/) | Documentation registry for Cursor |
| [cursor-project-scaffolding](../cursor-project-scaffolding/) | Project templates |
| [ggml](https://github.com/ludoplex/ggml) | Tensor library (ML integration) |
| [llvm-project](https://github.com/ludoplex/llvm-project) | Alternative compiler infrastructure |

---
Generated: 2025-12-03
Profile: rose-compiler
Registry: github-repos/docs-registry

