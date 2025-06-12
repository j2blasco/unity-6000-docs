* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/MaterialsAccessingViaScript.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)
  * Access material properties in a script


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upgrade-material.html)
Upgrade material assets to URP or HDRP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-landingpage.html)
Material Variants
# Access material properties in a script
All the parameters of a material asset that you see in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window are accessible via script, giving you the power to change or animate how a material works at runtime.
This allows you to modify numeric values on the material, change colours, and swap textures dynamically during gameplay. Some of the most commonly used methods to do this are:
Method Name | Use  
---|---  
[SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColor.html) | Change the color of a material (Eg. the albedo tint color)  
[SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetFloat.html) | Set a floating point value (Eg. the normal map multiplier)  
[SetInteger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetInteger.html) | Set an integer value in the material  
[SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html) | Assign a new texture to the material  
The full set of methods available for manipulating materials via script can be found on the [Material class scripting reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).
One important note is that these methods **only set properties that are available for the current**Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object** on the material. This means that if you have a shader that doesn’t use any textures, or if you have no shader bound at all, calling [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html) will have no effect. This is true even if you later set a shader that needs the texture. For this reason it is recommended to set the shader you want before setting any properties. However, after you have set the shader you can switch from one shader to another that use the same textures or properties and values will be preserved.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upgrade-material.html)
Upgrade material assets to URP or HDRP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-landingpage.html)
Material Variants
