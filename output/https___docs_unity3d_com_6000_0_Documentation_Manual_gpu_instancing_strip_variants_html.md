* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-strip-variants.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-birp.html)
  * [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-shader.html)
  * Prevent Unity stripping GPU instancing shaders in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-change-data.html)
Example of changing per-instance data at runtime in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-birp-shader-modifications.html)
GPU instancing shader reference for the Built-In Render Pipeline
# Prevent Unity stripping GPU instancing shaders in the Built-In Render Pipeline
Unity generates Surface **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) with instancing [variants](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html) by default, unless you specify `noinstancing` in the `#pragma` directive. Unity ignores uses of #pragma multi_compile_instancing in a **surface shader** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader).
Unity’s Standard and StandardSpecular shaders have instancing support by default, but with no per-instance properties other than the transform.
If your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) contains no **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with GPU instancing enabled, then Unity strips instancing shader variants. To override the stripping behaviour:
  1. Open Project Settings (menu: **Edit** > **Project Settings**).
  2. Go to **Graphics**.
  3. In the **Shader Stripping** section, set **Instancing Variants** to **Keep All**.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-change-data.html)
Example of changing per-instance data at runtime in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-birp-shader-modifications.html)
GPU instancing shader reference for the Built-In Render Pipeline
