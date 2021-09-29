# Generating E2e Model to IREE

## Initial/First Time Setups
### VirtualEnv Setup
```bash
pip install virtualenv
virtualenv -p /usr/bin/python3.9 ModelCompilerEnv
source ModelCompilerEnv/bin/activate
```
### Installing Miscallaneous Deps
```bash
pip install tensorflow
pip install gin-config
```
### Installing IREE-Python
```bash
python -m pip install \
  iree-compiler-snapshot \
  iree-runtime-snapshot \
  iree-tools-tf-snapshot \
  iree-tools-tflite-snapshot \
  iree-tools-xla-snapshot \
  --find-links https://github.com/google/iree/releases
```

### Getting ModelCompiler
```bash
git clone https://github.com/raikonenfnu/ModelCompiler
cd ModelCompiler
git submodule update --init --recursive 
```

## Generating IREE Model
```bash
cd ModelCompiler
export PYTHONPATH=$PYTHONPATH:$PWD/third_party/tf_models
cd nlp_gen
python bert_small_gen.py # should generate it to /tmp/model.mlir
```
