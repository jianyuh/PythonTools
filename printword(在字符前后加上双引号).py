import re
s='''
const
int
char
var
array
of
integer
procedure
funcion
if
then
case
for
to
downto
do
begin
end
read
write
(
)
[
]
,
;
+
-
*
/
<
<=
>
>=
=
<>
:=
:
.
'
"'''
abc = re.split('\n',s)
for i in abc:
	i='"'+i+'"'+","
	print i,
	
