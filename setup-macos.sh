#!/bin/bash
# macOS环境设置脚本

echo "设置OpenBachelorS macOS环境..."

# 检查Python版本
python_version=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
required_version="3.12"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "错误: 需要Python $required_version或更高版本，当前版本: $python_version"
    echo "请安装Python 3.12+: https://www.python.org/downloads/"
    exit 1
fi

# 检查并安装Poetry
if ! command -v poetry &> /dev/null; then
    echo "安装Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
    echo "Poetry已安装，请重新打开终端或运行: source ~/.zshrc"
else
    echo "Poetry已安装"
fi

# 检查并安装aria2
if ! command -v aria2c &> /dev/null; then
    echo "检测到缺少aria2，尝试安装..."
    if command -v brew &> /dev/null; then
        echo "使用Homebrew安装aria2..."
        brew install aria2
    else
        echo "警告: 未检测到Homebrew，请手动安装aria2:"
        echo "1. 安装Homebrew: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        echo "2. 安装aria2: brew install aria2"
    fi
else
    echo "aria2已安装"
fi

# 安装项目依赖
echo "安装项目依赖..."
poetry install

# 设置脚本执行权限
chmod +x start-dev.sh
chmod +x start-console.sh
chmod +x start-prod.sh

echo "macOS环境设置完成！"
echo ""
echo "使用方法:"
echo "  开发环境: ./start-dev.sh"
echo "  生产环境: ./start-prod.sh"
echo "  控制台:   ./start-console.sh"