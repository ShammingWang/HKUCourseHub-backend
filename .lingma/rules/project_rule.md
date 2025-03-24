**Add rules to help the model understand your coding preferences, including preferred frameworks, coding styles, and other conventions.**
**Note: This file only applies to the current project, with each file limited to 10,000 characters. If you do not need to commit this file to a remote Git repository, please add it to .gitignore.**

您是 Python 3.10+ 方面的专家，请严格遵守以下编码规则：

## 类型注解规范

- 使用 Python 3.10+ 的类型/注解语法
- 只在必要时使用 `Any` 类型，如果使用了则必须保留
- 为所有函数参数和返回值添加类型注解，args, kwargs 参数直接忽略注解
- 为字典返回值添加具体的类型注解（如 `dict[str, Any]`）
- 为列表返回值添加具体的类型注解（如 `list[dict[str, str]]`）

## 文档注释规范

- 不要在文件开头添加注释
- 函数文档格式如下：
    1. 有参数的函数：
        - 使用多行文档字符串
        - 第一行写函数描述
        - 空一行
        - 参数说明格式为 ":param 参数名: 参数说明"
        - 返回说明格式为 ":return:"
    2. 无参数的函数：
        - 使用单行文档字符串
        - 只写函数描述
        - 描述和引号在同一行
    3. 通用要求：
        - 函数描述要简洁明了
        - 不需要举例说明
        - 中英文之间要有空格
- 参数说明要具体和清晰
- 如果函数没有入参且描述只有简短文字，那么引号和内容写在同一行
- 如果函数被 model_validator 或 field_validator 注释，则只需添加函数描述即可

## 代码逻辑规范

- 在保证逻辑清晰的情况下，尽量避免使用多元表达式（如三元运算符）
- 保持代码的可读性和可维护性
- 使用提前返回模式简化代码
- 移除不必要的中间变量
- 添加适当的空行，提高代码可读性
- 优先处理错误和边缘案例
- 只要必要时添加 try
- 对错误条件使用提前返回，以避免嵌套较深的 if 语句
- 避免不必要的 else 语句，而应使用 if-return 模式
- 实施适当的错误记录和用户友好型错误信息
- 使用自定义错误类型或错误工厂进行一致的错误处理

## 代码格式规范

- 统一代码风格
- 保持适当的空行
- 优化长行（超过 120 个字符）的格式
- 使用括号进行换行
- 保持一致的缩进

## 代码注释规范

- 每个 py 文件开头都需添加以下内容
    ```
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    ```
- 合理的注释，避免不必要的注释
- 中英文之间应包加空格
- 注释文字描述应具体和清晰
- 注释要让人视觉上更清晰

## 命名规范

- 变量名要具有描述性
- 避免使用单字母变量名（除非是循环变量）
- 使用下划线命名法（snake_case）
- 类名使用大驼峰命名法（PascalCase）

## 函数定义规范

- 纯函数使用 `def`
- 异步操作使用 `async def`
- 函数尽量单一职责，避免过于复杂的函数，但也不要过于琐碎
- 不要擅自修改任何参数命名