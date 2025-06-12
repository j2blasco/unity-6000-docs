* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-functions.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-writing-shaders.html)
  * DOTS Instancing shader functions reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-macros.html)
DOTS Instancing shader macros reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger.html)
Rendering Debugger in URP
# DOTS Instancing shader functions reference for URP
Alongside the access macros, Unity provides **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) functions that load the values of constants directly from the draw command data. Shaders that Unity provides use these functions. 
Unity provides the following shader functions:
**Shader function** | **Description**  
---|---  
`LoadDOTSInstancedData_RenderingLayer` | Returns the [renderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-renderingLayerMask.html) for the draw command.  
`LoadDOTSInstancedData_MotionVectorsParams` | Returns the [motion vector generation mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-motionMode.html) for the draw command. This is formatted as a float4, which is what Unity shaders expect.  
`LoadDOTSInstancedData_WorldTransformParams` | Returns whether to draw the instance with a flipped triangle winding. See [FlipWinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.FlipWinding.html).  
`LoadDOTSInstancedData_LightData` | Returns whether the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)’s main Directional Light is active for the instance. The main light can be deactivated for multiple reasons, for example if the light already included in light maps.  
`LoadDOTSInstancedData_LODFade` | Returns the 8 bit crossfade value you set if the [LODCrossFade flag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.LODCrossFade.html) is set. If the flag is not set, the return value is undefined.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-macros.html)
DOTS Instancing shader macros reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger.html)
Rendering Debugger in URP
