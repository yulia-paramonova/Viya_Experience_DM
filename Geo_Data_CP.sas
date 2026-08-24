data &_output1;
set &_input1;
	if zip_code<10000
		then CP="0"||compress(put(zip_code,4.));
		else CP=compress(put(zip_code,5.));
	if department_number<10
		then Num_dep="0"||compress(put(department_number,1.));
		else Num_dep=compress(put(department_number,2.));
drop zip_code department_number;
run;
