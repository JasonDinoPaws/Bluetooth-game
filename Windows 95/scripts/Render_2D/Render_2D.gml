global.Textures = {}

/*
global.letterconverts = [
	[".","dot"],
	[",","comma"],
	["+","add"],
	["-","minus"],
	["=","equal"],
	["_","uscore"],
	["\'","quoat"],
	["\"","quotDuble"],
	["?","quest"],
	["<","than"],
	[",","comma"],
	[":","col"],
	[";","semicol"],
	["/","slash"],
	["[","brake"]
]*/

array_foreach([],function(el,_){show_debug_message(string(ord(el))+"|"+el)})
function RenderLeter(Letter = "",Left = 0,Top = 0,XSize = 7,YSize = 7,Alignment = ["Left","Top"],Color = c_white)
{
		sprite = asset_get_index("_"+string_lower(Letter))
		
		if sprite == -1 and asset_get_index("_"+string(ord(Letter)))
		{
			sprite = asset_get_index("_"+string(ord(Letter)))
			XSize = sprite_get_width(sprite)*(XSize/sprite_get_height(sprite))
		}
		if Alignment[0] == "Right"
			Left -= XSize
		else if Alignment[0] == "Center"
			Left -= XSize/2
		
		if sprite > -1
			draw_sprite_ext(sprite,-1,Left,Top,XSize/sprite_get_width(sprite),YSize/sprite_get_height(sprite),0,Color,1)
			
		return [XSize,YSize]
}
function RenderText(Text = "",Left = 0,Top = 0,XSize = 7,YSize = 7,Alignment = ["Left","Top"],Color = c_white)
{
	if is_array(Text)
	{
		NText = ""
		for (var t = 0;t < array_length(Text);t++)
			NText += string(Text[t])
		Text = NText
	}
	
	arr = string_split(Text,"\\n")
	Text = arr[0]
	for (i = 1; i < array_length(arr); i++)
	{
		RenderText(arr[i],Left,Top+(YSize*i)+(2*i),XSize,YSize,Alignment,Color)	
	}
	
	if Alignment[0] == "Center"
		Left -= (string_length(Text)*XSize)/2
		Left -= string_length(Text)/2
		
	if Alignment[1] == "Center"
		Top = Top-(YSize/2)
	else if Alignment[1] == "Bottom"
		Top = Top-YSize*array_length(string_split(Text,"\n"))
	
	if Alignment[0] == "Right"
		for (var t = string_length(Text);t > 0;t--)
		{
			Size = RenderLeter(string_char_at(Text,t),Left,Top,XSize,YSize,Alignment,Color) 
			Left -= Size[0]
			Left -= 2
		}
	else
		for (var t = 1;t <= string_length(Text);t++)
		{
			Size = RenderLeter(string_char_at(Text,t),Left,Top,XSize,YSize,Alignment,Color) 
			Left += Size[0]+2
		}
		
	return [Left,Top]
}

function RenderGrid(Objs = ["Hello"],x1,x2,top,RowCells = 2,CellSize = [1,1],Offset = [2.5,2.5],Fun = function(Obj,ix,x1,y1,x2,y2){},Type = "Center")
{
	left = ((x1+x2)/2)-((RowCells/2)*CellSize[0])-((RowCells/2)*Offset[0])
	if Type == "Left"
		left = x1
	else if Type == "Right"
		left = x2
	if RowCells == -1
		RowCells = array_length(Objs)
	row = 0
	
	for (var i = 0; i < array_length(Objs); i ++)
	{
		Xcell = i-(row*RowCells)
		
		y1 = top+(CellSize[1]*row)+(Offset[1]*row)
		y2 = y1+CellSize[1]
		
		if Type == "Right"
			x1 = left-(Xcell*CellSize[0])+(Xcell*Offset[0])
		else
			x1 = left+(Xcell*CellSize[0])+(Xcell*Offset[0])
		x2 = x1+CellSize[0]
		

		Fun(Objs[i],i,  x1,y1,x2,y2)
		
		if Xcell+1 == RowCells
			row++
	}
	if Type == "Right"
		return [x1,y1]
	else
		return [x2,y1]
}

function RenderButton(x,y, xscale,yscale, Text = "Hello", InsideColor = c_white, selected = false)
{
	if !selected
	{
		xscale -= .072916*room_width
		yscale -= .03308*room_height
	}
	
	xscale = xscale/105
	yscale = yscale/25
	draw_sprite_ext(ButtonOutline,-1,x,y, xscale,yscale,0,selected?c_white:c_black,1)
	
	if selected
		draw_sprite_ext(ButtonSelected,-1,x,y, xscale,yscale,0,InsideColor,1)
	else
		draw_sprite_ext(ButtonUnselected,-1,x,y, xscale,yscale,0,#7F8480,1)
		
	
	RenderText(Text,x,y,xscale*14,yscale*14,["Center","Center"])
}

function CreateSprite(Path)
{
	if file_find_first(Path,fa_directory) != "" and !struct_exists(global.Textures,Path)
		struct_set(global.Textures,Path,sprite_add(Path,1,0,0,0,0))
	
	return struct_get(global.Textures,Path)
}

function MakeColor(colortab){ return make_color_rgb(colortab[0],colortab[1],colortab[2]) }