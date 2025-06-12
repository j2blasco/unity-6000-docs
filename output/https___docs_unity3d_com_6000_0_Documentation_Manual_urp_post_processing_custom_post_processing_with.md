* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/custom-post-processing-with-volume.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Custom post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/custom-post-processing.html)
  * Create a custom post-processing effect with Volume support in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)
Create a low-code custom post-processing effect in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/renderer-feature-full-screen-pass.html)
Full Screen Pass Renderer Feature reference for URP
# Create a custom post-processing effect with Volume support in URP
This page describes how to create a custom **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effect with Volume support.
URP provides a template for custom post-processing effects. The implementation in the template consists of a Renderer Feature, where you can inject the code for the custom effect, and the script that implements the code for interacting with the Volume component.
To create an effect using the template, select the following menu item:
  * **Assets** > **Create** > **Rendering** > **URP Post-processing Effect (Renderer Feature with Volume)**.


Unity creates two new **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) in the `Assets` folder: the script containing the Renderer Feature template and the Volume component script.
The template contains the example effect implementation that inverts colors on the screen.
In the Renderer Feature, in the `Create` method you define the custom Material for the custom effect or the render pass that implements the effect logic.
The Renderer Feature script contains the `ScriptableRenderPass` implementation.
You set the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) properties for the custom effect in the following region in the render pass code:
```
#region PASS_SHARED_RENDERING_CODE

```

The render pass contains the following two regions. Unity selects the `PASS_RENDER_GRAPH_PATH` region and uses the render graph API if [Compatibility mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html) is disabled for the project, and uses the `PASS_NON_RENDER_GRAPH_PATH` region otherwise.
```
#region PASS_NON_RENDER_GRAPH_PATH

```
```
#region PASS_RENDER_GRAPH_PATH

```

To set the effect properties on the volume component, modify the following line in the `AddRenderPasses` method:
```
NewPostProcessEffectVolumeComponent myVolume = VolumeManager.instance.stack?.GetComponent<NewPostProcessEffectVolumeComponent>();
if (myVolume == null || !myVolume.IsActive())
    s_SharedPropertyBlock.SetFloat("_Intensity", myVolume.intensity.value);

```

## Additional resources
  * [Render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * [Example of a complete Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html)
  * [Compatibility Mode (Render Graph Disabled)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)
Create a low-code custom post-processing effect in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/renderer-feature-full-screen-pass.html)
Full Screen Pass Renderer Feature reference for URP
