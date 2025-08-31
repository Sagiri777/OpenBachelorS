#!/bin/bash
# macOS开发环境启动脚本

echo "启动OpenBachelorS开发服务器..."

# 检查Poetry是否安装
if ! command -v poetry &> /dev/null; then
    echo "错误: Poetry未安装，请先安装Poetry"
    echo "安装命令: curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

# 检查虚拟环境
if [ ! -d ".venv" ]; then
    echo "创建虚拟环境..."
    poetry install
fi

# 启动开发服务器
echo "启动开发服务器 (端口: 8443)..."
poetry run poe dev