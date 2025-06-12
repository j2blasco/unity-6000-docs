* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/inject-render-pass-via-script.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/inject-a-render-pass.html)
  * Inject a render pass via scripting in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
Scriptable Renderer Feature API reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/restrict-render-pass-scene-area.html)
Restrict a render pass to a scene area in URP
# Inject a render pass via scripting in URP
To inject a custom render pass into the rendering loop in the Universal Rendering Pipeline (URP), subscribe to one of the events in the [RenderPipelineManager](https://docs.unity3d.com/ScriptReference/Rendering.RenderPipelineManager.html) API and use the [`EnqueuePass`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.2/api/UnityEngine.Rendering.Universal.ScriptableRenderer.html#UnityEngine_Rendering_Universal_ScriptableRenderer_EnqueuePass_UnityEngine_Rendering_Universal_ScriptableRenderPass) API.
For example, you can render extra cameras to **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture), and use those textures for effects like planar reflections or surveillance **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) views.
**Note** : `RenderPipelineManager` events trigger only if a camera is active.
Follow these steps:
  1. Attach a new `MonoBehaviour` script to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), then create an instance of a custom render pass. For example:
```
public class InjectPass : MonoBehaviour
{
    // Declare a custom render pass
    private ExampleRenderPass exampleRenderPass;

    private void OnEnable()
    {
        // Create the custom render pass
        exampleRenderPass = new ExampleRenderPass(settings);
    }
}

```

For more information about writing a render pass, refer to [Write a render pass using the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-write-render-pass.html).
  2. Subscribe a method to one of the events in the `RenderPipelineManager` API. For example:
```
    private void OnEnable()
    {
        ...
        // Call the InjectRenderPass method when the beginCameraRendering event is raised.
        RenderPipelineManager.beginCameraRendering += InjectRenderPass;            
    }

```

  3. In the subscribed method, use the [`EnqueuePass`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.2/api/UnityEngine.Rendering.Universal.ScriptableRenderer.html#UnityEngine_Rendering_Universal_ScriptableRenderer_EnqueuePass_UnityEngine_Rendering_Universal_ScriptableRenderPass) API method to inject a custom render pass into the URP rendering loop.
```
public class InjectPass : MonoBehaviour
{
    ...

    // Add the method that Unity calls after the beginCameraRendering event is raised.
    // The method must accept the ScriptableRenderContext and Camera parameters the event delegate defines.
    private void InjectRenderPass(ScriptableRenderContext context, Camera cam)
    {
        ...
        // Use the EnqueuePass API to inject the custom render pass.
        cam.GetUniversalAdditionalCameraData().scriptableRenderer.EnqueuePass(exampleRenderPass);
    }
}

```

  4. Unsubscribe from the event in the `OnDisable` method. For example:
```
public class InjectPass : MonoBehaviour
{
    ...

    private void OnDisable()
    {
        RenderPipelineManager.beginCameraRendering -= InjectRenderPass;
    }
}

```



## Additional resources
  * [Write a render pass using the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-write-render-pass.html)
  * [Custom render pass workflow](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
Scriptable Renderer Feature API reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/restrict-render-pass-scene-area.html)
Restrict a render pass to a scene area in URP
