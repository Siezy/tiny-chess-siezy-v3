import os,sys,json,urllib.request as H
L=os.getenv('MAKEFUN_ENV_URL') or sys.exit()
def R(p,d):
 try:return json.load(H.urlopen(L+p,json.dumps(d).encode()))
 except:sys.exit()
W=(100,320,330,500,900,0);N=5e4;B=[0]*128;S=1;C=0;E=-1;Y=[];J={};Z=[0]*128
P='1111111112222221234444322345543234566543345555434555555444444444'
D8=(-17,-15,15,17,-16,-1,1,16)
def F(f):
 global B,S,C,E
 B=[0]*128;p=0;s=f.split()
 for r in reversed(s[0].split('/')):
  for c in r:
   if c.isdigit():p+=int(c)
   else:i='PNBRQKpnbrqk'.find(c);B[p]=(i%6+1)*(2*(i<6)-1);p+=1
  p=(p//16+1)*16
 S=2*(s[1]>'v')-1
 C=sum(('KQkq'[i]in s[2])<<i for i in range(4))
 E=(int(s[3][1])-1)*16+ord(s[3][0])-97 if s[3]>'-'else-1
def G(cap=False):
 o=[]
 def A(f,t):
  if t//16==7-(S<0)*7:o.extend((f,t,q*S)for q in(5,4,3,2))
  else:o.append((f,t,0))
 for f in range(128):
  if f&8:continue
  x=B[f]
  if not x or x*S<=0:continue
  a=abs(x)
  if a==1:
   d=16*S;t=f+d
   if not B[t] and not cap:
    A(f,t)
    if f//16==1+5*(S<0) and not B[f+2*d]:o.append((f,f+2*d,0))
   for df in(-1,1):
    u=t+df
    if 0<=u<128 and~u&8 and(B[u]*S<0 or u==E):A(f,u)
  elif a<3 or a==6:
   for d in(-31,-33,-14,-18,14,18,31,33) if a==2 else D8:
    t=f+d
    if 0<=t<128 and~t&8 and B[t]*S<(cap==0):o.append((f,t,0))
  else:
   for d in D8[4*(a==4):4+4*(a!=3)]:
    t=f+d
    while 0<=t<128 and~t&8:
     if B[t]:
      if B[t]*S<0:o.append((f,t,0))
      break
     if not cap:o.append((f,t,0))
     t+=d
 if not cap:
  for k,b,j,e in((4,1,7,(5,6)),(4,2,0,(3,2,1)),(116,4,119,(117,118)),(116,8,112,(115,114,113))):
   if C&b and B[j]==4*S and not any(B[s]for s in e)and not X(k,-S)and not X(e[0],-S):o.append((k,e[1],0))
 return o
def X(q,w):
 global S
 o=S;S=w;d=not B[q]
 if d:B[q]=-w
 r=any(t==q for _,t,_ in G(True))
 if d:B[q]=0
 S=o
 return r
D={4:3,0:2,7:1,112:8,116:12,119:4}
def M(f,t,pr):
 global C,E,S
 c=B[t];ep=0
 if B[f]==S and t==E and not c:
  ep=1;c=B[t-16*S];B[t-16*S]=0
 Y.append((f,t,c,pr,C,E,ep))
 B[t]=pr if pr else B[f];B[f]=0
 if abs(B[t])==6 and abs(t-f)==2:
  r=t+1-3*(t<f);s=t-1+2*(t<f);B[r]=0;B[s]=4*S
 E=(f+t)//2 if abs(B[t])==1 and abs(t-f)==32 else -1
 C&=~(D.get(f,0)|D.get(t,0))
 S=-S
def U():
 global C,E,S
 f,t,c,pr,oc,oe,ep=Y.pop()
 S=-S
 if abs(B[t])==6 and abs(t-f)==2:
  r=t-1+2*(t<f);s=t+1-3*(t<f);B[r]=0;B[s]=4*S
 B[f]=B[t] if not pr else S
 B[t]=c*(1-ep)
 if ep:B[t-16*S]=-S
 C,E=oc,oe
def K(w):return B.index(6*w)
def V():
 s=0;n=0;m=0;k=K(1);j=K(-1)
 for f in range(128):
  if f&8:continue
  x=B[f]
  if x:
   a=abs(x);i=f-(f//16)*8;v=W[a-1]+3*int(P[i if x>0 else 63-i])*(a<6)
   if a==3:n+=x>0;m+=x<0
   if a==1 and 14<(f-k if x>0 else j-f)<18:s+=9*(x>0 or-1)
   s+=v if x>0 else -v
 s+=25*((n>1)-(m>1))
 return s*S
T=0
def A(d,a,b,y):
 global T;T+=1
 if T>N:raise StopIteration
 ck=X(K(S),-S)
 if d>0:
  if ck:d+=1
  k=(tuple(B),S,C,E);e=J.get(k)
  if e and e[0]>=d and(e[2]<2 and(e[2]==0 or e[1]>=b)or e[2]==2 and e[1]<=a):return e[1]
  m=G();bm=e and e[3]
 else:
  s=V()
  if not ck:
   if s>=b:return b
   a=max(a,s)
  m=G() if ck else G(1);bm=None
 m.sort(key=lambda x:(x==bm,Z[y&127]==(x[0],x[1]),W[abs(B[x[1]])-1]),reverse=1)
 bb=None;n=0
 for f,t,pr in m:
  if d<=0 and a>W[abs(B[t])-1]+s:continue
  M(f,t,pr)
  if X(K(-S),S):U();continue
  n+=1
  v=-A(d-1,-b,-a,y+1)
  U()
  if v>=b:
   if d>0:Z[y&127]=(f,t);J[k]=(d,b,1,(f,t,pr))
   return b
  if v>a:a=v;bb=(f,t,pr)
 if n==0 and(d>0 or ck):return ck*(y-9999)
 if d>0:J[k]=(d,a,2*(not bb),bb)
 return a
u=lambda s:chr(97+s%16)+chr(49+s//16)
def main():
 global T
 while 1:
  g=R('/game',{})
  if g['status']=='done':break
  F(g['fen']);bs=None;T=0
  if len(J)>2e4:J.clear()
  for dp in range(1,30):
   try:
    bb=None;bv=-9e9
    for f,t,pr in G():
     M(f,t,pr)
     if X(K(-S),S):
      U();continue
     if not bs:bs=(f,t,pr)
     try:v=-A(dp-1,-9e9,9e9,1)
     except StopIteration:F(g['fen']);break
     U()
     if v>bv:bv=v;bb=(f,t,pr)
    else:
     if bb:bs=bb
   except StopIteration:break
  if not bs:bs=G()[0]
  f,t,pr=bs
  R('/move',{'game':g['game'],'move':u(f)+u(t)+(pr and'nbrq'[abs(pr)-2]or'')})
if'__main__'==__name__:main()
