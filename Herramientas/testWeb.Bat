@echo off
color a
ping www.consultacartas.com
if %errorlevel%==0 (
cls
echo La web esta activa 
)else (
cls
color 4
echo La web no esta activa, o no tienes conexion a internet
)
pause