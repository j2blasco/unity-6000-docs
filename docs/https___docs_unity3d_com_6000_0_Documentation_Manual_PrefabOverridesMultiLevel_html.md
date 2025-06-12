* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * Overrides at multiple levels


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabVariants.html)
Prefab variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnusedOverrides.html)
Unused overrides
# Overrides at multiple levels
When you work with Prefabs inside other Prefabs, or with **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) Variants, overrides can exist at multiple levels, and the same overrides can have multiple different Prefabs they can be applied to.
## Choice of apply target
When you have a Prefab instance which has nested Prefabs inside it, or which is a Prefab Variant, you might have a choice of which Prefab an override should be applied to.
Consider a Prefab “Vase” which is nested inside a Prefab “Table”, and the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) contains an instance of the “Table” Prefab.
![A ‘Vase’ Prefab nested inside a ‘Table’ Prefab.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsMultipleApplyTarget1.png) A ‘Vase’ Prefab nested inside a ‘Table’ Prefab.
If on this instance, a property on “Vase” is overridden, there are multiple Prefabs this override could be applied to: the “Vase” or the “Table”.
The **Apply All** button in the Overrides drop-down window only allows applying the override to the outer Prefab - the “Table” in this case. But a choice of apply target is available when applying either via the context menu, or via the comparison view for individual components in the Overrides drop-down window.
![The Inspector window displays the context menu of a Capsule Colldier component. The Added Component menu submenu gives the options to apply the override to the outer Table prefab or the inner Vase prefab.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsMultipleApplyTarget2.png) The Inspector window displays the context menu of a Capsule Colldier component. The Added Component menu submenu gives the options to apply the override to the outer Table prefab or the inner Vase prefab.
In this example, if you choose **Apply to Prefab ‘Vase’** , the value is applied to the ‘Vase’ Prefab Asset and is used for all instances of the ‘Vase’ Prefab.
And, if you choose **Apply as Override in Prefab ‘Table’** , the value becomes an override on the instance of ‘Vase’ that is inside the ‘Table’ Prefab. The property is no longer marked as an override on the instance in the Scene, but if you open the ‘Table’ Prefab in Prefab Mode, the property on the ‘Vase’ Prefab instance is marked as an override there.
The ‘Vase’ Prefab Asset itself is not affected at all when overriding as an override in the ‘Table’ Prefab Asset. This means that all instances of the ‘Table’ Prefab now have the new value on their ‘Vase’ Prefab instance, but other instances of the ‘Vase’ Prefab that are not part of the ‘Table’ Prefab are not affected.
If the property on the ‘Vase’ Prefab itself is later changed, it will affect all instances of the ‘Vase’ Prefab, except where that property is overridden. Since it’s overridden on the ‘Vase’ instance inside the ‘Table’ Prefab, the change won’t affect any of the ‘Vase’ instances that are part of ‘Table’ instances.
## Applying to inner Prefabs may affect outer Prefabs too
Applying one or more properties to an inner Prefab Asset can sometimes modify outer Prefab Assets as well, because those properties get their overrides reverted in the outer Prefabs.
In our example, if **Apply to Prefab ‘Vase’** is chosen and the ‘Table’ Prefab has an override of the value, this override in the ‘Table’ Prefab is reverted at the same time so that the property on the instance retains the value that was just applied. If this was not the case, the value on the instance would change right after being applied.
* * *
  * 2018–07–31 Page published 
  * Nested Prefabs and Prefab Variants added in 2018.3


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabVariants.html)
Prefab variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnusedOverrides.html)
Unused overrides
