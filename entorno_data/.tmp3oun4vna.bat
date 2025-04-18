@ECHO OFF
@SET PYTHONIOENCODING=utf-8
@SET PYTHONUTF8=1
@FOR /F "tokens=2 delims=:." %%A in ('chcp') do for %%B in (%%A) do set "_CONDA_OLD_CHCP=%%B"
@chcp 65001 > NUL
@CALL "C:\Users\marco\miniconda3\condabin\conda.bat" activate "c:\Users\marco\Desktop\Proyecto_Data\entorno_data"
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@c:\Users\marco\Desktop\Proyecto_Data\entorno_data\python.exe -Wi -m compileall -q -l -i C:\Users\marco\AppData\Local\Temp\tmpskgbvien -j 0
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@chcp %_CONDA_OLD_CHCP%>NUL
