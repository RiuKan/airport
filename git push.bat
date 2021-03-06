
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

git commit -m "/p 입력하세요"
git push origin master
