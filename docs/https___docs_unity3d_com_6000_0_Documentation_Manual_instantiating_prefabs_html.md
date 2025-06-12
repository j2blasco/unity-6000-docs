* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * Instantiating prefabs at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnpackingPrefabInstances.html)
Unpacking Prefab instances
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-intro.html)
Introduction to instantiating prefabs
# Instantiating prefabs at runtime
[Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) are useful when you want to instantiate complicated **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) or collections of GameObjects at runtime. Compared with creating GameObjects from scratch using code, instantiating prefabs using code has many advantages because you can:
  * Instantiate a prefab using one line of code. Creating equivalent GameObjects from scratch requires many more lines of code.
  * Set up, test, and modify the prefab quickly and easily using the ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view**, **Hierarchy** , and ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** windows.
  * Change which prefab is instantiated without changing the code. You can make a simple rocket into a super-charged rocket, without any code changes.


**Note** : You can download a Unity Project containing all the examples in this section here:
**[InstantiatingPrefabsExamples.zip](https://docs.unity3d.com/6000.0/Documentation/uploads/Examples/InstantiatingPrefabsExamples.zip)**
**Topic** | **Description**  
---|---  
[Introduction to instantiating prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-intro.html) | Introductory context and common scenarios in which instantiating prefabs is useful.  
[Build a structure with prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-structure.html) | Use prefabs to instantiate several copies of a block prefab to construct a wall.  
[Instantiating projectiles and explosions](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-projectiles.html) | Use prefabs to instantiate exploding projectiles.  
[Replace a character with a ragdoll or wreck](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-wrecks.html) | Use prefabs to replace an intact version of an object with a wreck to visualize object destruction.  
## Additional resources
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * [Introduction to GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnpackingPrefabInstances.html)
Unpacking Prefab instances
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-intro.html)
Introduction to instantiating prefabs
