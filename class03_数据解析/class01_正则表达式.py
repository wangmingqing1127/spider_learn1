"""
@Time ： 2024-06-10 08:58
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：正则表达式数据解析
"""
import requests

# 数据解析方式：1.正则表达式 2.xpath 3.BeautifulSoup

r"""
正则表达式（Regular Expression，简称Regex）是一种用于处理字符串的强大工具，它允许你按照特定的模式（pattern）来搜索、匹配、查找和替换文本。下面是一些常用的正则表达式知识点：
1. **基础匹配符**：
   - `.`：匹配除换行符以外的任意字符。
   - `[abc]`：匹配方括号内的任意字符（a、b 或 c）。
   - `[^abc]`：匹配不在方括号内的任意字符。
   - `a|b`：匹配 a 或 b。
   - `()`：标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。
2. **量词**：
   - `*`：匹配前面的子表达式零次或多次。
   - `+`：匹配前面的子表达式一次或多次。
   - `?`：匹配前面的子表达式零次或一次。
   - `{n}`：n 是一个非负整数，匹配确定的 n 次。
   - `{n,}`：至少匹配 n 次。
   - `{n,m}`：至少匹配 n 次且最多匹配 m 次。
3. **定位符**：
   - `^`：匹配输入字符串的开始位置。
   - `$`：匹配输入字符串的结束位置。
   - `\b`：匹配单词边界。
   - `\B`：匹配非单词边界。
4. **特殊字符**：
   - `\d`：匹配一个数字字符。等价于 `[0-9]`。
   - `\D`：匹配一个非数字字符。等价于 `[^0-9]`。
   - `\w`：匹配包括下划线的任何单词字符。等价于 `[A-Za-z0-9_]`。
   - `\W`：匹配任何非单词字符。等价于 `[^A-Za-z0-9_]`。
   - `\s`：匹配任何空白字符，包括空格、制表符、换行符等等。等价于 `[ \f\n\r\t\v]`。
   - `\S`：匹配任何非空白字符。等价于 `[^ \f\n\r\t\v]`。
5. **贪婪与懒惰**：
   - 贪婪模式：正则表达式会匹配尽可能多的字符。例如，`.*` 会匹配整个字符串。
   - 懒惰模式：正则表达式会匹配尽可能少的字符。在量词后面加上 `?` 即可启用懒惰模式，例如 `.*?`。
6. **分组与引用**：
   - 使用 `()` 可以对表达式进行分组，以便使用量词或进行反向引用。
   - 反向引用：比如 `\1`，表示引用第一个分组匹配的内容。
7. **零宽断言**：
   - `(?=...)`：正向预查，匹配 ... 前面的位置。
   - `(?!...)`：负向预查，匹配不是 ... 前面的位置。
   - `(?<=...)`：正向后查，匹配 ... 后面的位置。
   - `(?<!...)`：负向后查，匹配不是 ... 后面的位置。
这些是正则表达式的一些基础和常用知识点。正则表达式的强大之处在于它的灵活性和多样性，可以用于各种复杂的字符串处理任务。

"""

# 图片写入：爬取百度头像，保存到本地
if __name__ == '__main__':
    # 1.准备测试数据
    url = 'https://himg.bdimg.com/sys/portraitn/item/public.1.cf828361.RUOBQh2thZ5C1WgoqjTdaQ'
    # 2.模拟请求发送数据
    result = requests.get(url=url)  # text(字符串)、json(json数据对象)、content(二进制)
    # 3.解析响应数据并保存到本地
    with open('../data/baidu.jpg', 'wb') as f:
        f.write(result.content)
