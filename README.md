

*Say hello to the world.*

## Installation

clone:
```
$ git clone https://github.com/h1s97x/flask_app.git
$ cd app
```
create & activate virtual env then install dependency:

with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```

## 代码库架构

基于Flask的Web应用程序，整体架构：

1. **根目录文件**：
   - `.env` 和 `.flaskenv`：这些文件通常用于存储环境变量，如数据库连接字符串、应用密钥等。这些变量在运行时被Flask应用读取。
   - `.git` 和 `.gitignore`：与Git版本控制相关。
   - `data.db`：可能是SQLite数据库文件，用于存储应用数据。
   - `doc`：可能包含项目的文档或说明文件。
   - `environment.yaml`：可能是用于定义不同环境（如开发、测试、生产）的配置文件。
   - `LICENSE`、 README.md 、`setup.py`：项目的许可证、说明文件和安装脚本。
   - `Pipfile` 和 `Pipfile.lock`：使用Pipenv进行Python依赖管理的相关文件。
   - `wsgi.py`：用于部署的WSGI服务器入口点。
2. **应用主体（`app/` 目录）**：
   - `commands.py`：自定义的Flask命令，可用于执行特定任务，如数据迁移、清理等。
   - `config.py`：包含应用的配置信息，如数据库连接、调试模式、应用密钥等。
   - `errors.py`：定义错误处理逻辑，如自定义错误页面、错误日志记录等。
   - `extensions.py`：初始化和配置Flask应用的扩展，例如数据库连接（如Flask-SQLAlchemy）、邮件发送（如Flask-Mail）等。
   - `forms.py`：定义表单类，用于验证用户通过HTML表单提交的数据。
   - `models.py`：定义数据模型，这些模型通常与数据库表对应，并用于ORM（对象关系映射）操作。
   - `settings.py`：应用级别的设置或常量，可能包括一些全局配置或默认值。
   - `views.py`：包含处理用户请求的视图函数。这些函数接收请求，执行逻辑，并返回响应。
   - `__init__.py`：初始化Flask应用，加载配置、扩展和路由。这通常是应用的入口点。
3. **模板和静态文件**：
   - `templates/`：存放HTML模板文件。这些文件使用Jinja2模板引擎（Flask默认使用的模板引擎）来动态渲染页面内容。
   - `static/`：存放静态资源文件，如CSS样式表、JavaScript脚本和图片。这些文件在客户端浏览器中加载和运行。 总的来说，这个Flask项目遵循了典型的MVC架构模式，其中模型（M）负责数据处理，视图（V）负责页面展示，而控制器（C）的逻辑则分散在视图函数和其他处理用户请求的部分中。这种架构有助于保持代码的清晰和可维护性。

### 总结

该代码库是一个结构清晰的Flask Web应用程序，遵循了典型的MVC（模型-视图-控制器）架构模式。其中，`models.py`负责数据模型（M），`views.py`负责处理用户请求并返回响应（C），而`templates/`目录下的HTML文件则负责页面展示（V）。此外，应用还通过`extensions.py`、`forms.py`等文件提供了丰富的功能和验证机制。
