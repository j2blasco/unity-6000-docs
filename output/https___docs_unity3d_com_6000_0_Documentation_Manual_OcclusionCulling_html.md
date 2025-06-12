* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Excluding hidden objects with occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
  * Occlusion culling


[](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
Excluding hidden objects with occlusion culling
[](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-getting-started.html)
Set up a scene for occlusion culling
# Occlusion culling
Occlusion culling is a process which prevents Unity from performing rendering calculations for **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that are completely hidden from view (occluded) by other GameObjects.
Every frame, **Cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) perform culling operations that examine the Renderers in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and exclude (cull) those that do not need to be drawn. By default, Cameras perform [frustum culling](https://docs.unity3d.com/6000.0/Documentation/Manual/UnderstandingFrustum.html), which excludes all Renderers that do not fall within the Camera’s view frustum. However, frustum culling does not check whether a Renderer is occluded by other GameObjects, and so Unity can still waste CPU and GPU time on rendering operations for Renderers that are not visible in the final frame. **Occlusion culling** stops Unity from performing these wasted operations.
![Regular frustum culling renders all Renderers within the Cameras view.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/OcclusionFrustumCulling.jpg) Regular frustum culling renders all Renderers within the Camera’s view. ![Occlusion culling removes Renderers that are entirely obscured by nearer Renderers.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/OcclusionFullCulling.jpg) Occlusion culling removes Renderers that are entirely obscured by nearer Renderers.
## When to use occlusion culling
To determine whether occlusion culling is likely to improve the runtime performance of your Project, consider the following:
  * Preventing wasted rendering operations can save on both CPU and GPU time. Unity’s built-in occlusion culling performs runtime calculations on the CPU, which can offset the CPU time that it saves. Occlusion culling is therefore most likely to result in performance improvements when a Project is GPU-bound due to overdraw.
  * Unity loads occlusion culling data into memory at runtime. You must ensure that you have sufficient memory to load this data.
  * Occlusion culling works best in Scenes where small, well-defined areas are clearly separated from one another by solid GameObjects. A common example is rooms connected by corridors.
  * You can use occlusion culling to occlude Dynamic GameObjects, but Dynamic GameObjects cannot occlude other GameObjects. If your Project generates Scene geometry at runtime, then Unity’s built-in occlusion culling is not suitable for your Project.


## How occlusion culling works
Occlusion culling generates data about your Scene in the Unity Editor, and then uses that data at runtime to determine what a Camera can see. The process of generating data is known as baking.
When you bake occlusion culling data, Unity divides the Scene into cells and generates data that describes the geometry within cells, and the visibility between adjacent cells. Unity then merges cells where possible, to reduce the size of the generated data. To configure the baking process, you can change parameters in the [Occlusion Culling window](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-window.html), and use [Occlusion Areas](https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionArea.html) in your Scene.
At runtime, Unity loads this baked data into memory, and for each Camera that has its Occlusion Culling property enabled, it performs queries against the data to determine what that Camera can see. Note that when occlusion culling is enabled, Cameras perform both frustum culling and occlusion culling.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
Excluding hidden objects with occlusion culling
[](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-getting-started.html)
Set up a scene for occlusion culling
