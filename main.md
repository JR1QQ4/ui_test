# Selenium 自动化测试(Python 版)

## 一、环境搭建

- Selenium 三剑客: WebDriver、IDE、Grid
- 下载 Python: `https://www.python.org/downloads/`
- 下载安装浏览器驱动: `https://www.selenium.dev/documentation/en/webdriver/driver_requirements/`
    - 把驱动文件配置到环境变量中，可以省略初始化中的 executable_path 参数
- 下载安装 JDK
- 下载 Selenium: `pip install selenium`

## 二、Selenium 核心技术

- Selenium 实现元素定位:
    - find_element_by_id
    - find_element_by_class_name
    - find_element_by_css_selector
    - find_element_by_xpath
    - find_elements_by_tag_name
    - find_element_by_link_text
    - find_element_by_partial_link_text
    - find_element_by_name
    - find_element
- Selenium WebDriver
    - 常用属性:
        - driver.current_url
        - driver.title
        - driver.page_source
        - driver.current_window_handle
        - driver.window_handles
    - 常用方法:
        - driver.back()
        - driver.forward()
        - driver.refresh()
        - driver.close()
        - driver.quit() 
        - driver.switch_to.frame()
        - driver.switch_to.alert
        - driver.switch_to.active_element
        - driver.switch_to.window()
        - driver.switch_to.default_content()
- Selenium WebElement
    - 常用属性
        - id
        - size
        - rect
        - tag_name
        - text
    - 常用方法
        - webElement.send_keys()
        - webElement.click()
        - webElement.clear()
        - webElement.get_attribute("value")
        - webElement.is_selected()
        - webElement.is_enabled()
        - webElement.is_displayed()
        - webElement.value_of_css_property("font")
        - webElement.find_element()
- Selenium 操作 form 表单
    - 流程: 定位表单元素->输入测试值->判断表单元素属性->获得表单元素属性->提交表单进行验证
- Selenium 操作 checkbox 和 radiobutton
- Selenium 操作下拉列表
    - 常用属性:
        - selectElement.options
        - selectElement.all_selected_options
        - selectElement.first_selected_options
    - 常用方法:
        - selectElement.select_by_value()
        - selectElement.select_by_index()
        - selectElement.select_by_visible_text()
        - selectElement.deselect_by_index()
        - selectElement.deselect_by_value()
        - selectElement.deselect_by_visible_text()
        - selectElement.deselect_all()  
- Selenium 处理弹框
    - alertElement.accept()
    - alertElement.dismiss()
    - alertElement.send_keys()
    - alertElement.text
- Selenium 三种等待方式
    - time.sleep()
    - 隐式等待: driver.implicitly_wait()
    - 显示等待: WebDriverWait(driver, timeout, poll_frequency, ignored_exceptions)
        - 用法:
        - `from selenium.webdriver.support.wait import WebDriverWait`
        - `from selenium.webdriver.support import expected_conditions as EC`
        - `WebDriverWait(driver, 5, .5).until(EC.visibility_of_element_located((By.ID, "kw")))`
        - `WebDriverWait().until_not()`
- Selenium 等待条件
    - `from selenium.webdriver.support import expected_conditions as EC`
    - 常见的 expected_conditions:
        - `EC.title_is()`
        - `EC.title_contains()`
        - `EC.presence_of_element_located()`
        - `EC.visibility_of_element_located()`
        - `EC.visibility_of()`
        - `EC.presence_of_all_elements_located()`
        - `EC.visibility_of_all_elements_located()`
        - `EC.text_to_be_present_in_element()`
        - `EC.text_to_be_present_in_element_value()`
        - `EC.frame_to_be_available_and_switch_to_it()`
        - `EC.invisibility_of_element_located()`
        - `EC.element_to_be_clickable()`
        - `EC.staleness_of()`
        - `EC.element_to_be_selected()`
        - `EC.element_selection_state_to_be()`
        - `EC.element_located_selection_state_to_be()`
        - `EC.alert_is_present()`
        - `EC.url_contains()`
