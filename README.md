# font-rename
font-rename は、フォントファイル（.ttf, .otf）のファイル名を、フォント内部のPostScript名に一括リネームするためのコマンドラインツールです。

## installation


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
 - ディレクトリ内のサブディレクトリも再帰的に検索する
```bash
font-rename --recursive ./fonts
```
 - 複数のパスを組み合わせて指定する
```bash
font-rename example1.ttf example2.ttf ./fonts
```