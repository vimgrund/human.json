python %~dp0/src/setup.py py2exe

mkdir "%~dp0dist\media"
copy "%~dp0media\app-json.ico" "%~dp0dist\media\app-json.ico"


@pause