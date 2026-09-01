## Creacíon de superusuario de prueba
Para crear un superusuario de prueba en Django, ejecutar el siguiente comando desde la carpeta del proyecto:
```
     python manage.py createsuperuser
```
Completar los datos solicitados:
```
    Username: admin
    Email address: admin@gmail.com
    Password: admin
    Password (again): admin
```
Cuando Django solicite confirmación para utilizar una contraseña débil, seleccionar **"y"**:
```
    The password is too similar to the username.
    This password is too short. It must contain at least 8 characters.
    Bypass password validation and create user anyway? [y/N]: y
```
Una vez completado el proceso, el superusuario quedará creado y podrá utilizarse para acceder al panel administrativo de Django.