Sx = room_width-1
Sy = room_height

// Desktop
lclick = mouse_check_button(1)
for (r = 0; r < array_length(Icons); r ++)
	RenderGrid(Icons[r],5,Sx-5,5+(50*r)+(5*r),-1,[50,50],[2.75,0],function(obj,ix, x1,y1,x2,y2){
		if obj[1] == "" { return }
		Cx = (x1+x2)/2
		Cy = (y1+y2)/2
		isover = mouse_x >= x1 and mouse_x <= x2 and mouse_y >= y1 and mouse_y <= y2
		
		if isover{
			draw_set_alpha(.25)
			draw_rectangle(x1,y1,x2,y2,false)
			draw_set_alpha(1)
			
			if lclick {
				if !Icons[r][ix][2] 
					array_push(Tasks,string(r)+"|"+string(ix))
				Icons[r][ix][2] = true
				Icons[r][ix][3] = true
				if array_length(Win) > 1
				{
					splt = string_split(Win,"|")
					Icons[int64(splt[0])][int64(splt[1])][3] = false
				}
				Win = string(r)+"|"+string(ix)
				
			}
		}
		
			
		draw_sprite(obj[0],0,Cx-(sprite_get_width(obj[0])/2),Cy-sprite_get_height(obj[0]))
		RenderText(obj[1],Cx,Cy+5,4,4,["Center","Top"],#ffffff)
	},"Left")


// Windows
if string_length(Win) > 1
{
	splt = string_split(Win,"|")
	Icon = Icons[int64(splt[0])][int64(splt[1])]
	X = Icon[4][0] 
	Y = Icon[4][1]
	
	draw_sprite(Outline,0,X,Y)
	draw_sprite_ext(Icon[0],0,X+16,Y+10,13/sprite_get_width(Icon[0]),13/sprite_get_height(Icon[0]),0,#ffffff,1)
	RenderText(string_replace(Icon[1],"\\n"," "),X+45,Y+11,10,10,["Left","Top"],#ffffff) 
	draw_sprite(Icon[5][Icon[6]],-1,X+15,Y+42)
	

	if mouse_x >= X and mouse_x <= X+600 and mouse_y >= Y and mouse_y <= Y+41 and lclick
		Icons[int64(splt[0])][int64(splt[1])][4] = [mouse_x-300,mouse_y-20]
}

// Task bar
draw_rectangle_color(0,Sy-22,Sx,Sy,#C0C0C0,#C0C0C0,#C0C0C0,#C0C0C0,false)

//Tasks
Tx = 1+sprite_get_width(Start)+2
draw_sprite(Start,0,1,Sy-1)



//Props
text = RenderText(lzero(current_hour)+":"+lzero(current_minute),Sx-11,Sy-15,10,10,["Right","Top"],#000000)

draw_rectangle_color(Sx-3,Sy-20,Sx-2,Sy-2,#ffffff,#ffffff,#ffffff,#ffffff,false)
draw_rectangle_color(text[0]-7,Sy-20,Sx-4,Sy-19,#000000,#000000,#000000,#000000,false)
draw_rectangle_color(text[0]-7,Sy-3,Sx-4,Sy-2,#ffffff,#ffffff,#ffffff,#ffffff,false)

prop = RenderGrid(Props,0,text[0]-15-7,Sy-18,3,[15,15],[0,0],function(obj,ix, x1,y1,x2,y2){
	draw_sprite(obj,0,x1,y1)
	draw_rectangle_color(x1,Sy-20,x2,Sy-19,#000000,#000000,#000000,#000000,false)
	draw_rectangle_color(x1,Sy-3,x2,Sy-2,#ffffff,#ffffff,#ffffff,#ffffff,false)
},"Right")

draw_rectangle_color(prop[0]-1,Sy-20,prop[0],Sy-3,#000000,#000000,#000000,#000000,false)
draw_rectangle_color(-250,0,0,Sy,#000000,#000000,#000000,#000000,false)
draw_rectangle_color(Sx,0,Sx+250,Sy,#000000,#000000,#000000,#000000,false)