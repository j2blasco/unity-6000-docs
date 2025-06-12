* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)
  * Add GameObjects to reflections


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingReflectionProbes.html)
Place a Reflection Probe
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects-use.html)
Set GameObjects to use Reflection Probes
# Add GameObjects to reflections
## Add GameObjects to baked Reflection Probes
The reflections captured by baked probes can only include **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) objects marked as ****Reflection Probe** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) Static** (using the **Static** menu at the top left of the inspector panel for all objects). You can further refine the objects that get included in the reflection **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) using the ****Culling Mask** Allows you to include or omit objects to be rendered by a Camera, by Layer.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CullingMask)** and ****Clipping Planes** A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#clippingplane)** properties, which work the same way as for a [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) (the probe is essentially like a camera that is rotated to view each of the six cubemap faces).
## Add GameObjects to realtime Reflection Probes
You don’t need to mark objects as **Reflection Probe Static** to capture their reflections (as you would with a baked probe). However, you can selectively exclude objects from the reflection cubemap using the **Culling Mask** and **Clipping Planes** properties, which work the same way as for a [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html) (the probe is essentially like a camera that is rotated to view each of the six cubemap faces).
## Update Reflection Probes
To update probes, do one of the following:
  * In a probe’s ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window, select **Bake**.
  * In the Lighting window, select **Generate Lighting**. This updates all probes.


The bake process will take place asynchronously while you continue to work in the editor. If you move any static objects, change their materials or otherwise alter their visual appearance during the baking process, you must rebake to see the updated results.
**Note** : Currently, real-time probes will only update their reflections in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) when **Reflection Probe Static** objects are moved or change their appearance. This means that moving dynamic objects won’t cause an update even though those objects appear in the reflection. You should choose the **Bake Reflection Probes** option from the **Generate Lighting** button dropdown in the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html) to update reflections when a dynamic object is changed.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingReflectionProbes.html)
Place a Reflection Probe
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects-use.html)
Set GameObjects to use Reflection Probes
