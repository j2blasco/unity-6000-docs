* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configure-mesh-lod.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html)
  * Configure mesh LOD


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)
Mesh LOD
[](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-lod-meshes.html)
Import a mesh with LOD settings
# Configure mesh LOD
To configure **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD), you must have a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with a [LOD Group](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup) component. The LOD Group component provides controls to define how LOD behaves on this GameObject, and references the GameObjects that Unity shows or hides for each LOD level. See [LOD Group](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html) for details on the properties in this component.
You can set up LOD in Unity two ways:
  * You can configure LOD levels in your external 3D modeling application, and Unity can automatically create and configure the required GameObjects and components for you. See [Importing LOD Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-lod-meshes.html) for details on the correct configuration.
  * You can manually create a GameObject with a LOD Group component, and configure the LOD levels manually.


## Configure LOD levels
To manually configure the distance from the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) at which Unity displays each LOD level, use the [LOD Group component’s selection bar](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#LODGroup).
The LOD Group component accepts a maximum of eight LOD levels. **LOD 0** is the closest to the Camera, and therefore the most detailed LOD level.
## Configure project-wide LOD settings
In the [Quality settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) window, you can configure LOD settings that affect all GameObjects in your Project.
There are two LOD settings you can configure:
  * **Maximum LOD Level** : Exclude meshes above a specified LOD level from your build.
  * **LOD Bias** : Determine whether to favor higher or lower LOD levels at threshold distances.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)
Mesh LOD
[](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-lod-meshes.html)
Import a mesh with LOD settings
