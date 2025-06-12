* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/canvas-shader.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Shader Material Inspector window reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-reference.html)
  * Canvas Shader Graph


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/particles-unlit-shader.html)
Particles Unlit Shader Material Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
Shaders in the Built-In Render Pipeline
# Canvas Shader Graph
The Canvas material type enables you to author **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Graph shaders that can be applied to [UGUI user interface elements](https://docs.unity3d.com/Packages/com.unity.ugui@1.0/manual/UICanvas.html).
## Contexts
This material type comes with a distinct set of Graph Settings, which significantly affects the Blocks relevant to the Graph. This section provides details regarding the Blocks automatically added by default in this Master Stack material type and the Blocks that determine properties for the Graph Settings of this material type.
### Vertex Context
The Vertex context represents the vertex stage of this shader. Unity executes any block you connect to this context in the vertex function of this shader. For more information, refer to [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.0/manual/Master-Stack.html).
Vertex blocks are not compatible with the Canvas Master Stack.
### Fragment Context
The Fragment Context contains the default and relevant Blocks for the Canvas material.
#### Default Fragment Context
When you create a new Canvas material, the Fragment Context contains the following Blocks by default:
**Property** | **Description** | **Setting dependency** | **Default value**  
---|---|---|---  
**Base Color** | The base color of the material. | None | Color.grey  
**Alpha** | The Material’s alpha value. | None | 1.0  
**Emission** | The color of light to emit from this material’s surface. Emissive materials appear as a source of light in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). | None | Color.black  
#### Relevant Fragment Context
Depending on the [Graph Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/canvas-shader.html#graph-settings) you use, Shader Graph might add the following Blocks to the Fragment Context:
**Property** | **Description** | **Setting dependency** | **Default value**  
---|---|---|---  
**Alpha Clip Threshold** | The alpha value limit that URP uses to determine whether to render each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel). If the alpha value of the pixel is equal to or higher than the limit, URP renders the pixel. If the value is lower than the limit, URP does not render the pixel. The default value is 0.5. |  **Alpha Clipping** enabled | 0.5  
## Graph Settings
The following table describes the Surface Options in the Graph Settings:
**Property** | **Description**  
---|---  
**Material Type** | Specifies a type for the material. This allows you to customize the material with different settings depending on the type you select. The options are:  
• **Sprite Custom Lit**  
• **Sprite Lit**  
• **Sprite Unlit**  
• **Canvas**  
• **Decal**  
• **Fullscreen**  
• **Lit**  
• **Unlit** :  
**Alpha Clipping** | Indicates whether this material acts like a [Cutout Shader](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterRenderingMode.html).  
## Additional resources
  * [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.0/manual/)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/particles-unlit-shader.html)
Particles Unlit Shader Material Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
Shaders in the Built-In Render Pipeline
