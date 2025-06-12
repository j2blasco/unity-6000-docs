* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-prioritize-lower-quality-shaders.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Configure when and if Unity uses a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
  * Prioritize lower quality shaders with the LOD command


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-set-pass.html)
Set when Unity runs a shader pass via a LightMode tag
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-disable-dynamic-batching.html)
Disable dynamic batching of a shader
# Prioritize lower quality shaders with the LOD command
You can assign a **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) value to a SubShader. This value indicates how computationally demanding it is.
At runtime, you can set the ****shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) LOD** value for a single **Shader object** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject), or for all Shader objects. Unity then prioritises SubShaders that have a lower LOD value. For information on how Unity chooses when to use SubShaders, see [How Unity selects a subshader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html#selecting-subshaders).
**Note:** Although this technique is named after the LOD feature for rendering meshes, there are important differences: shader LOD does not relate to distance from the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), and Unity does not calculate shader LOD automatically. You must set the maximum shader LOD manually.
Use this technique to fine-tune shader performance on different hardware. This is useful when a SubShader is theoretically supported by a user’s hardware, but the hardware is not capable of running it well.
**Note** : Inside your `Shader` block, you must put your SubShaders in descending LOD order. For example, if you have SubShaders with LOD values of 200, 100, and 500, you must put the SubShader with the LOD value of 500 first, followed by the one with a LOD value of 200, followed by the one with a LOD value of 100. This is because Unity selects the first valid SubShader it finds, so if it finds one with a lower LOD first it will always use that.
## Example
This example code creates a Shader object that contains two SubShaders: one with a LOD value of 200, and one with a value of 100. The SubShaders are in descending order of LOD value.
```
Shader "Examples/ExampleLOD"
{
    SubShader
    {
        LOD 200

        Pass
        {                
              // The rest of the code that defines the Pass goes here.
        }
    }

    SubShader
    {
        LOD 100

        Pass
        {                
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Using the SubShader LOD value with C# code
To set the shader LOD for a given Shader object, you can use [Shader.maximumLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-maximumLOD.html). To set the shader LOD for all Shader objects, you can use [Shader.globalMaximumLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalMaximumLOD.html). By default, there is no maximum LOD.
## Additional resources
  * [LOD directive in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderLOD.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-set-pass.html)
Set when Unity runs a shader pass via a LightMode tag
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-disable-dynamic-batching.html)
Disable dynamic batching of a shader
