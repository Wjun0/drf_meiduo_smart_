1. 用户部分-QQ登录(Step3-保存QQ登录绑定数据-API接口设计与实现)

   ```http
   API接口设计:
   	POST /oauth/qq/user/
   	参数：
   		{
               "mobile": "手机号",
               "password": "密码",
               "sms_code": "短信验证码",
               "access_token": "加密openid"
   		}
   	响应:
   		{
               "id": "用户id",
               "username": "用户名",
               "token": "jwt token"
   		}
   ```

2. 用户部分-QQ登录(Step3-前端vue逻辑)

3. 用户部分-登录用户个人信息获取(API接口设计与实现-基本业务流程)

   ```http
   API接口设计:
   	GET /user/
   	参数:
   		通过请求头`Authorization`把jwt token传递给服务器
   		`Authorization`: JWT <jwt token内容>
   	响应:
   		{
   			"id": "用户id"
               "username": "用户名",
               "mobile": "手机号",
               "email": "邮箱",
               "email_active": "邮箱验证标记"
   		}
   
   request.user:
       1. 如果用户已认证，request.user就是登录的用户的对象
       2. 如果用户未认证，request.user是一个匿名用户类的对象
   ```

4. 用户部分-登录用户个人信息获取(API接口设计与实现-代码优化)

   ```http
   重新get_object:
   
   def get_object(self):
   	# self.request: 获取请求对象
   	return self.request.user
   ```

5. 用户部分-登录用户个人信息获取(前端vue逻辑)

   ```http
   在进入`user_center_info.html`页面时，向后端发起请求，获取登录用户个人信息并进行展示。
   ```

6. 用户部分-登录用户邮箱设置(API接口设计与实现-基本业务)

   ```http
   API接口设计:
   	PUT /email/
   	参数:
   		通过请求头`Authorization`把jwt token传递给服务器
   		{
               "email": "邮箱"
   		}
   	响应:
   		{
   			"id": "用户id",
               "email": "邮箱"
   		}
   		
   基本业务逻辑：
   1. 获取登录用户
   2. 获取email参数并进行校验(email必传，email格式)
   3. 设置登录用户的邮箱并给邮箱发送验证邮件
   4. 返回应答，邮箱设置成功
   ```

7. 用户部分-登录用户邮箱设置(Django框架邮件发送配置)

8. 用户部分-登录用户邮箱设置(API接口设计与实现-验证链接生成&Celery发送邮件)

9. 用户部分-登录用户邮箱设置(前端vue逻辑)

10. 用户部分-用户邮箱验证(API接口设计与实现)

11. 用户部分-用户邮箱验证(前端vue逻辑)

    

