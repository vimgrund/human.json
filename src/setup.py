from distutils.core import setup
import py2exe

setup(
    windows=[
        {
            "script": 'src/app.py',
            "icon_resources": [(1, "media/app-json.ico")]
        }
    ],
)
