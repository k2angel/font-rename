# font-rename
font-rename は、フォントファイル（.ttf, .otf）のファイル名を、フォント内部のPostScript名に一括リネームするためのコマンドラインツールです。

## installation
```bash
pip install git+https://github.com/k2angel/font-rename.git
```

## usage
```bash
font-rename [OPTIONS] <PATH...>
```

### example
`font-rename`は、複数のファイルパスやディレクトリパスを引数として受け付けます。

 - 単一のファイルをリネームする
```bash
font-rename example.ttf
```
 - 複数のファイルをリネームする
```bash
font-rename example1.ttf example2.ttf
```
 - ディレクトリ内のすべてのフォントファイルをリネームする
```bash
font-rename ./fonts
```
 - 複数のパスを組み合わせて指定する
```bash
font-rename example1.ttf example2.ttf ./fonts
```

### options
| オプション名          | 説明                            |
|-----------------|:------------------------------|
| -d, --dry-run   | 実際のリネームは行わず、変更されるファイル名を表示します。 |
| -r, --recursive | ディレクトリ内のサブディレクトリも再帰的に探します。    |