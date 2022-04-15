$curr_path = Get-Location
$app_path = Split-Path -Parent ${PSScriptRoot}

Set-Location $app_path

Remove-Item -Path build -Recurse -ErrorAction Ignore
Remove-Item -Path dist -Recurse -ErrorAction Ignore
Remove-Item -Path st1_voluptuous_json.egg-info -Recurse -ErrorAction Ignore

Set-Location $curr_path

