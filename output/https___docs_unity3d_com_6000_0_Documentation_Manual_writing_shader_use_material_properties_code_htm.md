* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-use-material-properties-code.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Adding material properties to shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-change-properties.html)
  * Access material properties in a script


[](https://docs.unity3d.com/6000.0/Documentation/Manual/material-properties-texture-properties.html)
Texture properties
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-use-material-properties.html)
Set shader variables with material property values
# Access material properties in a script
Material properties are represented in C# code by the [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) class.
To access variables defined in your HLSL code, you can call [Material.GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetFloat.html), [Material.SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetFloat.html). There are other, similar methods; see the [Material API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) for a full list. When you access HLSL variables using these APIs, it doesn’t matter whether the variable is a material property or not.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/material-properties-texture-properties.html)
Texture properties
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-use-material-properties.html)
Set shader variables with material property values
