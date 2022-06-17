# Introduction
This is a github action to compress resource pack for Minecraft Bedrock Edition on you repository into .pack style ignoring directory starting wih dot (e.g. .test) and minify json files (from v2.1).


# Bedrock Resource Pack Compressor v2.1
If you want to compress in repository, _ExampleResourcePack_ that has directory structure below.
```
ExampleResourcePack
├ manifest.json
├ animations
├ animation_controllers
└ ...
```

In this case, below is an example to upload resource pack as an artifact.

```yml

name: compress

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: checkout
        uses: actions/checkout@v3
        with:
          path: resourcepack

      - name: compress pack
        uses: famima65536/resourcepack-compressor@v2.1
        with:
          source: resourcepack
          destination: artifact
          pack-name: ExamplePack
          # minify: true
      - name: upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: resourcepack
          path: artifact/ExamplePack.mcpack
```