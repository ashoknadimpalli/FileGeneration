
flatfile_input=open('C://Users//vnadimpalli//Desktop//BCBSMI//NetworkHealth837.csv','r')
read_flatfile=flatfile_input.readlines()

def ifnull(var, val):
  if (var is None or var=='NULL' or var==''):
    return val
  return var

file=[]
for i in range(1,len(read_flatfile)):
    if(i==1):
        bp_hl='HL*'+str(i)+'**20*1~'
        file.append(bp_hl+'\n')
    else:
        bp_hl='HL*'+str(i+1)+'**20*1~'
        file.append(bp_hl+'\n')

    prv='PRV*BI*PXC*'+read_flatfile[i].split(',')[5].strip()+'~'
    file.append(prv+'\n')
    if(read_flatfile[i].split(',')[2].strip()=='NULL'):
        bp_nm1='NM1*85*2*'+read_flatfile[i].split(',')[1].strip()+'*****XX*'+str(read_flatfile[i].split(',')[0].strip())+'~'
        file.append(bp_nm1+'\n')
    elif(read_flatfile[i].split(',')[2].strip()!='NULL' and read_flatfile[i].split(',')[3].strip()=='NULL' ):
        bp_nm1='NM1*85*2*'+read_flatfile[i].split(',')[1].strip()+'*'+read_flatfile[i].split(',')[2].strip()+'****XX*'+str(read_flatfile[i].split(',')[0].strip())+'~'
        file.append(bp_nm1+'\n')
    elif(read_flatfile[i].split(',')[2].strip()!='NULL' and read_flatfile[i].split(',')[3].strip()!='NULL'):
        bp_nm1='NM1*85*2*'+read_flatfile[i].split(',')[1].strip()+'*'+read_flatfile[i].split(',')[2].strip()+'*'+read_flatfile[i].split(',')[3].strip()+'***XX*'+str(read_flatfile[i].split(',')[0].strip())+'~'
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
    sb_hl='HL*'+str(i+1)+'*'+str(i)+'*22*0~'
    file.append(sb_hl+'\n')
    sbr='SBR*S*18********MB~'
    file.append(sbr+'\n')
    if(read_flatfile[i].split(',')[14].strip()=='NULL' and read_flatfile[i].split(',')[13].strip()=='NULL'):
        sbr_nm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+'*'+'*'+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
        file.append(sbr_nm1+'\n')
    elif(read_flatfile[i].split(',')[14].strip()!='NULL' and read_flatfile[i].split(',')[13].strip()=='NULL'):
        sbr_nm1='NM1*IL*1*'+read_flatfile[i].split(',')[12].strip()+read_flatfile[i].split(',')[14].strip()+'*'+'*'+'**MI*'+read_flatfile[i].split(',')[11].strip()+'~'
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
    clm=('CLM*'+read_flatfile[i].split(',')[23].strip()+'*'+read_flatfile[i].split(',')[24].strip()+'***'+read_flatfile[i].split(',')[25].strip()+':'+'B'+':'+read_flatfile[i].split(',')[26].strip()+'*'+
        'N'+'*'+'C'+'*'+'W'+'*'+'I'+'~')
    file.append(clm+'\n')
    if(read_flatfile[i].split(',')[36].strip()!=''):
        med='REF*EA'+read_flatfile[i].split(',')[36].strip()+'~'
        file.append(med+'\n')
    hi_diag='HI*ABK:'+read_flatfile[i].split(',')[38].strip()+ifnull(read_flatfile[i].split(',')[39].strip(),ifnull(read_flatfile[i].split(',')[40].strip(),ifnull(read_flatfile[i].split(',')[41].strip(),ifnull(read_flatfile[i].split(',')[42].strip(),'~'))))
    file.append(hi_diag+'\n')
    if(read_flatfile[i].split(',')[52].strip()=='NULL'):
        re_nm1='NM1*82*1*'+read_flatfile[i].split(',')[51].strip()+'*****XX*'+str(read_flatfile[i].split(',')[50].strip())+'~'
        file.append(re_nm1+'\n')
    elif(read_flatfile[i].split(',')[52].strip()!='NULL' and read_flatfile[i].split(',')[53].strip()=='NULL' ):
        re_nm1='NM1*82*1*'+read_flatfile[i].split(',')[51].strip()+'*'+read_flatfile[i].split(',')[52].strip()+'****XX*'+str(read_flatfile[i].split(',')[50].strip())+'~'
        file.append(re_nm1+'\n')
    elif(read_flatfile[i].split(',')[2].strip()!='NULL' and read_flatfile[i].split(',')[3].strip()!='NULL'):
        re_nm1='NM1*82*1*'+read_flatfile[i].split(',')[51].strip()+'*'+read_flatfile[i].split(',')[52].strip()+'*'+read_flatfile[i].split(',')[53].strip()+'***XX*'+str(read_flatfile[i].split(',')[0].strip())+'~'
        file.append(re_nm1+'\n')
file_concatenate=''.join(file)
print(file_concatenate)







