# 初识Flask

2010.4.1，Armin Ronacher的愚人节玩笑。5天后Flask诞生。

Flask是用Python编写的Web微框架[^1]，Flask有两个主要依赖，一个是WSGI(Web Server Gateway Interface,Web服务器网关接口)工具集-Werkzeug(http://werkzeug.pocoo.org/)，另一个是Jinja2模板引擎(http://jinja.pocoo.org/)。Flask只保留了Web开发的核心功能，其他的功能都由外部扩展来实现，比如数据库集成、表单认证、文件上传等。

## 依赖项

在安装 Flask 时，将自动安装这些发行版。

- [Werkzeug](https://palletsprojects.com/p/werkzeug/) 实现 WSGI，它是应用程序和服务器之间的标准 Python 接口。
- [Jinja](https://palletsprojects.com/p/jinja/) 是一种模板语言，用于呈现应用程序提供的页面。
- [MarkupSafe](https://palletsprojects.com/p/markupsafe/) 附带 Jinja。在呈现模板时，它会转义不受信任的输入，以避免注入攻击。
- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/) 安全地对数据进行签名，以确保其完整性。这用于保护 Flask 的会话 Cookie。
- [Click](https://palletsprojects.com/p/click/) 是一个用于编写命令行应用程序的框架。它提供 `flask` 命令，并允许添加自定义管理命令。
- [Blinker](https://blinker.readthedocs.io/) 为 [信号](https://flask.org.cn/en/3.0.x/signals/) 提供支持。

### 可选依赖项

这些发行版不会自动安装。如果您安装它们，Flask 将检测并使用它们。

- [python-dotenv](https://github.com/theskumar/python-dotenv#readme) 在运行 `flask` 命令时支持 [dotenv 中的环境变量](https://flask.org.cn/en/3.0.x/cli/#dotenv)。
- [Watchdog](https://pythonhosted.org/watchdog/) 为开发服务器提供更快、更高效的重新加载器。



[^1]: 简单易于扩展

