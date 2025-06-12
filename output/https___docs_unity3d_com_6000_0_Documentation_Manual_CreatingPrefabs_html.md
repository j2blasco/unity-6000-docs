* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * Create prefabs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/prefabs-introduction.html)
Introduction to prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingInPrefabMode.html)
Edit prefabs
# Create prefabs
In Unity’s **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) system, **Prefab Assets** act as templates. You create Prefab Assets in the Editor, and they are saved as an Asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow). From **Prefab Assets** , you can create any number of **Prefab instances**. Prefab instances can either be created in the editor and saved as part of your **Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), or instantiated at runtime.
## Creating Prefab Assets
To create a Prefab Asset, drag a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) from the Hierarchy window into the Project window. The GameObject, and all its components and child GameObjects, becomes a new Asset in your Project window. Prefabs Assets in the Project window are shown with a thumbnail view of the GameObject, or the blue cube Prefab icon, depending on how you have set up your Project window.
![Two prefabs \(FatBlob and “Key”\) shown in the Project window in two-column view \(left\) and one-column view \(right\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsInProjectWindow1.png) Two prefabs (“FatBlob” and “Key”) shown in the Project window in two-column view (left) and one-column view (right)
This process of creating the Prefab Asset also turns the original GameObject into a Prefab instance. It is now an instance of the newly created Prefab Asset. Prefab instances are shown in the Hierarchy in blue text, and the root GameObject of the Prefab is shown with the blue cube Prefab icon, instead of the red, green and blue GameObject icon.
![A Prefab instance \(Key\) in the scene](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabInstanceInScene1.png) A Prefab instance (Key) in the scene
## Creating multiple Prefab Assets
To create multiple Prefab Assets at once, drag multiple GameObjects from the Hierarchy window into the Project window. This functionality is the same as in the above paragraph.
If you drag multiple GameObjects that are not already Prefabs into the Project window, Unity creates new original Prefab Assets for each one without any additional steps. 
If any of the GameObjects you drag into the Project Window are existing Prefab variants or Model Variants, Unity displays a dialog box which asks you to confirm whether you want to create new Prefab Assets or new variants from the GameObjects. The content of this dialog box changes depending on the number and type of GameObjects you drag into the Project window.
## Creating Prefab instances
You can create instances of the Prefab Asset in the Editor by dragging the Prefab Asset from the Project view to the Hierarchy or **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView).
![Dragging a Prefab Key into the Scene](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsDragIntoScene1.png) Dragging a Prefab “Key” into the Scene
You can also create instances of Prefabs at runtime using scripting. For more information, see [Instantiating Prefabs](https://docs.unity3d.com/Manual/instantiating-prefabs.html).
## Replacing existing prefabs
You can replace a Prefab by dragging a new GameObject from the Hierarchy window and dropping it on top of an existing Prefab asset in the Project window.
If you are replacing an existing Prefab, Unity tries to preserve references to the Prefab itself and the individual parts of the Prefab such as child GameObjects and Components. To do this, it matches the names of GameObjects between the new Prefab and the existing Prefab that you are replacing.
**Note:** _Because this matching is done by name only, if there are multiple GameObjects with the same name in the Prefab’s hierarchy, it is not possible to predict which will be matched. Therefore if you need to ensure your references are preserved when saving over an existing prefab, you must ensure all GameObjects within the Prefab have unique names._
**Also note:** _You may encounter a similar problem in the case of preserving references to existing Components when you save over an existing Prefab, if a single GameObject within the Prefab has more than one of the same Component type attached. In this case it is not possible to predict which of them will be matched to the existing references._
* * *
  * 2018–07–31 Page published 
  * Nested Prefabs and Prefab Variants added in 2018.3


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/prefabs-introduction.html)
Introduction to prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingInPrefabMode.html)
Edit prefabs
