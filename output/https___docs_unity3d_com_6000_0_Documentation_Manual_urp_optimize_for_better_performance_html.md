* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/optimize-for-better-performance.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Reducing rendering work on the CPU or GPU in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance-urp.html)
  * Adjust settings to improve performance in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-culling.html)
Enable GPU occlusion culling in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/xr-untethered-device-optimization.html)
Optimize for untethered XR devices in URP
# Adjust settings to improve performance in URP
If the performance of your Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) project seems slow, you can adjust settings to increase performance.
Based on your [analysis](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/analyze-your-project.html), you can adjust the following settings in the [Universal Render Pipeline (URP) Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html) or the [Universal Renderer asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html) to improve the performance of your project.
Depending on your project or the platforms you target, some settings might not have a significant effect. There might also be other settings that have an effect on performance in your project.
**Setting** | **Where the setting is** | **What to do for better performance**  
---|---|---  
**Accurate G-buffer normals** |  [Universal Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html) > **Rendering** | Disable if you use the Deferred rendering path  
**Additional Lights** > **Cast Shadows** |  [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html) > **Lighting** | Disable  
**Additional Lights** > **Cookie Atlas Format** | URP Asset > **Lighting** | Set to **Color Low**  
**Additional Lights** > **Cookie Atlas Resolution** | URP Asset > **Lighting** | Set to the lowest you can accept  
**Additional Lights** > **Per Object Limit** | URP Asset > **Lighting** | Set to the lowest you can accept. This setting has no effect if you use the Deferred or Forward+ rendering paths.  
**Additional Lights** > **Shadow Atlas Resolution** | URP Asset > **Lighting** | Set to the lowest you can accept  
**Additional Lights** > **Shadow Resolution** | URP Asset > **Lighting** | Set to the lowest you can accept  
**Cascade Count** | URP Asset > **Shadows** | Set to the lowest you can accept  
**Conservative Enclosing Sphere** | URP Asset > **Shadows** | Enable  
**Technique** | [Decal Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal.html) | Set to **Screen Space** , and set **Normal Blend** to **Low** or **Medium**  
**Fast sRGB/Linear conversion** | URP Asset > **Post Processing** | Enable  
**Grading Mode** | URP Asset > **Post Processing** | Set to **Low Dynamic Range**  
**LOD Cross Fade Dither** | URP Asset > **Quality** | Set to **Bayer Matrix**  
**LUT size** | URP Asset > **Post Processing** | Set to the lowest you can accept  
**Main Light** > **Cast Shadows** | URP Asset > **Lighting** | Disable  
**Max Distance** | URP Asset > **Shadows** | Reduce  
**Opaque Downsampling** | URP Asset > **Rendering** | If **Opaque Texture** is enabled in the URP Asset, set to **4x Bilinear**  
**Render Scale** | URP Asset > **Quality** | Set to below 1.0  
**Soft Shadows** | URP Asset > **Shadows** | Disable, or set to **Low**  
**Upscaling Filter** | URP Asset > **Quality** | Set to **Bilinear** or **Nearest-Neighbor**  
Refer to the following for more information on the settings:
  * [Deferred Rendering Path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
  * [Forward rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-rendering-paths.html)
  * [Decal Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal.html)
  * [Universal Render Pipeline Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html)
  * [Universal Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html)


## Additional resources
  * [Understand performance in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/understand-performance.html)
  * [Configure for better performance](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/configure-for-better-performance.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/Manual/graphics-performance-profiling.html)
  * [Best practices for profiling game performance](https://unity.com/how-to/best-practices-for-profiling-game-performance)
  * [Tools for profiling and debugging](https://unity.com/how-to/profiling-and-debugging-tools)
  * [Native CPU profiling: Tips to optimize your game performance](https://resources.unity.com/games/native-cpu-profiling-tips-to-optimize-your-game-performance)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-culling.html)
Enable GPU occlusion culling in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/xr-untethered-device-optimization.html)
Optimize for untethered XR devices in URP
