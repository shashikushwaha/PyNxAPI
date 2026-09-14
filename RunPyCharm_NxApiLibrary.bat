set UGII_ENV_FILE=%UGII_BASE_DIR%\ugii_env.dat
set PYTHONPATH=%UGII_BASEDIR%\NXBIN\python;C:\Python\Python36;C:\Python\Python36\Lib;C:\Python\Python36;C:\Python\Python36\Lib\site-packages
set path=%UGII_BASE_DIR%\NXBIN;%UGII_BASE_DIR%\UGII;%UGII_BASE_DIR%\UGOPEN;%path%
set PY_CHARM_ENV=C:\Program Files\JetBrains\PyCharm Community Edition 2024.3.2\bin
call "%PY_CHARM_ENV%\pycharm64.exe" %~dp0%
REM for %%t in (".\sln") do "%DEVENV%" %%t
pause