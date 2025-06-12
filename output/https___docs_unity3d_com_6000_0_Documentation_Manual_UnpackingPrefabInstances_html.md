* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UnpackingPrefabInstances.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * Unpacking Prefab instances


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnusedOverrides.html)
Unused overrides
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html)
Instantiating prefabs at runtime
# Unpacking Prefab instances
To return the contents of a **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) instance into a regular **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), you unpack the Prefab instance. This is exactly the reverse operation of creating (packing) a Prefab, except that it doesn’t destroy the Prefab Asset but only affects the Prefab instance.
You can unpack a Prefab instance by right-clicking on it in the Hierarchy and selecting **Unpack Prefab**. The resulting GameObject in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) no longer has any link to its former Prefab Asset. The Prefab Asset itself is not affected by this operation and there may still be other instances of it in your Project.
If you had any overrides on your Prefab instance before you unpacked it, those will be “baked” onto the resulting GameObjects. That is, the values will stay the same, but will no longer have status as overrides, since there’s no Prefab to override.
If you unpack a Prefab that has nested Prefabs inside, the nested Prefabs remain Prefab instances and still have links to their respective Prefab Assets. Similarly, if you unpack a Prefab Variant, there will be a new Prefab instance at the root which is an instance of the base Prefab.
In general, unpacking a Prefab instance will give you the same objects you see if you go into Prefab Mode for that Prefab. This is because Prefab Mode shows the contents that is inside of a Prefab, and unpacking a Prefab instance unpacks the contents of a Prefab.
If you have a Prefab instance that you want to replace with plain GameObjects and completely remove all links to any Prefab Assets, you can right-click on it in the Hierarchy and select **Unpack Prefab Completely**. This is equivalent to unpacking the Prefab, and keeping on unpacking any Prefab instances that appear as a result because they were nested Prefabs or base Prefabs.
You can unpack Prefab instances that exist in Scenes, or which exist inside other Prefabs.
* * *
  * 2018–07–31 Page published 
  * Nested Prefabs and Prefab Variants added in 2018.3


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnusedOverrides.html)
Unused overrides
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html)
Instantiating prefabs at runtime
