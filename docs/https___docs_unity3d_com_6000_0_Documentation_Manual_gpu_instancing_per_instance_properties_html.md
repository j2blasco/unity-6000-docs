* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-per-instance-properties.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-birp.html)
  * [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-shader.html)
  * Add per-instance properties to GPU instancing shaders in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-birp.html)
GPU Instancing in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-samples.html)
Examples of GPU instancing shaders in the Built-In Render Pipeline
# Add per-instance properties to GPU instancing shaders in the Built-In Render Pipeline
By default, Unity GPU instances **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with different [Transforms](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) in each instanced draw call. To add more variation to the instances, modify the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to add per-instance properties such as color. You can do this both in **surface shaders** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) and in vertex/fragment shaders.
Custom shaders don’t need per-instance data, but they do require an instance ID because world matrices need one to function correctly. Surface shaders automatically set up an instance ID, but custom vertex and fragment shaders don’t. To set up the ID for custom vertex and fragment shaders, use UNITY_SETUP_INSTANCE_ID at the beginning of the shader. For an example of how to do this, see [Vertex and fragment shader](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-vertex-fragment-shader-example.html).
When you declare an instanced property, Unity gathers all the property values from the MaterialPropertyBlock objects set on GameObjects into a single draw call. For an example of how to use MaterialPropertyBlock objects to set per-instance data at runtime, see [Changing per-instance data at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-change-data.html).
When adding per-instance data to multi-pass shaders, keep the following in mind:
  * If a multi-pass shader has more than two passes, Unity only instances the first pass. This is because Unity renders later passes together for each object, which forces material changes.
  * If you use the Forward **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) in the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), Unity can’t efficiently instance objects that are affected by multiple lights. Unity can only use instancing effectively for the base pass, not for additional passes. For more information about lighting passes, see documentation on [Forward Rendering and Pass Tags](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html).


When you use multiple per-instance properties, you don’t need to fill all of them in `MaterialPropertyBlock` objects. Also, if one instance lacks a property, Unity takes the default value from the referenced material. If the material doesn’t have a default value for the property, Unity sets the value to 0. Don’t put non-instanced properties in the `MaterialPropertyBlock`, because this disables instancing. Instead, create different materials for them.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-birp.html)
GPU Instancing in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-samples.html)
Examples of GPU instancing shaders in the Built-In Render Pipeline
