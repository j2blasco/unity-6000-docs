* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Custom post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/custom-post-processing.html)
  * [Creating a full-screen shader in Shader Graph in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-urp.html)
  * Fullscreen Master Stack reference for Shader Graph in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-urp.html)
Creating a full-screen shader in Shader Graph in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)
Fullscreen Master Stack in Shader Graph reference for URP
# Fullscreen Master Stack reference for Shader Graph in URP
Use the Fullscreen Master Stack to create a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Graph material to apply to the entire screen at the end of the rendering process. You can use this to create custom post-process and custom pass effects.
![A full-screen shader that applies a raindrop effect to the screen.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/Fullscreen-shader-rain.png) A full-screen shader that applies a raindrop effect to the screen.
## Contexts
A shader graph contains the following contexts:
  * [Vertex context](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html#vertex-context)
  * [Fragment context](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html#fragment-context)


The Fullscreen Master Stack has its own [Graph Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html) that determine which blocks you can use in the Shader Graph contexts.
This section contains information on the blocks that this Master Stack material type uses by default, and which blocks you can use to affect the Graph Settings.
###  Vertex context
The Vertex context represents the vertex stage of this shader. Unity executes any block you connect to this context in the vertex function of this shader. For more information, refer to [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph@14.0/manual/Master-Stack.html).
Vertex blocks are not compatible with the Fullscreen Master Stack.
###  Fragment context
The Fragment context represents the fragment (or pixel) stage of this shader. Unity executes any block you connect to this context in the fragment function of this shader. For more information, refer to [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph@14.0/manual/Master-Stack.html).
### Default
When you create a new Fullscreen Master Stack, the Fragment context contains the following blocks by default.
**Property** | **Description** | **Setting Dependency** | **Default Value**  
---|---|---|---  
**Base Color** | The base color of the material. | None | Color.grey  
**Alpha** | The Material’s alpha value. This determines how transparent the material is. The expected range is 0 - 1. | None | 1.0  
### Relevant
The following blocks are also compatible with the Fullscreen master stack.
**Property** | **Description** | **Setting Dependency** | **Default Value**  
---|---|---|---  
**Eye Depth** | Scales a value to world space to represent the depth from the near plane. This value represents a point in world space, determined by the platform you use. For more information, refer to [The Depth (Z) direction in Shaders](https://docs.unity3d.com/Manual/SL-PlatformDifferences.html). | In **Graph Settings** : • Enable **Depth Write**.  
• Set **Depth Write Mode** to **LinearEye**. | 0  
**Linear 01 Depth** | Uses a linear depth value between 0 and 1. | In **Graph Settings** : • Enable **Depth Write**.  
• Set **Depth Write Mode** to **Linear01**. | 0  
**Raw Depth** | Samples the depth value from the depth buffer. You can also use this setting with a nonlinear depth value. | In **Graph Settings** : • Enable **Depth Write**.  
• Set **Depth Write Mode** to **Raw**. | 0  
## Fullscreen Master Stack reference
For more information about the properties available in the Fullscreen Master Stack, refer to the [Master Stack Fullscreen reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-urp.html)
Creating a full-screen shader in Shader Graph in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)
Fullscreen Master Stack in Shader Graph reference for URP
