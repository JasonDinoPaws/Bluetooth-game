Sx = room_width-1
Sy = room_height


//RenderText("2023",Sx/2,5,7,7,["Center","Top"])
//RenderText("Release of 5.4",Sx/2,25,7,7,["Center","Top"])
//RenderText("A lot",Sx/2,34,5,5,["Center","Top"])
// Desktop
lclick = mouse_check_button_pressed(1)
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
	X = 100 
	Y = 75
	
	draw_sprite(Outline,0,X,Y)
	draw_sprite_ext(Icon[0],0,X+16,Y+10,13/sprite_get_width(Icon[0]),13/sprite_get_height(Icon[0]),0,#ffffff,1)
	RenderText(string_replace(Icon[1],"\\n"," "),X+45,Y+11,10,10,["Left","Top"],#ffffff) 
	draw_sprite(Icon[3][Icon[4]],current_second%sprite_get_number(Icon[3][Icon[4]]),X+15,Y+42)
	
	CreateButton(X+600-32.5,Y+9,"X",function(){
		i = 0
		for (i = 0; i < array_length(Tasks);i++)
		{
			if Tasks[i] == Win
				break
		}
		array_delete(Tasks,i,1)
		Win = "|"
		Icon[2] = false
	})
	
	CreateButton(X+600-52.5,Y+9,"_",function(){ Win = "|" })
	
	if array_length(Icon[3]) > 1
	{
		if Icon[4] > 0
			CreateButton(X+300-19,Y+27,"<",function(){ Icon[4] -= 1 })
			
		
		if Icon[4] < array_length(Icon[3])-1
			CreateButton(X+300,Y+27,">",function(){ Icon[4] += 1 })
	}
}

// Task bar
draw_rectangle_color(0,Sy-22,Sx,Sy,#C0C0C0,#C0C0C0,#C0C0C0,#C0C0C0,false)

//Tasks
Tx = 3+sprite_get_width(Start)+2
draw_sprite(Start,0,3,Sy-1)

array_foreach(Tasks,function(el,ix){
	splt = string_split(el,"|")
	Icon = Icons[int64(splt[0])][int64(splt[1])]
	c1 = #ffffff
	c2 = #000000
	if Win != el
	{
		c1 = #000000
		c2 = #ffffff
	}
	
	draw_sprite_ext(Icon[0],0,Tx+1,Sy-18,15/sprite_get_width(Icon[0]),15/sprite_get_height(Icon[0]),0,#ffffff,1)
	text = RenderText(string_replace(Icon[1],"\\n"," "),Tx+20,Sy-13,7,7,["Left","Top"],#000000)
	
	draw_rectangle_color(Tx,Sy-19,Tx+1,Sy-2,c1,c1,c1,c1,false)
	draw_rectangle_color(Tx,Sy-19,text[0],Sy-19,c1,c1,c1,c1,false)
	draw_rectangle_color(Tx,Sy-2,text[0],Sy-2,c2,c2,c2,c2,false)
	draw_rectangle_color(text[0],Sy-19,text[0]+1,Sy-2,c2,c2,c2,c2,false)
	
	isover = mouse_x >= Tx and mouse_x <= text[0]+1 and mouse_y >= Sy-19 and mouse_y <= Sy-2
	
	if isover and lclick
		Win = el
	
	Tx = text[0]+4
})



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