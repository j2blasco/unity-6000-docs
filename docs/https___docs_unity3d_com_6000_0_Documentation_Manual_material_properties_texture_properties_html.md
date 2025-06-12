* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/material-properties-texture-properties.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Adding material properties to shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-change-properties.html)
  * Texture properties


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PropertiesInPrograms.html)
Add material properties
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-use-material-properties-code.html)
Access material properties in a script
# Texture properties
For each texture that is setup as a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader)/material property, Unity also sets up some extra information in additional vector properties.
## Texture tiling & offset
[Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) often have Tiling and Offset fields for their texture properties. This information is passed into shaders in a float4 _{TextureName}_`_ST` property:
  * `x` contains X tiling value
  * `y` contains Y tiling value
  * `z` contains X offset value
  * `w` contains Y offset value


For example, if a shader contains texture named `_MainTex`, the tiling information will be in a `_MainTex_ST` vector.
## Texture size
_{TextureName}_`_TexelSize` - a float4 property contains texture size information:
  * `x` contains 1.0/width
  * `y` contains 1.0/height
  * `z` contains width
  * `w` contains height


## Texture HDR parameters
_{TextureName}_`_HDR` - a float4 property with information on how to decode a potentially **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) (e.g. RGBM-encoded) texture depending on the [color space](https://docs.unity3d.com/6000.0/Documentation/Manual/color-spaces-landing.html) used. See `DecodeHDR` function in [UnityCG.cginc](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html) shader include file.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PropertiesInPrograms.html)
Add material properties
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-use-material-properties-code.html)
Access material properties in a script
