# 導入
このGitHub Actionはリポジトリ上にあるMinecraft統合版のリソースパックを.mcpack形式に圧縮するものです。.で始まるディレクトリは無視され、(v2.1より).jsonで終わるファイルはデフォルトで軽量化(minify)されます。

# Bedrock Resource Pack Compressor v2 使用例
以下の構造を持つ _ExampleResourcePack_ というレポジトリをパックとして圧縮したいとします。 
```
ExampleResourcePack
├ manifest.json
├ animations
├ animation_controllers
└ ...
```

この場合,以下がリソースパックを成果物としてアップロードする例です。

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
        uses: famima65536/resourcepack-compressor@v2
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

この場合manifest.jsonがリポジトリ直下にあるため追加のパスをsourceで指定していませんが、aaaというフォルダにmanifest.jsonがある場合にはresourcepack/aaaが指定するパスとなります。

destinationはパックの出力先です。_pack-name_.packという名前で出力されます。