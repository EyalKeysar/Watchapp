@echo off
setlocal

set "source_path=C:\Dev\WatchServer\src\ServerAPI"
set "destination_path=C:\Dev\Watchapp\libs\ServerAPI"

echo Deleting old ServerAPI folder...
rmdir /s /q "%destination_path%"

echo Copying updated ServerAPI folder...
xcopy /s /e /i "%source_path%" "%destination_path%"

echo Update complete.
