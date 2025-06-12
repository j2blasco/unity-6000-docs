* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Structure.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html)
  * Tree Editor concepts


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html)
Create trees with Tree Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Mat-Shaders.html)
Shaders and the Ambient-Occlusion folder
# Tree Editor concepts
The Tree Editor tool lets you create trees directly within the Unity Editor. Use the Tree Editor to create new trees, then use the **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) system to add the trees to your world.
For most uses, the SpeedTree Modeler replaces the Tree Editor. For backward compatibility with content created before SpeedTree was introduced, use Tree Editor.
## The Tree Hierarchy view
To open the **Tree Hierarchy** view, add a Tree GameObject (**GameObject** > **3D Object** > **Tree**).
At the top of the tree’s **Inspector** is the **Tree Hierarchy** view, which shows the tree root node and any branch and leaf groups the tree has. Use the **Tree Hierarchy** view to add and delete branch and leaf groups, to control their properties, and to configure the tree.
![Tree Hierarchy view. The first level is the tree root node. Above it is a branch group, which is connected to the tree root node with a line. There are four tree editing options on the right, and a recompute button on the left.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeStructure.png) Tree Hierarchy view. The first level is the tree root node. Above it is a branch group, which is connected to the tree root node with a line. There are four tree editing options on the right, and a recompute button on the left.
For more information about the Tree Hierarchy view, refer to the [Tree Hierarchy view UI reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Hierarchy-UI.html).
## Tree levels and groups
The Tree Editor manages branches and leaves in groups, and arranges the groups in levels. 
The tree root doesn’t count as one of the levels, so the first level is the trunk. Branches growing directly from the trunk are the primary level. Branches growing from the primary branches are the secondary level. The branching process continues until the terminal twigs, adding a level each time. 
![A diagram showing tree levels: the first level is the trunk. It has six primary branches. Each of those branches has four secondary branches.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeStructureDiagram.png) A diagram showing tree levels: the first level is the trunk. It has six primary branches. Each of those branches has four secondary branches.
A branch group can subdivide into further branch groups. For example, you can add two branch groups to your trunk, and give each branch group a different growth angle or its own leaf group.
Leaves are also arranged in groups. Unlike branch groups, leaf groups can’t further subdivide: you can’t add a leaf or branch group to a leaf group.
For more information about working with branch and leaf groups, refer to [Design a tree](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-FirstTree.html). For more information about the Tree Hierarchy view, refer to the [Tree Hierarchy view UI reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Hierarchy-UI.html).
## The tree root node
The tree **root node** A transform in an animation hierarchy that allows Unity to establish consistency between Animation clips for a generic model. It also enables Unity to properly blend between Animations that have not been authored “in place” (that is, where the whole Model moves its world position while animating). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rootnode) exposes properties that affect the entire tree. For example, all branch and leaf groups inherit the ****LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) Quality** property from the tree root node, although each branch group can add a multiplier to this value.
For more information about the tree root node, refer to [Root node reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Root-Node.html).
## Tree Materials
Trees can have four materials: 
  * Leaves.
  * Bark.
  * Cross-section of a broken branch.
  * Fronds.


For information about **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) for these materials, refer to [Shaders and the Ambient-Occlusion folder](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Mat-Shaders.html).
## Tree geometry
There are three geometry options for branches:
  * Branch Only.
  * Branch and Fronds.
  * Fronds Only.


Each branch group can have a different geometry option. For example, you can have a branch group with a Branch Only geometry as the trunk, and a branch group with Fronds Only geometry as the branches.
To learn more about fronds, refer to [Branch group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Branches.html).
## Additional resources
  * [Shaders and the Ambient-Occlusion folder](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Mat-Shaders.html)
  * [Performance tips for trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Performance.html)
  * [Tree Hierarchy view UI reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Hierarchy-UI.html)
  * [Root node reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Root-Node.html)
  * [Branch group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Branches.html)
  * [Leaf group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Leaves.html)
  * [Terrain Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html)
  * [Mesh Renderer component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html)
Create trees with Tree Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Mat-Shaders.html)
Shaders and the Ambient-Occlusion folder
