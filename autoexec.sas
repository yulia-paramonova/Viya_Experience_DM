cas mysession sessopts=(caslib=casuser timeout=12000 locale="en_US" metrics=true);

libname casuser cas caslib="casuser";
libname public cas caslib="public";

options casdatalimit=ALL;
