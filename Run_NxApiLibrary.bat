set UGII_ENV_FILE=%UGII_BASE_DIR%\ugii_env.dat
set PYTHONPATH=%UGII_BASEDIR%\NXBIN\python;C:\Python\Python36;C:\Python\Python36\Lib;C:\Python\Python36;C:\Python\Python36\Lib\site-packages
set path=%UGII_BASE_DIR%\NXBIN;%UGII_BASE_DIR%\UGII;%UGII_BASE_DIR%\UGOPEN;%path%
set DEVENV=C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe
"%DEVENV%" "NxLibrary.sln"
REM for %%t in (".\sln") do "%DEVENV%" %%t
pause