- Selenium 鼠标和键盘事件
    - 单击: `ActionChains(self.driver).click(on_element=None)`
    - 按下不放: `ActionChains(self.driver).click_and_hold(on_element=None)`
    - 鼠标右键点击: `ActionChains(self.driver).context_click(on_element=None)`
    - 双击: `ActionChains(self.driver).double_click(on_element=None)`
    - 拖拽: `ActionChains(self.driver).drag_and_drop(source=None, target=None)`
    - 拖拽: `ActionChains(self.driver).drag_and_drop_by_offset(source=None, xoffset=0, yoffset=0)`
    - 按下按键: `ActionChains(self.driver).key_down(value=Keys, element=None)`
    - 弹起按键: `ActionChains(self.driver).key_up(value=Keys, element=None)`
    - 鼠标移动: `ActionChains(self.driver).move_by_offset(xoffset=0, yoffset=0)`
    - 鼠标移动: `ActionChains(self.driver).move_to_element(to_element=None)`
    - 鼠标移动: `ActionChains(self.driver).move_to_element_with_offset(to_element=None, xoffset=0, yoffset=0)`
    - 移动到某个元素或鼠标弹起: `ActionChains(self.driver).release(on_element=None)`
    - 操作按键: `webElement.send_keys(Keys.CONTROL, "v")`
    - 点击某个元素并发送值: `ActionChains(self.driver).send_keys_to_element(element=None, *keys_to_send)`
    - 执行所有的事件: `ActionChains(self.driver).perform()`
- Selenium 执行 JavaScript 脚本
    - `self.driver.execute_script(js)`
- Selenium 屏幕截图
    - driver.save_screenshot()
    - driver.get_screenshot_as_base64()
    - driver.get_screenshot_as_file()
    - driver.get_screenshot_as_png()

## 三、Selenium IDE

- 下载安装 Selenium IDE: 浏览器插件
- Selenium IDE 的基本用法
- Selenium IDE 实现录制和回放及脚本导出

## 四、项目实战

- 环境搭建: JDK+Tomcat+MySql+Jpress
- 需求分析和用例设计
    - 测试点
        - 用户注册: http://localhost:8080/jpress/user/register
        - 用户登录: http://localhost:8080/jpress/user/login
        - 后台管理员登录: http://localhost:8080/jpress/admin/login
        - 文章分类: http://localhost:8080/jpress/admin/article/category
        - 添加文章: http://localhost:8080/jpress/admin/article/write
- PyAutoGUI 模块处理常规方法无法操作的问题
    - 安装: `pip install pyautogui`
    - `pyautogui.position(x=None, y=None)`
    - `pyautogui.moveTo(x=None, y=None[, duration=t])`
    - `pyautogui.mouseDown(x=None, y=None)`
    - `pyautogui.mouseUp(x=None, y=None)`
    - `pyautogui.click(x=None, y=None)`
    - `pyautogui.doubleClick(x=None, y=None)`
    - `pyautogui.rightClick(x=None, y=None)`
    - `pyautogui.middleClick(x=None, y=None)`
    - `pyautogui.dragTo(x=None, y=None[, duration=t])`
    - `pyautogui.typewrite(s[, duration=t])`
- 验证码处理
    - 方案一: pytesseract 模块和 PIL 模块处理简单验证码
        - 安装: `pip install pytesseract`、`pip install Pillow`
    - 方案二: 第三方 API
    - 方案三: 使用 cookie
        - jpress 使用 cookie 登录需要传入 csrf_token、_jpuid
    - 方案三: 浏览器复用
        - 步骤1: 把浏览器放入环境变量
        - 步骤2: 开启浏览器调试模式 `chrome --remote-debugging-port=9222`
        - 步骤3: `options=Options();options.debugger_address="127.0.0.1:9222"` 此时不需要重新打开页面
- 项目架构设计 -> 完成项目基本测试 -> 解决验证码问题 -> 完成项目测试用例

## 五、使用 unittest 框架重构项目

- unittest 框架简介
- unittest 中的类方法和实例方法
- 测试用例和测试套件
- 使用 unittest 重构测试用例
- 为项目生成测试报告

## 六、使用 pytest 重构项目

- pytest 框架简介
- pytest 标记
- pytest 参数化处理
- pytest Fixture
- pytest allure 生成测试报告
- 使用 pytest 重构项目

## 八、用 ddt 思想重构项目

- Selenium 读取 CSV 文件
- Selenium 读取 XML 文件
- Selenium 读取 JSON 文件
- Selenium 读取 Excel 文件
- Selenium 读取 ini 配置文件
- Selenium 读取数据库数据
- Selenium 参数化测试
- Selenium ddt
- 使用 ddt 思想重构项目

## 九、用 POM 设计模式重构项目

- POM 设计模式简介
- 设计 BasePage 类
- 设计项目页面对应的 PO 类
- 设计项目测试用例
- 综合项目测试

## 十、Selenium Grid 分布式测试

- Selenium Grid 下载安装
- Selenium 远程测试-客户端
- Selenium 分布式测试 Grid
- Selenium 注册 node 节点
- Selenium Grid 实现分布式测试

## 十一、持续集成和交付

- Jenkins 环境搭建
- 项目环境配置
- 邮件通知
- 定时项目执行

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
