* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-LOD.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Landing.html)
  * Tree level of detail (LOD)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTreeImporter-Materials.html)
Materials tab
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Colliders.html)
Add collision to trees
# Tree level of detail (LOD)
Trees from Tree Editor and trees from SpeedTree handle their level of detail (LOD) differently. 
## SpeedTree
A SpeedTree **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) has an LODGroup component. Refer to [LOD](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) and [LOD Group](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup) for more information about configuring LOD components.
## Tree Editor
Tree Editor trees don’t have an LODGroup component. Unity’s LOD system uses a 2D to 3D transition zone to blend 2D **billboards** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) with 3D tree models. This prevents a sudden popping of 2D and 3D trees, which is important for realism in **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR). 
**Note** : Billboard trees don’t receive local lighting such as Point Lights and Spot Lights. They work with directional lights, but lighting on the billboards updates only when you rotate the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). 
Tree Editor controls LOD at two levels:
  * The tree root node.
  * Individual branch groups, as a multiplier of the tree **root node** A transform in an animation hierarchy that allows Unity to establish consistency between Animation clips for a generic model. It also enables Unity to properly blend between Animations that have not been authored “in place” (that is, where the whole Model moves its world position while animating). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rootnode)’s LOD.


The leaves and bark **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) also have LOD defaults. These are built-in shaders, and you can’t edit them.
Each **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) tile has settings for tree drawing, such as the distance from the camera where trees switch to billboard mode. These settings can impact the gaming experience when they create transitions that are visible to the player. Refer to the [Terrain Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html) for more information.
## Additional resources
  * [Create trees with Tree Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html)
  * [Terrain Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html)
  * [Import trees from SpeedTree](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTree-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTreeImporter-Materials.html)
Materials tab
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Colliders.html)
Add collision to trees
