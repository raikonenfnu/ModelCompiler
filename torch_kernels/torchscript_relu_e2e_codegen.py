# -*- Python -*-
# This file is licensed under a pytorch-style license
# See frontends/pytorch/LICENSE for license information.

import typing

import torch
import torch_mlir

from Util import compile_to_mlir
import os

mb = torch_mlir.ModuleBuilder()

class TestModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        return torch.relu(x)

test_module = TestModule()
class_annotator = torch_mlir.ClassAnnotator()
recursivescriptmodule = torch.jit.script(test_module)
torch.jit.save(recursivescriptmodule, '/tmp/foo.pt')

class_annotator.exportNone(recursivescriptmodule._c._type())
class_annotator.exportPath(recursivescriptmodule._c._type(), ['forward'])
class_annotator.annotateArgs(recursivescriptmodule._c._type(), ['forward'], [
    None,
    ([4], torch.float32, True)
])
# TODO: Automatically handle unpacking Python class RecursiveScriptModule into the underlying ScriptModule.
mb.import_module(recursivescriptmodule._c, class_annotator)
#mb.module.operation.print()

compiled = compile_to_mlir(mb.module)
mlir_path = "riscv_relu.mlir"
with open(mlir_path, "wt") as output_file:
    output_file.write(compiled)