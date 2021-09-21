# IREE "Torch Tanh Static Library for RISCV Backend" sample

## Environment Setup
```sh
export RISCV_TOOLCHAIN_ROOT=/home/stanley/riscv/toolchain/clang/linux/RISCV
```

## Generating your own Kernels from Torch
If you'd like to generate the tanh.mlir file by yourself, then you have to
build mlir-npcomp with torch [as seen here](https://github.com/llvm/mlir-npcomp/blob/main/README.md).
Once you have mlir-npcomp built, then run these commands:
```sh
export PYTHONPATH=$PYTHONPATH:/path/to/npcomp-build/python_packages/npcomp_core
export PYTHONPATH=$PYTHONPATH:/path/to/npcomp-build/python_packages/npcomp_torch
python torchscript_<kernel_name>_e2e_codegen.py
```