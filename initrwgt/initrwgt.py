
pdf=11000
numMembers=53
unc_scale=True
unc_pdf=True

s = ""
s += f"<initrwgt>\n"
s += f"<weightgroup name='nominal' combine='None'>\n"
s += f"<weight id='MUR1.0_MUF1.0_PDF{pdf}'>default</weight>\n"
s += f"</weightgroup>\n"
if unc_scale:
    s += f"<weightgroup name='scale_variations' combine='None'>\n"
    s += f"<weight id='MUR2.0_MUF2.0_PDF{pdf}'> renscfact=2d0 facscfact=2d0 </weight>\n"
    s += f"<weight id='MUR0.5_MUF0.5_PDF{pdf}'> renscfact=0.5d0 facscfact=0.5d0 </weight>\n"
    s += f"<weight id='MUR1.0_MUF2.0_PDF{pdf}'> renscfact=1d0 facscfact=2d0 </weight>\n"
    s += f"<weight id='MUR1.0_MUF0.5_PDF{pdf}'> renscfact=1d0 facscfact=0.5d0 </weight>\n"
    s += f"<weight id='MUR2.0_MUF1.0_PDF{pdf}'> renscfact=2d0 facscfact=1d0 </weight>\n"
    s += f"<weight id='MUR0.5_MUF1.0_PDF{pdf}'> renscfact=0.5d0 facscfact=1d0 </weight>\n"
    s += f"</weightgroup>"
if unc_pdf:
    s += f"<weightgroup name='pdf_variations' combine='None'>\n"
    for i in range(1,numMembers):
        s += f"<weight id='MUR1.0_MUF1.0_PDF{pdf+i}'> lhapdf={pdf+i}</weight>\n"
    s += f"</weightgroup>\n"
s += f"</initrwgt>\n"

print(s)