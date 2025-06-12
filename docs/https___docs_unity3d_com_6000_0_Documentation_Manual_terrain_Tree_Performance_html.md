* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Performance.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html)
  * Performance tips for trees


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html)
Create trees and leaves from meshes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Hierarchy-UI.html)
Tree Hierarchy view UI reference
# Performance tips for trees
To improve the performance of trees:
  * Performance depends on the polygon count of your tree model. Test your trees on your platform, and create simpler trees if performance is low.
  * Don’t create too many leaves and branches, because this can reduce performance.
  * Each **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) tile has settings for tree drawing, such as the distance from the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) where trees switch to **billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) mode. These settings can impact the gaming experience when they create transitions that are visible to the player. Refer to the [Terrain Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html) for more information.


## Additional resources
  * [Tree level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-LOD.html)
  * [Shaders and the Ambient-Occlusion folder](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Mat-Shaders.html)
  * [Tree Hierarchy view UI reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Hierarchy-UI.html)
  * [Root node reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Root-Node.html)
  * [Branch group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Branches.html)
  * [Leaf group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Leaves.html)
  * [Terrain Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html)
Create trees and leaves from meshes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Hierarchy-UI.html)
Tree Hierarchy view UI reference
