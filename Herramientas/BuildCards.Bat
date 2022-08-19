@echo off

color f
wget-1.11.4-1-setup
set path=%path%;C:\Program Files (x86)\GnuWin32\bin
FOR %%a IN (espada copa oro basto) DO (
	mkdir %%a
	FOR /L %%b IN (1,1,12) DO (
		wget -N http://www.consultacartas.com/imagenes/baraja_espanola/%%as_%%b.jpg -O .\%%a\%%b.jpg
        powershell -Command Write-Host "Descargada correctamente" -foreground "Green"		 		
	)
)
