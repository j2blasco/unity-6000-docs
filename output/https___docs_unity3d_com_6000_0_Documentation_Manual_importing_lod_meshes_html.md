* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/importing-lod-meshes.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html)
  * Import a mesh with LOD settings


[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-mesh-lod.html)
Configure mesh LOD
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)
LOD Group component reference
# Import a mesh with LOD settings
You can create meshes with different levels of detail in an external 3D application for use with Unity’s [LOD system](https://docs.unity3d.com/Manual/LevelOfDetail.html). If you name these meshes correctly, Unity automatically creates and configures a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with [LOD group](https://docs.unity3d.com/Manual/class-LODGroup.html)A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup) component for them when it imports the Model.
To import a Model with **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) level into Unity, you must do the following:
  1. In your external 3D application, follow the application’s process to create as many LOD meshes as you need.
  2. Name the meshes according to the following naming convention: 
     * ExampleMeshName_LOD0 for the first LOD level (i.e., the most detailed version)
     * ExampleMeshName_LOD1
     * ExampleMeshName_LOD2
  3. Export your Model as an FBX file. Alternatively, if you are using Maya, export the mesh group directly into Unity; to do this, go to **File > Send to Unity > Selection.**
  4. Import the FBX into Unity. Unity recognizes the grouped Meshes and naming convention, and automatically creates an[ LOD Group](https://docs.unity3d.com/Manual/class-LODGroup.html) component with the appropriate settings.


## Additional resources
  * To learn more about importing models, see [Importing models](https://docs.unity3d.com/Manual/ImportingModelFiles.html).
  * To learn more about creating and exporting LOD Meshes in Maya, follow the Unity tutorial [Creating LODs in Maya](https://learn.unity.com/tutorial/creating-lods-in-maya-for-unity).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-mesh-lod.html)
Configure mesh LOD
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)
LOD Group component reference
