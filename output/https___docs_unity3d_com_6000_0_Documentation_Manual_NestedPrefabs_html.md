* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/NestedPrefabs.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * Nested prefabs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingPrefabViaInstance.html)
Edit a prefab via its instances
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabVariants.html)
Prefab variants
# Nested prefabs
You can include **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) instances inside other Prefabs. This is called **nesting** Prefabs. Nested Prefabs retain their links to their own Prefab Assets, while also forming part of another Prefab Asset.
## Adding a nested Prefab in Prefab Mode
In Prefab Mode, you can add and work with Prefab instances just like you would do in Scenes. You can drag a Prefab Asset from the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) to the Hierarchy window or **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view to create a Prefab instance from that Asset inside the Prefab you have open.
**Note** : The root **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) of the Prefab that is open in Prefab Mode is not shown with the blue cube Prefab icon, however any instances of other Prefabs are. You can also add overrides to these Prefab instances, just like with Prefab instances in scenes.
![Left: GermOBlaster Prefab included \(nested\) in the “GermSlimeTarget” Prefab in Prefab Mode. Right: The “GermSlimeTarget” Prefab instance in the Scene with the “GermOBlaster” included.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsNestedPrefab.png) Left: “GermOBlaster” Prefab included (nested) in the “GermSlimeTarget” Prefab in Prefab Mode. Right: The “GermSlimeTarget” Prefab instance in the Scene with the “GermOBlaster” included.
## Nesting Prefabs via their instances
You can also add a Prefab instance as a child to another Prefab instance in the Scene without going into Prefab Mode, just like you can add any other GameObject. Such an added Prefab instance has a plus badge overlayed on the icon in the Hierarchy which indicates that it’s an override on that specific instance of the outer Prefab.
The added Prefab can be reverted or applied to the outer Prefab in the same way as other overrides (either via the Overrides drop-down window, or via the context menu on the GameObject in the Hierarchy), as described in [Editing a Prefab via its instances](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingPrefabViaInstance.html). The Overrides drop-down button is only on the outer Prefab. Once applied, the Prefab no longer shows the plus badge, since it is no longer an override, but is nested in the outer Prefab Asset itself. It does however retain its blue cube icon because it is a Prefab instance in its own right, and retains its connection to its own Prefab Asset.
![Left: An GermOBlaster Prefab added to an instance of the “GermSlimeTarget” Prefab as an override. Right: The “GermOBlaster” Prefab has been applied to “GermSlimeTarget” Prefab, and is now a nested Prefab in the “GermSlimeTarget” Prefab Asset.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsOverrideVsNested.png) Left: An “GermOBlaster” Prefab added to an instance of the “GermSlimeTarget” Prefab as an override. Right: The “GermOBlaster” Prefab has been applied to “GermSlimeTarget” Prefab, and is now a nested Prefab in the “GermSlimeTarget” Prefab Asset.
* * *
  * 2018–07–31 Page published 
  * Nested Prefabs and Prefab Variants added in 2018.3


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingPrefabViaInstance.html)
Edit a prefab via its instances
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabVariants.html)
Prefab variants
