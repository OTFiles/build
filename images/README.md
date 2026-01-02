# 图片 OCR 识别

本目录用于存放需要进行 OCR 识别的图片文件。

## 使用方法

### 自动触发
1. 将图片文件（支持格式：jpg, jpeg, png, webp, bmp）上传到本目录
2. 提交并推送到 GitHub 仓库
3. GitHub Actions 会自动触发 OCR 识别任务
4. 识别结果会保存到 `texts/` 目录中

### 手动触发
1. 在 GitHub 仓库的 Actions 页面找到 "OCR Image Recognition" workflow
2. 点击 "Run workflow"
3. 选择 "Process all images in the images directory" 选项
4. 点击 "Run workflow" 按钮
5. 所有图片的识别结果会保存到 `texts/` 目录中

## 支持的图片格式

- JPG
- JPEG
- PNG
- WEBP
- BMP

## 识别结果

识别结果会保存在 `texts/` 目录中，文件名与原图片文件名相同（扩展名为 .txt）

## 技术细节

- 使用 Umi-OCR 进行 OCR 识别
- 支持中文识别
- 自动进行排版解析

*最后测试：2026年1月2日*