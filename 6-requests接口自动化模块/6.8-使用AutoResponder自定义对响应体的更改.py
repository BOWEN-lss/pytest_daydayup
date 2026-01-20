"""
使用autoresponder自定义对响应体的更改

点击autoresponder 按钮 ，勾选左侧第一个单选框 enable rules ，此时直接打开要抓包的网址会报错如下：
[Fiddler] The Fiddler AutoResponder is enabled, but this request did not match any of the listed rules. 
Because the "Unmatched requests passthrough" option on the AutoResponder tab is not enabled, this HTTP/404 response has been generated. 
因为我们没有勾选第三个单选框 unmatched requests passthrough ，所以会返回404错误
勾选上之后就正常了

添加规则 ：
1.点击 add rule 按钮
2.填写规则 常用方法是直接copy网址的url粘贴进去，在下方一行自定义响应体内容（响应内容下拉框自选）
"""



