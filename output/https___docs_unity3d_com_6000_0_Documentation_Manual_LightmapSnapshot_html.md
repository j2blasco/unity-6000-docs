* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightmapSnapshot.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Lighting data](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmap-data-landing.html)
  * Lighting Data Assets


[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-precomputed-data.html)
Introduction to lighting data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)
Global Illumination (GI) cache
# Lighting Data Assets
A Lighting Data Asset stores precomputed lighting data for a Scene in the Unity Editor. Lighting Data Assets exist as separate files in your Project for workflow reasons; storing precomputed lighting data in a separate file means that changes to the precomputed lighting data do not result in changes to the Scene file. Lighting Data Assets are not intended for users to edit.
Unity stores precomputed lighting data in a Lighting Data Asset when you invoke a lighting precompute, either by using the **Generate Lighting** button in the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html), or by using the [Lightmapping.Bake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Bake.html) or [Lightmapping.BakeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.BakeAsync.html) APIs.
The Lighting Data Asset contains **global illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) data and all the supporting files needed to recreate the lighting for a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). This asset references the renderers, the real-time **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap), the baked lightmaps, **light probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe), **reflection probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) and a data structure which stores the relationships between these elements. It also includes all the precomputed **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime Global Illumination data needed to update how real-time global illumination looks in the Player.
When you change the scene, for instance by breaking a **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) connection on a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that is marked as **Contribute GI** , the asset data will get out of date and has to be rebuilt.
The intermediate files that are generated during the lighting build process, but is not needed for generating a Player build is not part of the asset, they are stored in the [GI Cache](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)The cached intermediate files used when Unity precomputes lighting data. Unity keeps this cache to speed up computation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GICache) instead.
The build time for the Lighting Data Asset can vary. If your [GI Cache](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html) is fully populated i.e. you have done a bake on the machine before (with the scene in its current state) it will be fast. If you are pulling the scene to a machine with a blank cache or the cache data needed has been removed due to the cache size limit, the cache will have to be populated with the intermediate files first which requires the precompute and bake processes to run. These steps can take some time.
## Default Lighting Data Assets
When you add a new scene, Unity uses a default Lighting Data Asset. The asset references a hidden ambient probe and a hidden Reflection Probe that capture environment lighting from Unity’s built-in Default **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox). The asset doesn’t appear in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow).
The data in the hidden probes is fixed. For example, if you change the **Skybox Material** in the Lighting window, the data in the probes doesn’t change, so environment lighting on objects stays the same.
To stop using the default Lighting Data Asset, select **Generate Lighting** or **Clear Baked Data** in the Lighting window. Unity then creates and uses a new default Lighting Data Asset and a new baked Reflection Probe (the ambient Reflection Probe). These assets appear in the Project window, and update when you select **Generate Lighting**.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-precomputed-data.html)
Introduction to lighting data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)
Global Illumination (GI) cache
