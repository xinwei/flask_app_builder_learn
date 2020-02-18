from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from .models import Article
from . import appbuilder, db
"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""
class ArticleModelView(ModelView):
    datamodel = SQLAInterface(Article)
    list_title = '文章列表'
    add_title = '添加文章'
    edit_title = '修改文章'
    # 修改列名称
    label_columns = {'id':'编号','title':'题目','date':'日期','context':'内容','keys':'关键字'}
    #定义列显示名称
    list_columns = ['id','title','context'] #定义视图中要显示的字段


@appbuilder.app.errorhandler(404)
def page_not_found(e):
 return (render_template("404.html", base_template=appbuilder.base_template, appbuilder=appbuilder),404,)


db.create_all()
appbuilder.add_view(ArticleModelView,'文章列表',icon = 'fa-address-card-o',category = '文章管理')

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
