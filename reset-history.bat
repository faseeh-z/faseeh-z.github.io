@echo off
set "folder=.git"

echo This would permanently delete the "%folder%" folder. Do you want to continue? (Y/N)
choice /c YN /n
if errorlevel 2 (
    echo Deletion cancelled.
    exit /b
)

rmdir /s /q "%folder%"
echo Removed "%folder%".
git init
git remote add origin https://github.com/faseeh-official/faseeh-official.github.io.git
git add -A
git commit -m "Initial Commit"
git push --force -u origin main

echo .
echo .
echo .
echo Finished history reset.
pause
