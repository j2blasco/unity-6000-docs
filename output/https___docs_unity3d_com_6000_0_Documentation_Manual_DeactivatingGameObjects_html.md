* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/DeactivatingGameObjects.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [GameObject fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/gameobject-fundamentals.html)
  * Deactivate GameObjects


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html)
Static GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)
Primitive and placeholder objects
# Deactivate GameObjects
To temporarily remove a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) from your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), you can mark the GameObject as inactive. 
To do this, navigate to the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window and clear the checkbox to the left of the GameObject’s name. The names of deactivated GameObjects appear faded in the Hierarchy window.
To deactivate a GameObject through script, use the [SetActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SetActive.html) method. To see if an object is active or inactive, check the [activeSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeSelf.html) property.
If you deactivate a GameObject, coroutines attached to it are stopped. 
## Deactivate a parent GameObject
If you deactivate a parent GameObject, you also deactivate all of its child GameObjects because the deactivation overrides the `activeSelf` setting on all child GameObjects. The child GameObjects return to their original state when you reactivate the parent.
To know if a child GameObject is active in your scene, use the [activeInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeInHierarchy.html) property.
**Note:** The `activeSelf` property is not always accurate if you check a child GameObject because even if it is set to active, you might have set one of its parent GameObjects to inactive.
![The selected GameObject \(Cube\) is set as active, but remains inactive until you set its parent GameObject to active.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/deactivating2.png) The selected GameObject (Cube) is set as active, but remains inactive until you set its parent GameObject to active.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html)
Static GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)
Primitive and placeholder objects
