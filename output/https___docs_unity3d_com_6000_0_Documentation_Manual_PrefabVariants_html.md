* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabVariants.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * Prefab variants


[](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedPrefabs.html)
Nested prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html)
Overrides at multiple levels
# Prefab variants
Prefab Variants are useful when you want to have a set of predefined variations of a **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab).
For example, you might want to have several different types of GermSlimeTargets in your game, which are all based on the same basic GermSlimeTarget Prefab. However you may want some GermSlimeTargets to carry items, some to move at different speeds, or some to emit extra sound effects.
To do this, you could set up your initial GermSlimeTarget Prefab to perform all the basic actions you want all GermSlimeTarget to share, then you could create several Prefab Variants to:
  * Make a GermSlimeTarget move faster by using a property override on a script to change its speed.
  * Make a GermSlimeTarget carry an item by attaching an additional **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to its arm.
  * Give GermSlimeTarget a slug-like squelch by adding an AudioSource component that plays a squelching sound.


A Prefab Variant inherits the properties of another Prefab, called the base. Overrides made to the Prefab Variant take precedent over the base Prefab’s values. A Prefab Variant can have any other Prefab as its base, including Model Prefabs or other Prefab Variants.
## Creating a Prefab Variant
There are multiple ways to create a Prefab Variant based on another Prefab.
You can **right-click** on a Prefab in the Project view and select **Create > Prefab Variant**. This creates a variant of the selected Prefab, which initially doesn’t have any overrides. You can open the Prefab Variant in Prefab Mode to begin adding overrides to it.
You can also **drag** a Prefab instance in the Hierarchy into the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow). When you do this, a dialog asks if you want to create a new Original Prefab or a Prefab Variant. If you choose Prefab Variant you get a new Prefab Variant based on the Prefab instance you dragged. Any overrides you had on that instance are now inside the new Prefab Variant. You can open it in Prefab Mode to add additional overrides or edit or remove overrides.
Prefab Variants are shown with the blue Prefab icon decorated with arrows.
![A basic GermSlimeTarget Prefab, and a variant of that Prefab called GermSlimeTarget With GermOBlaster, as viewed in the Hierarchy window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsBasicAndVariant.png) A basic GermSlimeTarget Prefab, and a variant of that Prefab called “GermSlimeTarget With GermOBlaster”, as viewed in the Hierarchy window.
## Editing a Prefab Variant
When a Prefab Variant is opened in Prefab Mode, the root appears as a Prefab instance with the blue Prefab icon. This Prefab instance represents the base Prefab that the Prefab Variant inherits from; it doesn’t represent the Prefab Variant itself. Any edits you make to the Prefab Variant become overrides to this base that exists in the Variant.
![The Prefab Variant GermSlimeTarget With GermOBlaster in Prefab Mode. The “GermOBlaster” Prefab is added as an override to the base Prefab](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsVariantAddedObject.png) The Prefab Variant “GermSlimeTarget With GermOBlaster” in Prefab Mode. The “GermOBlaster” Prefab is added as an override to the base Prefab
In the screenshot above, if you were to select the **GermSlimeTarget With GermOBlaster** root GameObject and click the **Select** button in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), it will select the base Prefab **GermSlimeTarget** and not the Variant **GermSlimeTarget With GermOBlaster** because the Prefab instance is an instance of the base Prefab **GermSlimeTarget** and the **Select** button always selects the Prefab Asset that an instance comes from.
As with any Prefab instance, you can use prefab overrides in a Prefab Variant, such as modified property values, added components, removed components, and added child GameObjects. There are also the same limitations: you cannot reparent GameObjects in the Prefab Variant which come from its base Prefab. You also cannot remove a GameObject from a Prefab Variant which exists in its base Prefab. You can, however, deactivate GameObjects (as a property override) to achieve the same effect as removing a GameObject.
**Note** : When editing a Prefab Variant in Prefab Mode, you should understand that applying these overrides (via the Overrides drop-down window or context menus) will cause your variant’s variations to be applied to the base Prefab Asset. This is often **not** what you want. The point of a Prefab Variant is to provide a convenient way to store a meaningful and reusable collection of overrides, which is why they should normally remain as overrides and not get applied to the base Prefab Asset. To illustrate this point, if you were to apply the additional **GermOBlaster** GameObject to the base Prefab Asset (the “GermSlimeTarget”), then the Prefab Asset would also have the **GermOBlaster**. The whole point of the **GermSlimeTarget With GermOBlaster** variant is that only this variation carries an GermOBlaster, so the added **GermOBlaster** GameObject should be left as an override inside the Prefab Variant.
When you open the Overrides drop-down window, you can always see in its header which object the overrides are to, and in which context the overrides exist. For a Prefab Variant, the header will say that the overrides are to the base Prefab and exist in the Prefab Variant. To make it extra clear, the **Apply All** button also says **Apply All to Base**.
![Overrides dropdown for a Prefab Variant when editing the Prefab Variant in Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsVariantOverrideDropdown.png) Overrides dropdown for a Prefab Variant when editing the Prefab Variant in Prefab Mode
* * *
  * 2018–07–31 Page published 
  * Nested Prefabs and Prefab Variants added in 2018.3


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedPrefabs.html)
Nested prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html)
Overrides at multiple levels
