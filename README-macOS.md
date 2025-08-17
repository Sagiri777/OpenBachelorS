# OpenBachelorS macOS 安装和运行指南

## 系统要求

- macOS 10.15 或更高版本
- Python 3.12 或更高版本
- 至少 2GB 可用磁盘空间

## 快速开始

### 1. 自动设置环境

运行自动设置脚本：

```bash
./setup-macos.sh
```

这个脚本会自动：
- 检查Python版本
- 安装Poetry（如果未安装）
- 安装aria2（通过Homebrew）
- 安装项目依赖
- 设置脚本执行权限

### 2. 启动服务

#### 开发环境
```bash
./start-dev.sh
```
- 启动开发服务器
- 支持热重载
- 监听端口：8443

#### 生产环境
```bash
./start-prod.sh
```
- 启动生产服务器
- 多进程模式
- 监听端口：8443

#### 控制台工具
```bash
./start-console.sh
```
- 启动交互式控制台
- 用于管理游戏数据

## 手动安装步骤

如果自动设置脚本失败，可以按照以下步骤手动安装：

### 1. 安装依赖

#### 安装Homebrew（如果未安装）
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 安装Python 3.12+
```bash
brew install python@3.12
```

#### 安装Poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```

#### 安装aria2
```bash
brew install aria2
```

### 2. 安装项目依赖
```bash
poetry install
```

### 3. 设置脚本权限
```bash
chmod +x start-dev.sh start-console.sh start-prod.sh setup-macos.sh
```

## 配置说明

### 环境变量

项目支持以下环境变量：

- `PROD_FLAG`: 设置为1启用生产模式
- `DATABASE_URL`: 数据库连接URL（可选）

### 配置文件

主要配置文件位于 `conf/` 目录：

- `config.json`: 主配置文件
- `version.json`: 版本信息
- `assist.json`: 助战配置
- `squad.json`: 编队配置

## 常见问题

### Q: Poetry安装失败
A: 确保Python 3.12+已正确安装，然后重新运行安装命令。

### Q: aria2命令未找到
A: 运行 `brew install aria2` 安装aria2。

### Q: 端口8443被占用
A: 修改 `pyproject.toml` 中的端口配置，或停止占用该端口的进程。

### Q: 权限被拒绝
A: 运行 `chmod +x *.sh` 给脚本添加执行权限。

## 开发说明

### 项目结构
```
OpenBachelorS/
├── src/openbachelors/          # 主要源代码
│   ├── bp/                     # 蓝图（路由）
│   ├── const/                  # 常量定义
│   ├── tool/                   # 工具脚本
│   └── util/                   # 工具函数
├── conf/                       # 配置文件
├── data/                       # 游戏数据
├── res/                        # 游戏资源
└── asset/                      # 资源文件
```

### 开发命令

```bash
# 运行测试
poetry run pytest

# 代码格式化
poetry run ruff check --fix

# 启动开发服务器
poetry run poe dev

# 启动生产服务器
poetry run poe prod
```

## 支持

如果遇到问题，请检查：

1. Python版本是否为3.12+
2. Poetry是否正确安装
3. 所有依赖是否安装完成
4. 脚本是否有执行权限

更多信息请参考项目文档或提交Issue。