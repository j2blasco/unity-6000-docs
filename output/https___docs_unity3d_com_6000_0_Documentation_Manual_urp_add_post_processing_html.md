* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/add-post-processing.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * Add post-processing in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html)
Introduction to post-processing in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/volumes-landing-page.html)
Volumes in URP
# Add post-processing in URP
New scenes in URP do not use **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) by default. Instead you must manually add post-processing to any new **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) which you create. You can then configure each effect individually to create the visual effect you want.
**Note** : Some examples and scene templates in URP use post-processing by default. If you use these to create a new scene, you might not need to make any changes.
## Add post-processing to a scene
To add post-processing to a scene:
  1. Select a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), then in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window enable **Post Processing**.
  2. Add a GameObject with a [Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volumes.html) component in the scene. For example, select **GameObject** > **Volume** > **Global Volume**.
  3. Select the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), then in the **Volume** component select **New** to create a new [Volume Profile](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html).
  4. Select **Add Override** , then select a post-processing effect [Volume Override](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/VolumeOverrides.html), for example **Bloom**.


Now you can use the Volume Override to enable and adjust the settings for the post-processing effect.
**Note** : Post-processing effects from a volume apply to a camera only if a value in the **Volume Mask** property of the camera contains the layer that the volume belongs to.
## Configure individual post-processing effects
Each post-processing effect in URP has individual settings you can adjust to tune the visual impact they have on your scene. For more information on the post-processing effect settings, refer to the reference pages in the [Effect List](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html)
Introduction to post-processing in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/volumes-landing-page.html)
Volumes in URP
