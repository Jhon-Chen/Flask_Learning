from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'qwoeufkljniuc'


@app.route('/')
def index():
    return 'index'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if not all([username, password, password2]):
            # 向前端界面弹出一条提示(闪现消息)
            flash("参数不足")
        elif password != password2:
            flash("两次密码不一致")
        else:
            # 假装做注册操作
            print(username, password, password2)
            return "success"
    return render_template('temp5_WTF.html')


if __name__ == '__main__':
    app.run(debug=True)