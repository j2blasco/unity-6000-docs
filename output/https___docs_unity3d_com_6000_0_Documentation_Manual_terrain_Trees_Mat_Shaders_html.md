* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Mat-Shaders.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html)
  * Shaders and the Ambient-Occlusion folder


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Structure.html)
Tree Editor concepts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-FirstTree.html)
Design a tree
# Shaders and the Ambient-Occlusion folder
Trees you create using Tree Editor must use the **Nature/Soft Occlusion Leaves** and **Nature/Soft Occlusion Bark** **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). 
To use these shaders, you must place your trees in a folder named `Ambient-Occlusion`. The trees don’t render correctly if the shaders are in a different folder.
To place trees in the `Ambient-Occlusion` folder:
  1. In the **Project** window, select the `Assets` folder.
  2. Select **Add** (+) > **Folder**.
  3. Give the folder the name `Ambient-Occlusion`.
  4. Move the tree **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) (`Tree.prefab`) and its texture folder (`Tree_Textures`) into the `Ambient-Occlusion` folder. These objects were created when you added a Tree **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).


**Note** : The dependency on these shaders means you can only use Tree Editor trees with the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline). If you’re using the Universal Render Pipeline (URP) or High Definition Render Pipeline (HDRP), you can import trees from [SpeedTree](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTree-landing.html).
## Additional resources
  * [Tree level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-LOD.html)
  * [Tree Hierarchy view UI reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Hierarchy-UI.html)
  * [Root node reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Root-Node.html)
  * [Branch group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Branches.html)
  * [Leaf group reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Leaves.html)
  * [Terrain Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Structure.html)
Tree Editor concepts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-FirstTree.html)
Design a tree
