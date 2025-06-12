* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BindChannels.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [ShaderLab legacy functionality reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-legacy.html)
  * ShaderLab: legacy vertex data channel mapping


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SetTexture.html)
ShaderLab: legacy texture combining
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PragmaDirectives.html)
HLSL pragma directives reference
# ShaderLab: legacy vertex data channel mapping
**Note** : The **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) functionality on this page is legacy, and is documented for backwards compatibility only. If your **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) source file includes HLSL code, Unity ignores these commands completely. If your shader source file does not include HLSL code, Unity compiles these commands into regular shader programs on import.
## Render pipeline compatibility
**Feature name** | **Built-in**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline)** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP**  
---|---|---|---|---  
**Legacy vertex data channel mapping** | Yes | No | No | No  
## Overview
The **BindChannels** command allows you to specify how vertex data maps to the graphics hardware. By default, Unity figures out the bindings for you, but in some cases you want custom ones to be used. 
For example you could map the primary UV set to be used in the first texture stage and the secondary UV set to be used in the second texture stage; or tell the hardware that vertex colors should be taken into account.
## Syntax
```
BindChannels { Bind "source", target }

```

Specifies that vertex data _source_ maps to hardware _target_.
**Source** can be one of:
  * **Vertex** : vertex position
  * **Normal** The direction perpendicular to the surface of a mesh, represented by a Vector. Unity uses normals to determine object orientation and apply shading. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normal): vertex normal
  * **Tangent** : vertex tangent
  * **Texcoord** : primary UV coordinate
  * **Texcoord1** : secondary UV coordinate
  * **Color** : per-vertex color


**Target** can be one of:
  * **Vertex** : vertex position
  * **Normal** : vertex normal
  * **Tangent** : vertex tangent
  * **Texcoord0** , **Texcoord1** , …: texture coordinates for corresponding texture stage
  * **Texcoord** : texture coordinates for all texture stages
  * **Color** : vertex color


## Details
Unity places some restrictions on which sources can be mapped to which targets. Source and target must match for **Vertex** , **Normal** , **Tangent** and **Color**. Texture coordinates from the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) (**Texcoord** and **Texcoord1**) can be mapped into texture coordinate targets (**Texcoord** for all texture stages, or **TexcoordN** for a specific stage).
There are two typical use cases for BindChannels:
  * Shaders that take vertex colors into account.
  * Shaders that use two UV sets.


## Examples
```
// Maps the first UV set to the first texture stage
// and the second UV set to the second texture stage
BindChannels {
   Bind "Vertex", vertex
   Bind "texcoord", texcoord0
   Bind "texcoord1", texcoord1
}

```
```
// Maps the first UV set to all texture stages
// and uses vertex colors
BindChannels {
   Bind "Vertex", vertex
   Bind "texcoord", texcoord
   Bind "Color", color
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SetTexture.html)
ShaderLab: legacy texture combining
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PragmaDirectives.html)
HLSL pragma directives reference
