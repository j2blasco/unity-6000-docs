* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * Multiple cameras in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-change.html)
Change the render type of a camera in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/camera-stacking-concepts.html)
Camera stacking in URP
# Multiple cameras in URP
![An example of the effect camera stacking can produce in URP](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/camera-stacking-example.png) An example of the effect camera stacking can produce in URP
Resources and approaches for using multiple cameras to work with multiple **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) outputs and targets in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP).
**Note:** If you use multiple cameras, it might make rendering slower. An active camera runs through the entire rendering loop even if it renders nothing.
Page | Description  
---|---  
[Camera stacking](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/camera-stacking-concepts.html) | Learn about the fundamental concepts of camera stacking.  
[Set up a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html) | Stack cameras to layer the outputs of multiple cameras into a single combined output.  
[Add and remove cameras in a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html) | Add, remove, and reorder cameras within a camera stack.  
[Set up split-screen rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-to-the-same-render-target.html) | Render multiple camera outputs to a single render target to create effects such as split screen rendering.  
[Apply different post processing effects to separate cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/apply-different-post-proc-to-cameras.html) | Apply different **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) setups to individual cameas within a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).  
[Render a camera’s output to a Render Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-to-a-render-texture.html) | Render to a **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) to create effects such as in-game CCTV monitors.  
[Create a render request](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/User-Render-Requests.html) | Trigger a camera to render to a Render Texture outside of URP rendering loop.  
## Additional resources
  * [Multiple cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras-landing.html)
  * [Camera render types in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type.html)
  * [Camera render order in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-advanced.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-change.html)
Change the render type of a camera in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/camera-stacking-concepts.html)
Camera stacking in URP
