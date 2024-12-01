
function lzero(str="25",len = 2){
	str = string(str)
	for (i = 1; i <= len-string_length(str); i++)
		str = "0"+str
	return str
}