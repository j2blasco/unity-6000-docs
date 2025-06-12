* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tree-FirstTree.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html)
  * Design a tree


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Mat-Shaders.html)
Shaders and the Ambient-Occlusion folder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html)
Create trees and leaves from meshes
# Design a tree
Design a tree in the Tree Editor, create its materials, and add **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider).
If you want to use an imported **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), refer to [Create trees and leaves from meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html).
## Add a new tree
To create a new **Tree** asset, from the main menu, select **GameObject** > **3D Object** > **Tree**.
This action adds a tree to your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view. It also adds a tree **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) (`Tree.prefab`) and a texture folder (`Tree_Textures`) in the `Assets` folder of your **Project** window.
## Place the tree in the Ambient-Occlusion folder
Trees can render correctly only when placed in a folder called `Ambient-Occlusion`.
  1. In the **Project** window, select the `Assets` folder.
  2. Select **Add** (+) > **Folder**.
  3. Give the folder the name `Ambient-Occlusion`.
  4. Move the tree prefab and its texture folder into the `Ambient-Occlusion` folder.


## Add branches and leaves
The first branch functions as the trunk - it starts on the ground and grows upwards. This example creates a single trunk, but you can create multiple trunks, for example for a group of reeds (refer to the Frequency property in the [Branch group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Branches.html)). 
![A new tree, showing only the first branch, which functions as the tree trunk.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeCreator-BasicBranch.png) A new tree, showing only the first branch, which functions as the tree trunk.
### Available group actions
Select the tree to view it in the **Inspector** window. The **Tree Hierarchy** view shows the root node and the branch group that functions as the trunk. To learn more, refer to [Tree Editor concepts](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Structure.html).
Use the **Tree Hierarchy** view controls to manage branch and leaf groups:
  * **Add Leaf Group**. You can add a leaf group to the tree **root node** A transform in an animation hierarchy that allows Unity to establish consistency between Animation clips for a generic model. It also enables Unity to properly blend between Animations that have not been authored “in place” (that is, where the whole Model moves its world position while animating). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rootnode) or any branch group, but not to another leaf group. The leaf group is always one level above the branch group to which you added it.
  * **Add Branch Group**. You can add a branch group to the tree root node or another branch group, but not to a leaf group. The branch group is always one level above the branch group to which you added it.
  * **Duplicate Selected Group**. Create a copy of the group, with the same settings and at the same level.
  * **Delete Selected Group**. Note that if you delete a group that has subgroups, the subgroups are also deleted.

![Four options for managing branches and leaves. From left to right: Add Leaf Group, Add Branch Group, Duplicate Selected Group, and Delete Selected Group.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeGroupTools.png) Four options for managing branches and leaves. From left to right: Add Leaf Group, Add Branch Group, Duplicate Selected Group, and Delete Selected Group.
### Add branches
Branches are managed in groups. To add branches to the tree trunk, in the **Tree Hierarchy** view, select the existing branch group (the trunk) and click **Add Branch Group**.
A new branch group has only one branch. To add more branches, in the **Inspector** window > **Tree Hierarchy** view, select the new branch group and change its **Frequency** setting.
![A tree trunk with a single branch group.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeCreator-AddingBranches1.png) A tree trunk with a single branch group.
To add smaller branches to the existing branches, select the branch group you just added (not the trunk) and click **Add Branch Group**. The new branch group is added at a level above the selected branch group. Change the new group’s frequency to add more branches. 
**Note** : The frequency isn’t always the final number of branches. The number of branches in the first group does equal its frequency, because those branches all grow out of a single branch (the trunk). In this new group, however, the branches grow from all the branches in the previous group, and so their frequency is distributed. To create a natural look, the growth isn’t uniform, meaning the distribution isn’t even. As a result, the final number of branches in the second group isn’t a simple product of the two frequencies. 
![The tree has two branch groups, one growing from the trunk and one growing from the first branch group. The Tree Hierarchy view shows both branch groups, the trunk, and the root node.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeCreator-AddingBranches2.png) The tree has two branch groups, one growing from the trunk and one growing from the first branch group. The Tree Hierarchy view shows both branch groups, the trunk, and the root node.
A new branch group’s growth angle is parallel to the ground. To change the angle, select the branch group and adjust its **Growth Angle** setting. You can also change its **Seek Sun** setting to make the branches bend upwards or downwards.
For more branch group settings and to learn about fronds, refer to [Branch group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Branches.html).
### Add leaves
You can add leaves to any branch group, including the trunk. You can also add leaves to the tree root node, which gives the effect of leaves scattered on the ground. Like branches, leaves are managed in groups.
To add leaves to a branch group, select the branch group and click **Add Leaf Group**.
![The tree has leaves growing from both branch groups, but not the trunk or root node. The Tree Hierarchy view shows one leaf group attached to each branch group.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeCreator-AddingLeaves.png) The tree has leaves growing from both branch groups, but not the trunk or root node. The Tree Hierarchy view shows one leaf group attached to each branch group.
Leaves are added as an opaque plane. Change the group settings until you like the leaves’ appearance before adding materials. For more information, refer to [Leaf group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Leaves.html).
### Add fruit
You can use the leaf group to add fruit. Refer to [Create trees and leaves from meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html) for more information.
To create fruit and leaves that overlap, add two leaf groups at the same level, and give them the same frequency and distribution.
## Add materials
Trees have four materials: for the leaves, the fronds, the bark, and the cross-section visible on broken branches.
### Create a material
To create a material:
  1. From the main menu, select **Assets** > **Create** > **Material**.
  2. Name the material.
  3. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window, select the ****Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader)** drop-down and choose either: 
     * For leaves: **Nature** > **Tree Creator Leaves**.
     * For bark (trunk and branches): **Nature** > **Tree Creator Bark**.
