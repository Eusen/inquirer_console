"""
Inquirer.js风格的命令行提示模块的Python实现。

本模块提供了交互式命令行用户界面，用于轻松收集用户输入。

示例：
```python
from inquirer_console import Inquirer, Input, Confirm, List, Checkbox, Password

# 使用单独的提示
name = Input(message="你的名字是?").prompt()

# 或者使用Inquirer链式调用
answers = Inquirer().prompt([
    {
        'type': 'input',
        'name': 'name',
        'message': '你的名字是?'
    },
    {
        'type': 'list',
        'name': 'favorite_lang',
        'message': '你最喜欢的编程语言是?',
        'choices': ['Python', 'JavaScript', 'Rust']
    }
])

print(f"你好, {answers['name']}!")
print(f"你喜欢 {answers['favorite_lang']}!")
```
"""
from .prompt import Inquirer, BasePrompt, ExitPromptError
from .prompts.input import Input
from .prompts.confirm import Confirm
from .prompts.select import Select
from .prompts.checkbox import Checkbox
from .prompts.password import Password
from .prompts.text import Text

# 创建和配置全局Inquirer实例
inquirer = Inquirer()
inquirer.register_prompt('input', Input)
inquirer.register_prompt('confirm', Confirm)
inquirer.register_prompt('list', Select)
inquirer.register_prompt('checkbox', Checkbox)
inquirer.register_prompt('password', Password)
inquirer.register_prompt('text', Text)

# 导出所有内容以便用户导入
__all__ = [
    'Inquirer',
    'BasePrompt',
    'ExitPromptError',
    'Input',
    'Confirm',
    'Select',
    'Checkbox',
    'Password',
    'Text',
    'inquirer'
]
