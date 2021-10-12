dim fso,fle,fles,fld ,MyDateStr,MyDate
Set fso = CreateObject("Scripting.FileSystemObject") 
set fld = fso.getfolder(".") 
sub rename(fles) 
num=0 
for each fle in fles 
ext=fso.GetExtensionName(fle) 
ext=lcase(ext) 

if fso.FileExists("New.bkf")  then 

MydateStr=split(date,"-")

Mydate=MydateStr(0)&"-"&MydateStr(1)&"-"&MydateStr(2)

fle.name=Mydate&"."&ext 
end if 
next 
end sub 
rename fld.files 
