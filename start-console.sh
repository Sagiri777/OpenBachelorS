#!/bin/bash
# macOS控制台启动脚本

echo "启动OpenBachelorS控制台..."

# 检查Poetry是否安装
if ! command -v poetry &> /dev/null; then
    echo "错误: Poetry未安装，请先安装Poetry"
    echo "安装命令: curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

# 启动控制台
poetry run console