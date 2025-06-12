* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [Shader in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader-object.html)
  * Fallback block in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html)
Properties block reference in ShaderLab
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CustomEditor.html)
Custom Editor block in ShaderLab reference
# Fallback block in ShaderLab reference
This page contains information on using a `Fallback` block in your **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) code to assign a fallback **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object. For information on how a **Shader object** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject) works, and how Unity chooses when to use a fallback, see [Shader objects introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html).
## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: Fallback block** | Yes | Yes | Yes | Yes  
## Syntax
To assign a fallback, you place a `Fallback` block inside a `Shader` block.
**Signature** | **Function**  
---|---  
`Fallback "<name>"` | If no compatible SubShaders are found, use the named Shader object.  
`Fallback Off` | Do not use a fallback Shader object in place of this one. If no compatible SubShaders are found, display the [error shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-error.html).  
## Example
This example code demonstrates the syntax for creating a Shader object that has a named fallback.
```
Shader "Examples/ExampleFallback"
{
    SubShader
    {
        // Code that defines the SubShader goes here.

        Pass
        {                
              // Code that defines the Pass goes here.
        }
    }

    Fallback "ExampleOtherShader"
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html)
Properties block reference in ShaderLab
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CustomEditor.html)
Custom Editor block in ShaderLab reference
