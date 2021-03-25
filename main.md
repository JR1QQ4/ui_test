# UI 测试

## PageObject

### 六大原则

- The public methods represent the services that the page offers
    - 公共方法表示页面提供的服务
    
- Try not to expose the internals of the page
    - 不要暴露页面的细节
    
- Generally don't make assertions
    -Page 设计中不要出现断言，应该写在测试用例类中

- Methods return other PageObjects
    - 方法应该返回其他的 Page 对象

- Need not represent an entire page
    - 不要去代表整个 page，如果一个页面中有很多功能，只需要对重点功能封装方法即可

- Different results for the same action are modeled as different methods
    - 不同的结果返回不同的方法，不同的模式

### 登录问题

#### 解决方法一: 浏览器复用

- 步骤1: 把浏览器放入环境变量
- 步骤2: 开启浏览器调试模式 `chrome --remote-debugging-port=9222`
- 步骤3: `options=Options();options.debugger_address="127.0.0.1:9222"` 此时不需要重新打开页面

## 技巧

### 生成 requirements.txt 以及安装依赖

- 生成 requirements.txt: `$ pip freeze > requirements.txt`
- 使用 requirements.txt 安装依赖: `$ pip install -r requirements.txt`
