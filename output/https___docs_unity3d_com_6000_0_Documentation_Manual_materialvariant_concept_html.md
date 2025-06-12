* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-concept.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)
  * [Material Variants](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-landingpage.html)
  * Introduction to Material Variants


[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-landingpage.html)
Material Variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-hierarchyconcept.html)
Material Variant inheritance
# Introduction to Material Variants
## How Material Variants help artists
Many of the materials in a game may be variations on a source—outfits with a variety of color schemes, damaged and undamaged versions of scenery, shiny and weathered instances of props. To help you manage and maintain these materials, Material Variants address specific shortcomings of copied materials, as illustrated in this table.
**Copied material** | **Material Variant**  
---|---  
Does not automatically change if its source material changes. | Automatically changes if its parent changes.  
To replicate a change to a copy in its source material, you must manually adjust the source material. | You can copy changes from a child material to its parent with two mouse clicks.  
You can’t limit changes to the Properties of copies. | You can lock one or more Properties on a Material or Material Variant to prevent modifications to those Properties in its children.  
You can’t associate a copy with a different source. | You can reparent Material Variants.  
### Create, convert, or reparent Material Variants
You can create Material Variants from both Materials and other Material Variants. It is also possible to convert Material Variants into Materials. To use the Override(s) in a variant with a variety of different Materials, you can change the parent of that variant.   
  
See [Create, modify, and apply Material Variants](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-tasks.html) for information about how to create and convert Material Variants.   
  
See [Material Variant inheritance](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-hierarchyconcept.html) for an explanation of the Material Variant hierarchy.
### Variant sources
It is possible to create a Material Variant from any Material, including one you make with [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@13.1/manual/index.html) or download from the [Asset Store](https://assetstore.unity.com)A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore). See [Create, modify, and apply Material Variants](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-tasks.html) for detailed information about how to create Material Variants from **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
### Identify and revert changes
An Override is a change you make to a Material Variant’s Properties. You can revert one Override at a time or all Overrides at once. Unity does not handle reverts through the Undo stack, which means that you can revert an Override without undoing any other changes.   
  
See [Create, modify, and apply Material Variants](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-tasks.html) for detailed information about how to identify and revert Overrides.
### Unity prevents inheritance issues
Unity protects against ancestor deletion and circular dependencies. If you attempt to delete the parent of a Material Variant, Unity warns you to select a new parent for the child or reparent it.   
  
See [Material Variant inheritance](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-hierarchyconcept.html) for detailed information about Material Variant hierarchies and inheritance error messages.
### Scripts
You can use the Material Variant API to access Material Variant functionality for complex or large operations.   
  
See the [Material](https://docs.unity3d.com/2022.1/Documentation/ScriptReference/Material.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) and [MaterialEditor](https://docs.unity3d.com/ScriptReference/MaterialEditor.html) API documentation for information about how to work with Material Variants in **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
## Similarities to Prefab Variants
[Prefab Variants](https://docs.unity3d.com/Manual/PrefabVariants.html) and Material Variants have much the same functionality, foundational concepts, and workflow. There are two key differences between them:
  * You can reparent a Material Variant.
  * You can lock Material Variant Properties.


## Prerequisites and limitations
Material Variants are not designed to address optimization and scalability concerns. In addition, it is not possible to use Material Variants to alter Materials at runtime in the Player.
## Additional resources
  * [Materials introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-introduction.html)
  * [Material Inspector Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab)
  * [Prefab Variants](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabVariants.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-landingpage.html)
Material Variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-hierarchyconcept.html)
Material Variant inheritance
