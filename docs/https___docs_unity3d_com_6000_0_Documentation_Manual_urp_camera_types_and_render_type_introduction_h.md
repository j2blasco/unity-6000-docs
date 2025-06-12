* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-introduction.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Camera render types in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type.html)
  * Introduction to camera render types in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type.html)
Camera render types in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-change.html)
Change the render type of a camera in URP
# Introduction to camera render types in URP
There are two types of **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP):
  * A [Base Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-introduction.html#base-camera) is a general purpose Camera that renders to a render target (a screen, or a [Render Texture](https://docs.unity3d.com/Manual/class-RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture)).
  * An [Overlay Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-introduction.html#overlay-camera) renders on top of another Camera’s output. You can combine the output of a Base Camera with the output of one or more Overlay Cameras. This is called [Camera stacking](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html).


## Base Camera
Base Camera is the default type of Camera in URP. A Base Camera is a general purpose Camera that renders to a given render target.
To render anything in URP, you must have at least one Base Camera in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). You can have multiple Base Cameras in a scene. You can use a Base Camera on its own, or you can use it in a [Camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html). For more information on working with multiple Cameras in URP, refer to [Working with multiple cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html).
When you have an active Base Camera in your scene, this icon appears next to the Camera **Gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView):
![Overlay Camera icon](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/camera-icon-base.png) Overlay Camera icon
For information on the properties that Unity exposes in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) for a Base Camera, refer to the [Camera component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html).
## Overlay Camera
An Overlay Camera is a Camera that renders its view on top of another Camera’s output. You can use Overlay Cameras to create effects such as **3D objects** A 3D GameObject such as a cube, terrain or ragdoll. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#3DObject) in a 2D UI, or a cockpit in a vehicle.
You must use Overlay Cameras in conjunction with one or more Base Cameras using the [Camera Stacking](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html) system. You cannot use Overlay Cameras on their own. An Overlay Camera that is not part of a Camera Stack does not perform any steps of its render loop, and is known as an orphan Camera.
**Note:** In this version of URP, Overlay Cameras and Camera Stacking are supported only when using the Universal Renderer.
When you have an active Overlay Camera in your scene, this icon appears next to the Camera Gizmo in the Scene view:
![Overlay Camera icon](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/camera-icon-overlay.png) Overlay Camera icon
The Base Camera in a Camera Stack determines most of the properties of the Camera Stack. Because you can only use Overlay Cameras in a Camera Stack, URP uses only the following properties of an Overlay Camera when rendering the scene:
  * Projection
  * FOV Axis
  * Field of View
  * Physical Camera properties
  * Clipping planes
  * Renderer
  * Clear Depth
  * Render Shadows
  * Culling Mask
  * Occlusion Culling


Unity hides all of the other unused properties in the Inspector. You can access unused properties using a script, but any changes you make to these unused properties will not affect the visual output of any Camera Stacks that use the Overlay Camera.
**Note:** While you can apply **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) to an individual Overlay Camera within a camera stack, the effects also apply to all the outputs the camera stack renders before the Overlay Camera. This is different to how you can apply post-processing to an individual Base Camera where the effects on only apply to the Base Camera.
For information on the properties that Unity exposes in the Inspector of an Overlay Camera, refer to the [Camera component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type.html)
Camera render types in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-change.html)
Change the render type of a camera in URP
