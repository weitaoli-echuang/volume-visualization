#version 130

// --> to be used with #version 430
//layout (location = 0)   
in vec3 VerPos;

// --> to be used with #version 430
//layout (location = 1) 
in vec3 VerClr;  


out vec3 EntryPoint;
out vec4 ExitPointCoord;

uniform mat4 MVP;

void main()
{
	
    EntryPoint = VerClr;
    gl_Position = MVP * vec4(VerPos,1.0);
    
    ExitPointCoord = gl_Position;  
}