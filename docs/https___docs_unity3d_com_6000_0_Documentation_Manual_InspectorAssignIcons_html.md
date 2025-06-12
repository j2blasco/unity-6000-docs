* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorAssignIcons.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)
  * Assign icons to inspected items


[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorFocused.html)
Focused Inspectors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorManageComponents.html)
Manage components and their values
# Assign icons to inspected items
Use the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window to assign an icon to the item you’re inspecting. The icon appears in the ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)** view, making it easier to identify the item.
The icon’s behavior in the [Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) depends on the item type:
  * **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject): The icon appears over that GameObject, and any duplicates.
  * **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab): The icon appears over any instances of that prefab.
  * Script: The icon appears over any GameObject that has the script attached.


To control how Unity draws custom icons in the **Scene** view, use the [Gizmos menu](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html).
**Note:** When you change an asset’s icon, Unity marks the asset as modified, and **version control** A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VersionControl) systems register the change.
### Icon types
The Unity Editor supports three icons types.
**Icon type** | **Description**  
---|---  
**Label icons** | Colored capsules that show the item’s name.  
**Image only icons** | Colored circles. They’re useful for objects that don’t have a visual representation such as waypoints.  
**Custom icons** (other) | An icon based on an asset in the project. For example, use a skull and crossbones icon to indicate danger areas in a game level.  
## Manage icons in the **Inspector** window
To add icons, in the **Inspector** window, select **Select icon**. Then:
  * To assign an icon to a GameObject or a script, do one of the following: 
    * To assign a label or image icon, click any icon from the list.
    * To assign a custom icon, select **Other…** and select a texture.
  * To assign an icon to a prefab, open the prefab in [Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingInPrefabMode.html).


To replace or remove icons, in the **Inspector** window, select **Select icon**. Then:
  * To replace the icon, select any other icon from the list.
  * To remove the icon, select **None**. The item’s icon reverts to the default Unity icon.


## Additional resources
  * [Using the Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * [Gizmos menu](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html)
  * [Editing in Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingInPrefabMode.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorFocused.html)
Focused Inspectors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorManageComponents.html)
Manage components and their values
