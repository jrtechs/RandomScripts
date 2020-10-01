:: Author : Jeffery Russell 11-27-18

@echo off

pushd %~dp0
dir
copy plum.sqlite %LocalAppData%\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite

pause