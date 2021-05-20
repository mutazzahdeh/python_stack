Microsoft Windows [Version 10.0.19042.928]
(c) Microsoft Corporation. All rights reserved.

C:\Users\User\Desktop\ormfirst\orm>cd orm

C:\Users\User\Desktop\ormfirst\orm\orm>code .

C:\Users\User\Desktop\ormfirst\orm\orm>cd..

C:\Users\User\Desktop\ormfirst\orm>cd..

C:\Users\User\Desktop\ormfirst>cd..

C:\Users\User\Desktop>cd Python_stackax

C:\Users\User\Desktop\Python_stackax>cd My_enviroments

C:\Users\User\Desktop\Python_stackax\My_enviroments>call py3Env/scripts/activatey
'py3Env' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\User\Desktop\Python_stackax\My_enviroments>call py3Env/scripts/activate
(py3Env) C:\Users\User\Desktop\Python_stackax\My_enviroments>cd..

(py3Env) C:\Users\User\Desktop\Python_stackax>cd..

(py3Env) C:\Users\User\Desktop>cd ormfirst

(py3Env) C:\Users\User\Desktop\ormfirst>cd orm

(py3Env) C:\Users\User\Desktop\ormfirst\orm>cd orm

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm>cd orm

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm\orm>cd.

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm\orm>cd..

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 20, 2021 - 14:04:49
Django version 3.2.3, using settings 'orm.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[20/May/2021 14:04:55] "GET / HTTP/1.1" 200 8
Microsoft Windows [Version 10.0.19042.928]
(c) Microsoft Corporation. All rights reserved.

C:\Users\User\Desktop\ormfirst\orm>cd orm

C:\Users\User\Desktop\ormfirst\orm\orm>code .

C:\Users\User\Desktop\ormfirst\orm\orm>cd..

C:\Users\User\Desktop\ormfirst\orm>cd..

C:\Users\User\Desktop\ormfirst>cd..

C:\Users\User\Desktop>cd Python_stackax

C:\Users\User\Desktop\Python_stackax>cd My_enviroments

C:\Users\User\Desktop\Python_stackax\My_enviroments>call py3Env/scripts/activatey
'py3Env' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\User\Desktop\Python_stackax\My_enviroments>call py3Env/scripts/activate
(py3Env) C:\Users\User\Desktop\Python_stackax\My_enviroments>cd..

(py3Env) C:\Users\User\Desktop\Python_stackax>cd..

(py3Env) C:\Users\User\Desktop>cd ormfirst

(py3Env) C:\Users\User\Desktop\ormfirst>cd orm

(py3Env) C:\Users\User\Desktop\ormfirst\orm>cd orm

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm>cd orm

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm\orm>cd.

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm\orm>cd..

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 20, 2021 - 14:04:49
Django version 3.2.3, using settings 'orm.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[20/May/2021 14:04:55] "GET / HTTP/1.1" 200 8

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm>python manage.py makemigrations\
Unknown command: 'makemigrations\\'. Did you mean makemigrations?
Type 'manage.py help' for usage.

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm>python manage.py makemigrations
Migrations for 'app':
  app\migrations\0001_initial.py
    - Create model users

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, app, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying app.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

(py3Env) C:\Users\User\Desktop\ormfirst\orm\orm>python manage.py shell
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from app.models import users
>>> users.objects.create(first_name:'haitham', last_name:'abbas', email_address:'hddsklnfs', age:'23')
  File "<console>", line 1
    users.objects.create(first_name:'haitham', last_name:'abbas', email_address:'hddsklnfs', age:'23')
                                   ^
SyntaxError: invalid syntax
>>> users.objects.create(first_name='haitham', last_name='abbas', email_address='hddsklnfs', age='23')
<users: users object (1)>
>>> users.objects.create(first_name='mutaz', last_name='zahdeh', email_address='asfaasdfas', age='24')
<users: users object (2)>
>>> users.objects.create(first_name='Mia', last_name=Sharapovaa', email_address='sdsasa', age='34')
  File "<console>", line 1
    users.objects.create(first_name='Mia', last_name=Sharapovaa', email_address='sdsasa', age='34')
                                                                                ^
SyntaxError: invalid syntax
>>> users.objects.create(first_name='Mia', last_name='Sharapovaa', email_address='sdsasa', age='34')
<users: users object (3)>
>>> users.objects.all()
<QuerySet [<users: users object (1)>, <users: users object (2)>, <users: users object (3)>]>
>>> users.objects.all()
<QuerySet [<users: users object (1)>, <users: users object (2)>, <users: users object (3)>]>
>>> users.objects.first()
<users: users object (1)>
>>> code .
  File "<console>", line 1
    code .
         ^
SyntaxError: invalid syntax
>>> users.objects.all().value()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'value'
>>> users.objects.get(id=1)
<users: users object (1)>
>>> hello=users.object.first()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'users' has no attribute 'object'
>>> users.objects.all()
<QuerySet [<users: users object (1)>, <users: users object (2)>, <users: users object (3)>]>
>>> users.objects.all().value
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'value'
>>> users.objects.all().values
<bound method QuerySet.values of <QuerySet [<users: users object (1)>, <users: users object (2)>, <users: users object (3)>]>>
>>> users.objects.last()
<users: users object (3)>
>>> c = users.objects.get(id=3)
>>> c.last_name='pancakes'
>>> c.save
<bound method Model.save of <users: users object (3)>>
>>> c.save()
>>> users_to_delete = users.objects.get(id=2)
>>> users_to_delete.delete()
(1, {'app.users': 1})
>>> users.objects.all().order_by("first_name")
<QuerySet [<users: users object (3)>, <users: users object (1)>]>
>>>
