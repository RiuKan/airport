
set /p initi= git init? (Y ot n): 
echo %initi%
if "%initi%" == "Y" git init
if "%initi%" == "Y" set /p remote= remote address? 
if "%initi%" == "Y" git remote add origin %remote%

if "%initi%" == "y" git init
if "%initi%" == "y" set /p remote= remote address? 
if "%initi%" == "y" git remote add origin %remote%
	



git add *
setlocal
set /p message= message: 
git commit -m "%message%"
git push origin master
