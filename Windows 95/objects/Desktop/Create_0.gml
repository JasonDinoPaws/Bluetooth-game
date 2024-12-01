Props = [audio,bluetooth]
Icons = []
Win = "|"
Tasks = []

for (r = 0; r < 10; r++)
{
	//   0     1      2        3      4       5      6
	// [Icon, Name, isopen, winfoc, [x,y], [Pages], page]
	for (c = 0; c < 15; c++)
		Icons[r][c] = [NaN,"", false, false,[100,75], [], 0]
}
		
function addIcon(Row,Col ,Icon, Name, Pages = [])
{
	Icons[Row][Col][0] = Icon
	Icons[Row][Col][1] = Name
	Icons[Row][Col][5] = Pages
}

addIcon(0,0 ,MyComp, "My\\nComputer", [MyComp])
addIcon(1,0 ,Network, "Network\\nNeighborhood", [Network])


addIcon(4,7 ,_m,"M.png",[_m])
addIcon(4,8 ,_y,"M.png",[_y])

addIcon(5,2 ,_p,"P.png",[_p])
addIcon(5,3 ,_r,"R.png",[_r])
addIcon(5,4 ,_e,"E.png",[_e])
addIcon(5,5 ,_s,"S.png",[_s])
addIcon(5,6 ,_e,"E2.png",[_e])
addIcon(5,7 ,_n,"N.png",[_n])
addIcon(5,8 ,_t,"T.png",[_t])
addIcon(5,9 ,_a,"A.png",[_a])
addIcon(5,10 ,_t,"T2.png",[_t])
addIcon(5,11 ,_i,"I.png",[_i])
addIcon(5,12 ,_o,"O.png",[_o])
addIcon(5,13 ,_n,"N2.png",[_n])



//Icons[0][7] = [nine4,"1994.html"]