Tree Editor trees and leaves must use these shaders. You can’t use your own shaders.
  4. Add textures. If you don’t have textures yet, you can rely on the **Main color** selection for testing, or download assets from the [Unity Asset Store](https://assetstore.unity.com/).
To learn more about textures, refer to [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture).

![The Inspector window showing a new leaf material and its textures. The shader is Nature/Tree Creator Leaves.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeCreator-LeavesMaterial.png) The Inspector window showing a new leaf material and its textures. The shader is Nature/Tree Creator Leaves.
### Add a material to the tree
To add a material to a group, select the group in the **Tree Hierarchy** view and assign the material in its **Geometry** section:
  * Leaves have only one material.
  * Branches have two materials: **Branch Material** for the bark of the branch, and **Break Material** for the cross-section of a broken branch.

![A close up of a tree showing the branch material and the break material.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeCreator-material-closeup.png) A close up of a tree showing the branch material and the break material.
## Transform individual branches and leaves
GameObject transforms work only on the tree as a whole and are available when you select the tree root node. 
To transform individual branches and leaves, use the tree creator’s control points.
**Tip** : To [transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) the entire tree, click the **Tree Root Node** button.
### Display the branch or leaf control points
When you select a branch group in the **Tree Hierarchy** view, the Unity Editor selects its branches in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView). The branch or leaf group in the Scene view includes control points, which you can use to edit the branch or leaf. The following example shows a tree with a single branch selected.
![A single tree branch, the trunk, showing multiple control points along its length.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeWithControlPoints01.png) A single tree branch, the trunk, showing multiple control points along its length.
The control options are available from a **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) below the **Tree Hierarchy** view.
![The toolbar showing the three branch control options. From left to right: Move, Rotate, and Free Hand](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeHandEditTools.png) The toolbar showing the three branch control options. From left to right: Move, Rotate, and Free Hand
### Transform branches
The control points of the branches pass through the center line of each branch. You can click and drag any of the control points to move the branch.
For a branch, the control options are:
  * **Move Branch** : Move a point on the branch. The rest of the branch remains in place, so the branch bends around the control point.
  * **Rotate Branch** : Rotate the branch around the control point. The movement is only from the part of the branch above the control point.
  * **Free Hand** : Draw a branch as a spline. Click and drag from the highest control point to add a part of the branch. Click on a lower control point to trim the branch down to that point.

![One of the control points on the tree trunk is to the side of the center line, creating a curving trunk](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TreeWithControlPoints02.png) One of the control points on the tree trunk is to the side of the center line, creating a curving trunk
### Transform leaves
For leaves, the control options are:
  * **Move Leaf** : Move a leaf up or down a branch. You can’t move a leaf to another branch.
  * **Rotate Leaf** : Click the point at the center of the leaf and drag it to rotate the leaf around its axis.


### Impact on procedural properties
Some branch and leaf properties are procedural, meaning that the Tree Editor generates them. When you edit a branch or leaf, the Tree Editor disables the procedural properties. 
To restore the procedural properties, click **Convert to Procedural Group**. This removes any edits you made by hand.
## Add a collider
Colliders define the shape of an object. They calculate physical **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) so that a character can’t walk through a tree, for example. Trees use the ****Capsule Collider** A capsule-shaped collider component that handles collisions for GameObjects like barrels and character limbs. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#capsulecollider)** component.
To learn more about tree colliders, refer to [Add collision to trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Colliders.html).
## Add wind
Wind Zones animate tree movements. 
To add a **Wind Zone** A GameObject that adds the effect of wind to your terrain. For instance, Trees within a wind zone will bend in a realistic animated fashion and the wind itself will move in pulses to create natural patterns of movement among the tree. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#windzone) **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), in the tree’s **Inspector** window, click **Create Wind Zone**. You can do this from any branch or leaf group, but not from the tree root node.
The Wind Zone’s default settings create a gentle breeze, and you can use it for your trees without changing it. If you want to create a stronger wind effect, refer to [Animate trees with Wind Zones](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html).
## Hide the tree
The tree is now ready to be painted onto the **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) in groups. It’s a good idea to make the tree GameObject invisible so that you don’t accidentally move it or change its settings. 
Select the tree GameObject in the **Hierarchy** window, and in the **Inspector** window, disable the **Visibility** checkbox next to the GameObject’s name.
## Add the tree to the terrain
Use the Paint Trees tool to add clumps of your tree to the terrain. Refer to [Add trees to the terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees.html) for more information.
## Additional resources
  * [Create trees and leaves from meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html)
  * [Shaders and the Ambient-Occlusion folder](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Mat-Shaders.html)
  * [Root node reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Root-Node.html)
  * [Branch group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Branches.html)
  * [Leaf group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Leaves.html)
  * [Tree Editor concepts](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Structure.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Mat-Shaders.html)
Shaders and the Ambient-Occlusion folder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html)
Create trees and leaves from meshes
