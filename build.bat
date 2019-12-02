
@RD /S /Q "build"
@RD /S /Q "dist"

pyinstaller __main__.spec

xcopy ExploranceAnonymizer.bat dist
xcopy README.md dist