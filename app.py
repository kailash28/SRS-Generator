from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('home.html')

@app.route('/student')
def select():
	return render_template('student.html')

@app.route('/hello/', methods=['POST'])
def hello():
    Purpose=request.form['Purpose']
    Scope=request.form['Scope']
    daa=request.form['daa']
    ref=request.form['ref']
    Overview=request.form['Overview']
    pp=request.form['pp']
    sysi=request.form['sysi']
    hi=request.form['hi']
    softi=request.form['softi']
    ci=request.form['ci'] 
    mc=request.form['mc']
    sar=request.form['sar']

    pf=request.form['pf']
    uc=request.form['uc'] 
    cons=request.form['cons']
    aad=request.form['aad']
    aor=request.form['aor']
    ei=request.form['ei'] 
    funcs=request.form['funcs']
    pr=request.form['pr']	
    ldr=request.form['ldr']  
    dc=request.form['dc']  
    ssa=request.form['ssa']  
    rel=request.form['rel']  
    avail=request.form['avail']  
    sec=request.form['sec']  
    main=request.form['main'] 
    port=request.form['port'] 
    otsr=request.form['otsr']
    sm=request.form['sm'] 
    uc1=request.form['uc1'] 
    obj=request.form['obj'] 
    f=request.form['f']
    sti=request.form['sti']
    res=request.form['res']
    ac=request.form['ac']
    cmp1=request.form['cmp1']   
    da=request.form['da']
    si=request.form['si']
    
    return render_template('srs.html', Purpose=Purpose, Scope=Scope
    	,daa=daa,ref=ref,Overview=Overview,pp=pp,sysi=sysi,hi=hi,softi=softi,ci=ci,mc=mc,sar=sar,pf=pf,uc=uc,cons=cons,
    	aad=aad,aor=aor,ei=ei,funcs=funcs,pr=pr,ldr=ldr,dc=dc,ssa=ssa,rel=rel,avail=avail,sec=sec,main=main,port=port,otsr=otsr,sm=sm,uc1=uc1,obj=obj
    	,f=f,sti=sti,res=res,ac=ac,cmp1=cmp1,da=da,si=si)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)



if __name__ == '__main__':
   app.run(debug = True)