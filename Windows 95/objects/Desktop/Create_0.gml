Props = [audio,bluetooth]
Icons = []
Win = "|"
Tasks = []

lclick = 0
for (r = 0; r < 10; r++)
{
	//   0     1      2        3      4
	// [Icon, Name, isopen, [Pages], page]
	for (c = 0; c < 15; c++)
		Icons[r][c] = [NaN,"", false, [], 0]
}
		
function addIcon(Row,Col ,Icon, Name, Pages = [])
{
	Icons[Row][Col][0] = Icon
	Icons[Row][Col][1] = Name
	Icons[Row][Col][3] = Pages
}

function CreateButton(xs,ys,char,fun)
{
	draw_rectangle_color(xs,ys,xs+15,ys,#ffffff,#ffffff,#ffffff,#ffffff,false)
	draw_rectangle_color(xs,ys,xs,ys+13,#ffffff,#ffffff,#ffffff,#ffffff,false)
	draw_rectangle_color(xs+16,ys,xs+16,ys+13,#000000,#000000,#000000,#000000,false)
	draw_rectangle_color(xs,ys+14,xs+16,ys+14,#000000,#000000,#000000,#000000,false)
	draw_rectangle_color(xs+1,ys+1,xs+15,ys+13,#C0C0C0,#C0C0C0,#C0C0C0,#C0C0C0,false)
	
	RenderLeter(char,xs+8,ys+3,7,8,["Center","Top"],#000000)
	
	if mouse_x >= xs and mouse_x <= xs+16 and mouse_y >= ys and mouse_y <= ys+14 and lclick
		fun()
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


addIcon(0,6 ,nine4,"1994.html",[p1_94,p2_94,p3_94])
addIcon(0,7 ,questio,"WHAT.html",[p1_what,p2_what,p3_what,p4_what])
addIcon(0,8 ,Time,"Time.html",[p1_time,p2_time,p3_time,p4_time,p5_time,p6_time])