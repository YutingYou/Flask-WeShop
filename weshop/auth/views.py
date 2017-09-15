# -*- coding: utf-8 -*-
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    pass
    # if form.validate_on_submit():
    #     user = UserBaseInfo.query.filter_by(email=form.email.data).first()
    #     if user is not None and user.verify_password(form.password.data):
    #         flash('登录成功')
    #         login_user(user, form.remember_me.data)
    #         return redirect(request.args.get('next') or url_for('homepage.index'))
    #     flash('无效的用户名或密码。')
    # return render_template('auth/login.html', form=form)
