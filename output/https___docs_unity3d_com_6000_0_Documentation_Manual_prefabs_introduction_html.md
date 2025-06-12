* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/prefabs-introduction.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * Introduction to prefabs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
Prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html)
Create prefabs
# Introduction to prefabs
Prefabs allow you to reuse a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) configured in a particular way, such as a non-player character (NPC), prop or piece of scenery, in multiple places in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), or across multiple scenes in your project. This is better than simply copying and pasting the GameObject, because the **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) system allows you to automatically keep all the copies in sync.
Any edits that you make to a prefab asset are automatically reflected in the instances of that prefab, allowing you to easily make broad changes across your whole project without having to repeatedly make the same edit to every copy of the asset.
You can [nest prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedPrefabs.html) inside other prefabs to create complex hierarchies of objects that are easy to edit at multiple levels. However, this does not mean all prefab instances have to be identical. You can [override](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabInstanceOverrides.html) settings on individual prefab instances if you want some instances of a prefab to differ from others. You can also create [prefab variants](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabVariants.html) to group a set of overrides together into a meaningful variation of a prefab.
You should also use prefabs when you want to [instantiate GameObjects at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html) that did not exist in your scene at the start. For example, to make powerups, special effects, projectiles, or NPCs appear at the right moments during gameplay.
Some common examples of prefab use include:
  * Environmental assets: For example, a certain type of tree used multiple times around a level.
  * Non-player characters (NPCs): For example, a certain type of robot may appear in your game multiple times, across multiple levels. They may differ (using overrides) in the speed they move, or the sound they make.
  * Projectiles: For example, a pirate ship’s cannon might instantiate a cannonball prefab each time it’s fired.
  * The user’s main playable character: The character prefab might be placed at the starting point on each level (separate scenes) of your game.


## Prefab Inspector previews
When you select a prefab and view it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, the Asset Preview pane in the Inspector shows a preview of the prefab. If the size of the prefab is less than 8MB, the Asset Preview pane shows an interactive preview of the prefab, which allows you to rotate the prefab inside the Asset Preview pane. 
If the size of the prefab is greater than 8MB, by default the Asset Preview shows a static preview of the prefab. To view an interactive preview of a prefab that is greater than 8MB, click anywhere inside the Asset Preview pane.
## Additional resources
  * [Creating prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html)
  * [The Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
Prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html)
Create prefabs
