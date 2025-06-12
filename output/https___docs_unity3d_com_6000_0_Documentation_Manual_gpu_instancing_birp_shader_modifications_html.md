* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-birp-shader-modifications.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-birp.html)
  * [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-shader.html)
  * GPU instancing shader reference for the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-strip-variants.html)
Prevent Unity stripping GPU instancing shaders in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-landing.html)
Graphics performance and profiling reference
# GPU instancing shader reference for the Built-In Render Pipeline
This section contains information about **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) additions that relate to GPU instancing.
Addition | Description  
---|---  
`#pragma multi_compile_instancing` | Generates instancing variants. This is required for fragment and **vertex shaders** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader). It is optional for **Surface Shaders** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader).  
`#pragma instancing_options` | Specifies options that Unity uses for instances. For information on the option switches available, see [`#pragma instancing_options`](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-birp-shader-modifications.html#instancing_options-switches).  
`UNITY_VERTEX_INPUT_INSTANCE_ID` | Defines an instance ID in the vertex shader input/output structure. To use this macro, enable the INSTANCING_ON shader keyword. Otherwise, Unity doesn’t set up the instance ID.  
To access the instance ID, use `vertexInput.instanceID` inside an #ifdef INSTANCING_ON block. If you don’t use this block, variants fail to compile.  
`UNITY_INSTANCING_BUFFER_START(bufferName)` | Declares the start of a per-instance constant buffer named `bufferName`. Use this macro with `UNITY_INSTANCING_BUFFER_END` to wrap declarations of the properties that you want to be unique to each instance. Declare properties inside the buffer using`UNITY_DEFINE_INSTANCED_PROP`.  
`UNITY_INSTANCING_BUFFER_END(bufferName)` | Declares the end of a per-instance constant buffer named `bufferName`. Use this macro with `UNITY_INSTANCING_BUFFER_START` to wrap declarations of the properties that you want to be unique to each instance. Declare properties inside the buffer using`UNITY_DEFINE_INSTANCED_PROP`.  
`UNITY_DEFINE_INSTANCED_PROP(type, propertyName)` | Defines a per-instance shader property with the specified type and name. In the examples below, the `_Color` property is unique.  
`UNITY_SETUP_INSTANCE_ID(v);` | Allows shader functions to access the instance ID. For vertex shaders, this macro is required at the beginning. For fragment shaders, this addition is optional. For an example, see [Vertex and fragment shader](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-vertex-fragment-shader-example.html).  
`UNITY_TRANSFER_INSTANCE_ID(v, o);` | Copies the instance ID from the input structure to the output structure in the vertex shader. Use this macro if you need to access per-instance data in the fragment shader.  
`UNITY_ACCESS_INSTANCED_PROP(bufferName, propertyName)` | Accesses a per-instance shader property in an instancing constant buffer. Unity uses the instance ID to index into the instance data array.`bufferName` must match the name of the constant buffer that contains the specified property.This macro compiles differently for INSTANCING_ON and non-instancing variants.  
## Instancing_options switches
The [#pragma instancing_options](#pragma-instancing_options) directive can use the following switches:
**Switch** | **Description**  
---|---  
`forcemaxcount:batchSize` and `maxcount:batchSize` | On most platforms, Unity automatically calculates the instancing data array size. It divides the maximum constant buffer size on the target device with the size of the structure that contains all per-instance properties. Generally, you don’t need to worry about the batch size. However, some platforms require a fixed array size. To specify the batch size for those platforms, use the `maxcount` option. Other platforms ignore this option. If you want to force a batch size for all platforms, use `forcemaxcount`. This is useful when, for example, your project uses RenderMeshInstanced to issue draw calls with 256 instanced **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite). The default value for the two options is 500.  
`assumeuniformscaling` | Instructs Unity to assume that all the instances have uniform scalings (the same scale for all X, Y, and Z axes).  
`nolodfade` | Makes Unity not apply GPU instancing to [LOD](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) fade values.  
`nolightprobe` | Prevents Unity from applying GPU instancing to [Light Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) values and their occlusion data. Setting this option to `ON` can improve performance if your project doesn’t contain **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that use both GPU instancing and Light Probes.  
`nolightmap` | Prevents Unity from applying GPU instancing to **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) atlas information values. Setting this option to `ON` can improve performance if your project doesn’t contain GameObjects that use both GPU instancing and lightmaps.  
`procedural:FunctionName` | Generates an additional variant for use with [Graphics.RenderMeshIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshIndirect.html). At the beginning of the vertex shader stage, Unity calls the function specified after the colon. To set up the instance data manually, add per-instance data to this function in the same way you would normally add per-instance data to a shader. Unity also calls this function at the beginning of a fragment shader if any of the fetched instance properties are included in the fragment shader.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-strip-variants.html)
Prevent Unity stripping GPU instancing shaders in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-landing.html)
Graphics performance and profiling reference
