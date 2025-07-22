# ZipAutoPartRenamer
一个用于转换各种 .001 分卷压缩文件为标准命名格式的工具，便于在上传至某些云盘前整理文件

自动识别并重命名压缩分卷文件（7z / rar / zip），支持双向转换格式：

- `.7z.001` ↔ `-Part1.7z`
- `.rar.001` ↔ `-Part1.rar`
- `.zip.001` ↔ `-Part1.zip`

## 特性

- 支持 `.7z`, `.rar`, `.zip` 三种格式
- 自动识别当前命名格式并进行转换
- 双击可运行，无需额外操作
- 支持打包为单文件 `.exe`

## 用法

### 直接运行 python 文件

将脚本放入包含分卷文件的目录中，双击运行或命令行执行：

```bash
python auto_rename.py
```
## 编译为 exe
```bash
pyinstaller ZipAutoPartRenamer.spec
```
## 运行打包好的 exe

双击运行 ZipAutoPartRenamer.exe，程序会自动完成重命名。
示例
重命名前：
```
myfile.7z.001
myfile.7z.002
```
重命名后：
```
myfile-Part1.7z
myfile-Part2.7z
```
（反之亦然）

## 许可

MIT License © 2025 Radiumbit