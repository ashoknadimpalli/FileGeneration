
flatfile_input=open('C://Users//vnadimpalli//Desktop//BCBSMI//NetworkHealth837I.csv','r')
read_flatfile=flatfile_input.readlines()

def ifnull(var, val):
  if (var is None or var=='NULL' or var==''):
    return val
  return var

def diagnull(var, val):
  if (var is None or var=='NULL' or var==''):
    return val
  return '*ABF:'+var


def padiagnull(var, val):
  if (var is None or var=='NULL' or var==''):
    return val
  return '*APR:'+var

file=[]
j=1
for i in range(1,len(read_flatfile)):


    bp_hl='HL*'+str(j)+'**20*1~'
    j=j+1
    file.append(bp_hl+'\n')


    prv='PRV*BI*PXC*'+read_flatfile[i].split(',')[5].strip()+'~'
    file.append(prv+'\n')

    if(read_flatfile[i].split(',')[2].strip()=='NULL'):
        bp_nm1='NM1*85*2*'+read_flatfile[i].split(',')[1].strip()+'*****XX*'+str(read_flatfile[i].split(',')[0].strip())+'~'
        file.append(bp_nm1+'\n')
    elif(read_flatfile[i].split(',')[2].strip()!='NULL' and read_flatfile[i].split(',')[3].strip()=='NULL' ):
        bp_nm1='NM1*85*1*'+read_flatfile[i].split(',')[1].strip()+'*'+read_flatfile[i].split(',')[2].strip()+'****XX*'+str(read_flatfile[i].split(',')[0].strip())+'~'
        file.append(bp_nm1+'\n')
    elif(read_flatfile[i].split(',')[2].strip()!='NULL' and read_flatfile[i].split(',')[3].strip()!='NULL'):
        bp_nm1='NM1*85*1*'+read_flatfile[i].split(',')[1].strip()+'*'+read_flatfile[i].split(',')[2].strip()+'*'+read_flatfile[i].split(',')[3].strip()+'***XX*'+str(read_flatfile[i].split(',')[0].strip())+'~'
        file.append(bp_nm1+'\n')

    if(read_flatfile[i].split(',')[7].strip()=='NULL'):
        bp_n3='N3*'+read_flatfile[i].split(',')[6].strip()+'~'
        file.append(bp_n3+'\n')
    elif(read_flatfile[i].split(',')[7].strip()!='NULL'):
        bp_n3='N3*'+read_flatfile[i].split(',')[6].strip()+'*'+read_flatfile[i].split(',')[7].strip()+'~'
        file.append(bp_n3+'\n')

    bp_n4='N4*'+read_flatfile[i].split(',')[8].strip()+'*'+read_flatfile[i].split(',')[9].strip()+'*'+read_flatfile[i].split(',')[10].strip()+'~'
    file.append(bp_n4+'\n')

    bp_tax='REF*EI*'+read_flatfile[i].split(',')[4].strip()+'~'
    file.append(bp_tax+'\n')

    sb_hl='HL*'+str(j)+'*'+str(j-1)+'*22*0~'
    j=j+1
    file.append(sb_hl+'\n')

    sbr='SBR*S*18*******MB~'
    file.append(sbr+'\n')

    if(read_flatfile[i].split(',')[14].strip()=='NULL' and read_flatfile[i].split(',')[13].strip()=='NULL'):
        sbr_nm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+'*'+'*'+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
        file.append(sbr_nm1+'\n')
    elif(read_flatfile[i].split(',')[14].strip()!='NULL' and read_flatfile[i].split(',')[13].strip()=="NULL"):
        sbr_nm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+'*'+read_flatfile[i].split(',')[14].strip()+'*'+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
        file.append(sbr_nm1+'\n')
    elif(read_flatfile[i].split(',')[14].strip()=='NULL' and read_flatfile[i].split(',')[13].strip()!='NULL'):
        sbr_nm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+'*'+read_flatfile[i].split(',')[13].strip()+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
        file.append(sbr_nm1+'\n')
    else:
        sbr_nm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+'*'+read_flatfile[i].split(',')[14].strip()+'*'+read_flatfile[i].split(',')[13].strip()+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
        file.append(sbr_nm1+'\n')

    if(read_flatfile[i].split(',')[16].strip()=='NULL'):
        sbr_n3='N3*'+read_flatfile[i].split(',')[15].strip()+'~'
        file.append(sbr_n3+'\n')
    else:
        sbr_n3='N3*'+read_flatfile[i].split(',')[15].strip()+'*'+read_flatfile[i].split(',')[16].strip()+'~'
        file.append(sbr_n3+'\n')

    sbr_n4='N4*'+read_flatfile[i].split(',')[17].strip()+'*'+read_flatfile[i].split(',')[18].strip()+'*'+read_flatfile[i].split(',')[19].strip()+'~'
    file.append(sbr_n4+'\n')

    sbr_dmg='DMG*D8*'+read_flatfile[i].split(',')[21].strip()+'*'+read_flatfile[i].split(',')[20]+'~'
    file.append(sbr_dmg+'\n')

    payer_nm1='NM1*PR*2*EDSCMS*****PI*80882~'
    file.append(payer_nm1+'\n')

    payer_n3='N3*7500 Security Blvd~'
    file.append(payer_n3+'\n')

    payer_n4='N4*Baltimore*MD*212441850~'
    file.append(payer_n4+'\n')

    payer_ref='REF*2U*'+read_flatfile[i].split(',')[22].strip()+'~'
    file.append(payer_ref+'\n')

    clm=('CLM*'+read_flatfile[i].split(',')[23].strip()+'*'+read_flatfile[i].split(',')[24].strip()+'***'+read_flatfile[i].split(',')[80].strip()+':'+'A'+':'+read_flatfile[i].split(',')[81].strip()+'*'+
        '*'+'C'+'*'+'W'+'*'+'I'+'~')
    file.append(clm+'\n')

    statement_date='DTP*434*RD8*'+read_flatfile[i].split(',')[82].strip()+'-'+read_flatfile[i].split(',')[83].strip()+'~'
    file.append(statement_date+'\n')

    admission_date='DTP*435*D8*'+read_flatfile[i].split(',')[82].strip()+'~'
    file.append(admission_date+'\n')

    cl='CL*'+str(read_flatfile[i].split(',')[84].strip())+'*'+str(read_flatfile[i].split(',')[85].strip())+'*'+str(read_flatfile[i].split(',')[86].strip())+'~'
    file.append(cl+'\n')

    if(read_flatfile[i].split(',')[36].strip()!=''):
        med='REF*EA*'+read_flatfile[i].split(',')[36].strip()+'~'
        file.append(med+'\n')

    hi_diag='HI*ABK:'+read_flatfile[i].split(',')[38].strip()+'~'
    file.append(hi_diag+'\n')

    if(read_flatfile[i].split(',')[87].strip()!=''):
        if(read_flatfile[i].split(',')[88].strip()==''):
            patient_reason='HI*APR:'+read_flatfile[i].split(',')[87].strip()+'~'
            file.append(patient_reason+'\n')
        else:
            patient_reason='HI*APR:'+read_flatfile[i].split(',')[87].strip()+padiagnull(read_flatfile[i].split(',')[89].strip(),padiagnull(read_flatfile[i].split(',')[88].strip(),'~'))+'~'
            file.append(patient_reason+'\n')

    if(read_flatfile[i].split(',')[40].strip()==''):
        other_diag='HI*ABF:'+read_flatfile[i].split(',')[39].strip()+'~'
        file.append(other_diag+'\n')
    else:
        other_diag='HI*ABF:'+read_flatfile[i].split(',')[39].strip()+(
        diagnull(read_flatfile[i].split(',')[46].strip(),diagnull(read_flatfile[i].split(',')[45].strip(),diagnull(read_flatfile[i].split(',')[44].strip(),
        diagnull(read_flatfile[i].split(',')[43].strip(),diagnull(read_flatfile[i].split(',')[42].strip(),diagnull(read_flatfile[i].split(',')[41].strip(),
        diagnull(read_flatfile[i].split(',')[40].strip(),'~')))))))+'~')
        file.append(other_diag+'\n')





    # else:
    #     hi_diag='HI*ABK:'+read_flatfile[i].split(',')[38].strip()+diagnull(read_flatfile[i].split(',')[42].strip(),diagnull(read_flatfile[i].split(',')[41].strip(),diagnull(read_flatfile[i].split(',')[40].strip(),diagnull(read_flatfile[i].split(',')[39].strip(),'~'))))+'~'
    #     file.append(hi_diag+'\n')

    if(read_flatfile[i].split(',')[52].strip()=='NULL'):
        re_nm1='NM1*82*1*'+read_flatfile[i].split(',')[51].strip()+'*****XX*'+str(read_flatfile[i].split(',')[50].strip())+'~'
        file.append(re_nm1+'\n')
    elif(read_flatfile[i].split(',')[52].strip()!='NULL' and read_flatfile[i].split(',')[53].strip()=='NULL' ):
        re_nm1='NM1*82*1*'+read_flatfile[i].split(',')[51].strip()+'*'+read_flatfile[i].split(',')[52].strip()+'****XX*'+str(read_flatfile[i].split(',')[50].strip())+'~'
        file.append(re_nm1+'\n')
    elif(read_flatfile[i].split(',')[2].strip()!='NULL' and read_flatfile[i].split(',')[3].strip()!='NULL'):
        re_nm1='NM1*82*1*'+read_flatfile[i].split(',')[51].strip()+'*'+read_flatfile[i].split(',')[52].strip()+'*'+read_flatfile[i].split(',')[53].strip()+'***XX*'+str(read_flatfile[i].split(',')[0].strip())+'~'
        file.append(re_nm1+'\n')

    sbr_other='SBR*P*18*******16~'
    file.append(sbr_other+'\n')

    sbr_payerpaid='AMT*D*'+str(read_flatfile[i].split(',')[54].strip())+'~'
    file.append(sbr_payerpaid+'\n')

    sbr_oi='OI***W***I~'
    file.append(sbr_oi+'\n')

    if(read_flatfile[i].split(',')[14].strip()=='NULL' and read_flatfile[i].split(',')[13].strip()=='NULL'):
        sbr_onm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+'*'+'*'+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
        file.append(sbr_onm1+'\n')
    elif(read_flatfile[i].split(',')[14].strip()!='NULL' and read_flatfile[i].split(',')[13].strip()=='NULL'):
        sbr_onm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+'*'+read_flatfile[i].split(',')[14].strip()+'*'+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
        file.append(sbr_onm1+'\n')
    elif(read_flatfile[i].split(',')[14].strip()=='NULL' and read_flatfile[i].split(',')[13].strip()!='NULL'):
        sbr_onm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+'*'+read_flatfile[i].split(',')[13].strip()+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
        file.append(sbr_onm1+'\n')
    else:
        sbr_onm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+'*'+read_flatfile[i].split(',')[14].strip()+'*'+read_flatfile[i].split(',')[13].strip()+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
        file.append(sbr_onm1+'\n')

    if(read_flatfile[i].split(',')[16].strip()=='NULL'):
        sbr_on3='N3*'+read_flatfile[i].split(',')[15].strip()+'~'
        file.append(sbr_on3+'\n')
    else:
        sbr_on3='N3*'+read_flatfile[i].split(',')[15].strip()+'*'+read_flatfile[i].split(',')[16].strip()+'~'
        file.append(sbr_on3+'\n')

    sbr_on4='N4*'+read_flatfile[i].split(',')[17].strip()+'*'+read_flatfile[i].split(',')[18].strip()+'*'+read_flatfile[i].split(',')[19].strip()+'~'
    file.append(sbr_on4+'\n')

    oth_payer='NM1*PR*2*Network Health*****XV*'+read_flatfile[i].split(',')[22].strip()+'~'
    file.append(oth_payer+'\n')

    lx='LX*'+str(read_flatfile[i].split(',')[55].strip())+'~'
    file.append(lx+'\n')

    if(read_flatfile[i].split(',')[57].strip()=='' and read_flatfile[i].split(',')[58].strip()=='' and read_flatfile[i].split(',')[59].strip()=='' and read_flatfile[i].split(',')[60].strip()==''):
        sv1='SV1*HC:'+str(read_flatfile[i].split(',')[56].strip())+'*'+read_flatfile[i].split(',')[24].strip()+'*UN*'+str(read_flatfile[i].split(',')[63].strip())+'***1~'
    elif(read_flatfile[i].split(',')[57].strip()!='' and read_flatfile[i].split(',')[58].strip()=='' and read_flatfile[i].split(',')[59].strip()=='' and read_flatfile[i].split(',')[60].strip()==''):
        sv1='SV1*HC:'+str(read_flatfile[i].split(',')[56].strip())+':'+read_flatfile[i].split(',')[57].strip()+'*'+read_flatfile[i].split(',')[24].strip()+'*UN*'+str(read_flatfile[i].split(',')[63].strip())+'***1~'
    elif(read_flatfile[i].split(',')[57].strip()!='' and read_flatfile[i].split(',')[58].strip()!='' and read_flatfile[i].split(',')[59].strip()=='' and read_flatfile[i].split(',')[60].strip()==''):
        sv1='SV1*HC:'+str(read_flatfile[i].split(',')[56].strip())+':'+read_flatfile[i].split(',')[57].strip()+':'+read_flatfile[i].split(',')[58].strip()+'*'+read_flatfile[i].split(',')[24].strip()+'*UN*'+str(read_flatfile[i].split(',')[63].strip())+'***1~'
    elif(read_flatfile[i].split(',')[57].strip()!='' and read_flatfile[i].split(',')[58].strip()!='' and read_flatfile[i].split(',')[59].strip()!='' and read_flatfile[i].split(',')[60].strip()==''):
        sv1='SV1*HC:'+str(read_flatfile[i].split(',')[56].strip())+':'+read_flatfile[i].split(',')[57].strip()+':'+read_flatfile[i].split(',')[58].strip()+':'+read_flatfile[i].split(',')[59].strip()+'*'+read_flatfile[i].split(',')[24].strip()+'*UN*'+str(read_flatfile[i].split(',')[63].strip())+'***1~'
    elif(read_flatfile[i].split(',')[57].strip()!='' and read_flatfile[i].split(',')[58].strip()!='' and read_flatfile[i].split(',')[59].strip()!='' and read_flatfile[i].split(',')[60].strip()!=''):
        sv1='SV1*HC:'+str(read_flatfile[i].split(',')[56].strip())+':'+read_flatfile[i].split(',')[57].strip()+':'+read_flatfile[i].split(',')[58].strip()+':'+read_flatfile[i].split(',')[59].strip()+':'+read_flatfile[i].split(',')[60].strip()+'*'+read_flatfile[i].split(',')[24].strip()+'*UN*'+str(read_flatfile[i].split(',')[63].strip())+'***1~'
    file.append(sv1+'\n')

    srvc_date='DTP*472*RD8*'+read_flatfile[i].split(',')[68].strip()+'-'+read_flatfile[i].split(',')[69].strip()+'~'
    file.append(srvc_date+'\n')

    if(read_flatfile[i].split(',')[57].strip()=='' and read_flatfile[i].split(',')[58].strip()=='' and read_flatfile[i].split(',')[59].strip()=='' and read_flatfile[i].split(',')[60].strip()==''):
        svd='SVD*'+read_flatfile[i].split(',')[22].strip()+'*'+read_flatfile[i].split(',')[74].strip()+'*HC:'+str(read_flatfile[i].split(',')[56].strip())+'**'+str(read_flatfile[i].split(',')[63].strip())+'~'
    elif(read_flatfile[i].split(',')[57].strip()!='' and read_flatfile[i].split(',')[58].strip()=='' and read_flatfile[i].split(',')[59].strip()=='' and read_flatfile[i].split(',')[60].strip()==''):
        svd='SVD*'+read_flatfile[i].split(',')[22].strip()+'*'+read_flatfile[i].split(',')[74].strip()+'*HC:'+str(read_flatfile[i].split(',')[56].strip())+':'+read_flatfile[i].split(',')[57].strip()+'**'+str(read_flatfile[i].split(',')[63].strip())+'~'
    elif(read_flatfile[i].split(',')[57].strip()!='' and read_flatfile[i].split(',')[58].strip()!='' and read_flatfile[i].split(',')[59].strip()=='' and read_flatfile[i].split(',')[60].strip()==''):
        svd='SVD*'+read_flatfile[i].split(',')[22].strip()+'*'+read_flatfile[i].split(',')[74].strip()+'*HC:'+str(read_flatfile[i].split(',')[56].strip())+':'+read_flatfile[i].split(',')[57].strip()+':'+read_flatfile[i].split(',')[58].strip()+'**'+str(read_flatfile[i].split(',')[63].strip())+'~'
    elif(read_flatfile[i].split(',')[57].strip()!='' and read_flatfile[i].split(',')[58].strip()!='' and read_flatfile[i].split(',')[59].strip()!='' and read_flatfile[i].split(',')[60].strip()==''):
        svd='SVD*'+read_flatfile[i].split(',')[22].strip()+'*'+read_flatfile[i].split(',')[74].strip()+'*HC:'+str(read_flatfile[i].split(',')[56].strip())+':'+read_flatfile[i].split(',')[57].strip()+':'+read_flatfile[i].split(',')[58].strip()+':'+read_flatfile[i].split(',')[59].strip()+'**'+str(read_flatfile[i].split(',')[63].strip())+'~'
    elif(read_flatfile[i].split(',')[57].strip()!='' and read_flatfile[i].split(',')[58].strip()!='' and read_flatfile[i].split(',')[59].strip()!='' and read_flatfile[i].split(',')[60].strip()!=''):
        svd='SVD*'+read_flatfile[i].split(',')[22].strip()+'*'+read_flatfile[i].split(',')[74].strip()+'*HC:'+str(read_flatfile[i].split(',')[56].strip())+':'+read_flatfile[i].split(',')[57].strip()+':'+read_flatfile[i].split(',')[58].strip()+':'+read_flatfile[i].split(',')[59].strip()+':'+read_flatfile[i].split(',')[60].strip()+'**'+str(read_flatfile[i].split(',')[63].strip())+'~'
    file.append(svd+'\n')

    cas='CAS*CO*45*'+str(round(float(read_flatfile[i].split(',')[61].strip())-float(read_flatfile[i].split(',')[74].strip())-float(read_flatfile[i].split(',')[79].strip()),2))+'~'
    file.append(cas+'\n')

    paid_date='DTP*573*D8*'+read_flatfile[i].split(',')[78].strip()+'~'
    file.append(paid_date+'\n')

    patient_liab='AMT*EAF*'+str(read_flatfile[i].split(',')[79].strip())+'~'
    file.append(patient_liab+'\n')


file_concatenate=''.join(file)
print(file_concatenate)







