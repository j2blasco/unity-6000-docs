* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PropertiesInPrograms.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Adding material properties to shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-change-properties.html)
  * Add material properties


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-material-properties.html)
Introduction to material properties
[](https://docs.unity3d.com/6000.0/Documentation/Manual/material-properties-texture-properties.html)
Texture properties
# Add material properties
To assign material properties to a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object in **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab), you place a `Properties` block inside a `Shader` block.
If you want to access some of those properties in a [shader program](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html), you need to declare a Cg/HLSL variable with the same name and a matching type.
For example these shader properties:
```
_MyColor ("Some Color", Color) = (1,1,1,1) 
_MyVector ("Some Vector", Vector) = (0,0,0,0) 
_MyFloat ("My float", Float) = 0.5 
_MyTexture ("Texture", 2D) = "white" {} 
_MyCubemap ("Cubemap", CUBE) = "" {} 

```

would be declared for access in Cg/HLSL code as:
```
fixed4 _MyColor; // low precision type is usually enough for colors
float4 _MyVector;
float _MyFloat; 
sampler2D _MyTexture;
samplerCUBE _MyCubemap;

```

Cg/HLSL can also accept **uniform** keyword, but it is not necessary:
```
uniform float4 _MyColor;

```

Property types in ShaderLab map to Cg/HLSL variable types this way:
  * Color and Vector properties map to **float4** , **half4** or **fixed4** variables.
  * Range and Float properties map to **float** , **half** or **fixed** variables.
  * Texture properties map to **sampler2D** variables for regular (2D) textures; **Cubemaps** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) map to **samplerCUBE** ; and 3D textures map to **sampler3D**.


## Color spaces and color/vector shader data
When using [Linear color space](https://docs.unity3d.com/6000.0/Documentation/Manual/color-spaces-landing.html), all material color properties are supplied as sRGB colors, but are converted into linear values when passed into shaders.
For example, if your [Properties](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html) shader block contains a `Color` property called “ _MyColor“, then the corresponding ”_ MyColor” HLSL variable will get the linear color value.
For properties that are marked as `Float` or `Vector` type, no color space conversions are done by default; it is assumed that they contain non-color data. It is possible to add `[Gamma]` attribute for float/vector properties to indicate that they are specified in sRGB space, just like colors (see [Properties](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html)).
## Additional resources
  * [Properties block reference in ShaderLab](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html)
  * [Writing Shader Programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-material-properties.html)
Introduction to material properties
[](https://docs.unity3d.com/6000.0/Documentation/Manual/material-properties-texture-properties.html)
Texture properties
