* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/renderer-feature-full-screen-pass.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Custom post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/custom-post-processing.html)
  * Full Screen Pass Renderer Feature reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/custom-post-processing-with-volume.html)
Create a custom post-processing effect with Volume support in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-urp.html)
Creating a full-screen shader in Shader Graph in URP
# Full Screen Pass Renderer Feature reference for URP
The Full Screen Pass Renderer Feature lets you inject full screen render passes at pre-defined injection points to create full screen effects.
You can use this Renderer Feature to create [custom post-processing effects](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/custom-post-processing.html).
## How to use the feature
To add the Renderer Feature to your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene):
  1. [Add the Full Screen Pass Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html) to the URP Renderer.


Refer to the following page for an example of how to use this feature:
  * [How to create a custom post-processing effect](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/post-processing-custom-effect-low-code.html).


## Properties
The Full Screen Pass Renderer Feature contains the following properties.
Property | Description  
---|---  
**Name** | Name of the Full Screen Pass Renderer Feature.  
**Pass Material** | The Material the Renderer Feature uses to render the effect.  
**Injection Point** | Select when the effect is rendered:
  * **Before Rendering Transparents** : Add the effect after the skybox pass and before the transparents pass.
  * **Before Rendering Post Processing** : Add the effect after the transparents pass and before the post-processing pass.
  * **After Rendering Post Processing** : Add the effect after the post-processing pass and before AfterRendering pass.

**After Rendering Post Processing** is the default setting.  
**Requirements** | Select one or more of the following passes for the Renderer Feature to use:
  * **None** : Add no additional passes.
  * **Everything** : Adds all additional passes available (Depth, Normal, Color, and Motion).
  * **Depth** : Adds a depth prepass to enable the use of depth values. For more information, refer to **Depth Texture** in [Camera Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html)
  * **Normal** : Enables the use of normal vector data.
  * **Color** : Copies color data of a screen to the _BlitTexture texture inside the shader.
  * **Motion** : Enables the use of motion vectors.

**Color** is the default setting.  
**Pass Index** | Select a specific pass inside the Pass Material’s shader for the Pass Material to use.  
  
This option is hidden by default. To access this option, click ⋮ in the Renderer Feature section of the Inspector and select **Advanced Properties**.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/custom-post-processing-with-volume.html)
Create a custom post-processing effect with Volume support in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/fullscreen-master-stack-urp.html)
Creating a full-screen shader in Shader Graph in URP
