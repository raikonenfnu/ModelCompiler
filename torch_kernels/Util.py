import npcomp
from npcomp.passmanager import PassManager
from npcomp.compiler.pytorch.backend import iree

def compile_to_mlir(imported_module):
    with npcomp.ir.Context() as ctx:
        npcomp.register_all_dialects(ctx)
        module = npcomp.ir.Module.parse(str(imported_module))

    pipeline_str = "torchscript-to-npcomp-backend-pipeline,npcomp-backend-to-iree-frontend-pipeline"
    with module.context:
        pm = PassManager.parse(pipeline_str)
        pm.run(module)
    return str(module)
