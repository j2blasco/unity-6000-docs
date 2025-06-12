* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-screen-space-shadows.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Shadows in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Shadows-in-URP.html)
  * Add screen space shadows in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shadow-resolution-urp.html)
Configure shadow resolution in the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao-landing.html)
Screen space ambient occlusion (SSAO) in URP
# Add screen space shadows in URP
![Screen-space shadows](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/ssshadows/ssshadows-result.png)  
_Screen-space shadows in a sample scene._
You can add a [Screen Space Shadows Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-screen-space-shadows.html) to a Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) renderer. This makes URP use a single **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) to calculate and draw shadows from the main Directional Light, instead of multiple [shadow cascade](https://docs.unity3d.com/Manual/shadow-cascades.html) textures.
The Screen Space Shadows Renderer Feature doesn’t affect how shadows look. 
If your project uses the [Forward Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html), screen-space shadows might make rendering faster, because the Universal Render Pipeline (URP) doesn’t need to access multiple shadow cascade textures.
Screen-space shadows have the following limitations:
  * URP adds a depth prepass so it can sample the depth texture. This might reduce performance on mobile platforms that use tile-based rendering. Refer to [Depth Priming Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html#rendering) for more information about the depth prepass.
  * URP creates a screen-space shadows texture, which uses more memory.


![Screen-space shadows texture](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/ssshadows/ssshadows-shadow-texture.png)  
_The screen-space shadows texture for the previous image._
## Enable screen-space shadows
To add screen-space shadows to your project, add the Screen Space Shadows Renderer Feature. Refer to [Add a renderer feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html).
URP doesn’t calculate or draw screen-space shadows for transparent objects. URP uses shadow maps for transparent objects instead.
## View screen-space shadows
Use the [Frame Debugger](https://docs.unity3d.com/Manual/FrameDebugger.html) to view the render passes that draw shadows. Check the following render passes:
  * **ScreenSpaceShadows** , which creates the screen-space shadows texture.
  * **MainLightShadow** , which creates shadow map textures.


Check the **DrawOpaqueObjects** render pass to check which shadow texture URP uses to draw shadows on each object.
![Shadows using the screen-space shadows texture](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/ssshadows/ssshadows-cast-shadow-using-screenspace.png)  
_The Frame Debugger with screen-space shadows enabled. The objects in the**DrawOpaqueObjects** render pass use **_ScreenSpaceShadowmapTexture**._
![Shadows using shadow maps](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/ssshadows/ssshadows-cast-shadow-using-cascades.png)  
_The Frame Debugger with screen-space shadows disabled. The objects in the**DrawOpaqueObjects** render pass use **TempBuffer 398 2048x1024** and **TempBuffer 399 2048x2048** , which are shadow map textures from the **MainLightShadow** render pass._
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shadow-resolution-urp.html)
Configure shadow resolution in the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao-landing.html)
Screen space ambient occlusion (SSAO) in URP
