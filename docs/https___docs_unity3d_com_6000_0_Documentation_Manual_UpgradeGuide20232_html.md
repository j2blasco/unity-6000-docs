* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20232.html

  * [Install and upgrade](https://docs.unity3d.com/6000.0/Documentation/Manual/install-and-upgrade.html)
  * [Upgrade Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuides.html)
  * Upgrade to Unity 2023.2


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuideUnity6.html)
Upgrade to Unity 6.0
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20231.html)
Upgrade to Unity 2023.1
# Upgrade to Unity 2023.2
This page lists changes in Unity 2023.2 which might affect existing projects when you upgrade them from a 2023.1 version to 2023.2.
### Page outline
  * [Environment lighting: Ambient probe and skybox Reflection Probe are no longer baked by default](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20232.html#environment-lighting)
  * [Auto-generated lighting has been removed](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20232.html#auto-generated-lighting)
  * [DepthAuto, ShadowAuto and VideoAuto graphics formats are now obsolete](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20232.html#depthauto-shadowauto-videoauto)
  * [Mipmap Limits no longer affect runtime Textures by default](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20232.html#mipmap-limits)
  * [Enhanced custom controls creation with UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20232.html#enhanced-custom-controls-creation-with-uxml)
  * [Assets/Create menu and ScriptTemplates have been reorganized](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20232.html#assets-create-menu-and-scripttemplates-have-been-reorganized)
  * [UI Toolkit event handling reorganization and simplification](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20232.html#ui-toolkit-event-handling-reorganization-and-simplification)


## Environment lighting: Ambient probe and skybox Reflection Probe are no longer baked by default
Unity’s Progressive **Lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) no longer bakes the ambient probe and the **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) **Reflection Probe** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) by default, and the **Recalculate Environment Lighting** setting in the **Lighting** window has been removed.
To avoid a newly created **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) having no environment lighting, Unity assigns a default [Lighting Data Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/LightmapSnapshot.html) containing environment lighting that matches the default skybox material.
You must select **Generate Lighting** in the **Lighting** window in the following cases:
  * To fix the lights in a scene where you rely on the previous automatic baking behavior.
  * To see lighting changes in a new scene if you change the environment lighting settings.


If you rely on the previous automatic baking behavior but you use the default environment lighting settings, Unity upgrades the scene to use the default Lighting Data Asset.
## Auto-generated lighting has been removed
The **Auto Generate** setting in the **Lighting** window has been removed, and related APIs are now obsolete.
To generate baked lighting for a scene, you can do any of the following:
  * Select **Generate Lighting** in the **Lighting** window.
  * Use the `Lightmapping.Bake` API.
  * Use the `Lightmapping.BakeAsync` API.


To check **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) while you’re editing, you can now select a [Scene View Draw Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/GIVis.html) and set **Lighting Data** to **Preview**. This displays a preview of the baked lighting. The preview lightmaps are non-destructive, and you can use them after you’ve baked the scene.
If a scene relies on auto-generated lighting, it no longer has its baked lighting. Select **Generate Lighting** in the **Lighting** window to re-bake the lighting manually.
If you use a script to open a scene, you must now use `Lightmapping.Bake` or `Lightmapping.BakeAsync` instead of waiting for auto-generated lighting to complete.
## DepthAuto, ShadowAuto and VideoAuto graphics formats are now obsolete
The following graphics formats, which were [previously deprecated in 2022.1](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2021LTS.html#Graphics), are now obsolete and produce compile errors if you use them:
  * `GraphicsFormat.DepthAuto`
  * `GraphicsFormat.ShadowAuto`
  * `GraphicsFormat.VideoAuto`


The [GraphicsFormatUtility.GetGraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormatUtility.GetGraphicsFormat.html) API no longer returns the obsolete formats. Instead it does the following:
  * Translates `RenderTextureFormat.Depth` to `GraphicsFormat.None` instead of `GraphicsFormat.DepthAuto`. `GraphicsFormat.None` indicates depth-only rendering.
  * Translates `RenderTextureFormat.Shadowmap` to `GraphicsFormat.None` instead of `GraphicsFormat.ShadowAuto`. If you create a **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) with the `GraphicsFormat.None` format, you must set RenderTextureDescriptor.shadowSamplingMode to ShadowSamplingMode.CompareDepths to enable depth-compare sampling.


Because `GraphicsFormat.DepthAuto` and `GraphicsFormat.ShadowAuto` were both considered depth stencil formats but used as colors formats, you may need to adjust your code.
For example, in the following snippet, `GraphicsFormatUtility.IsDepthFormat` returns `false` instead of `true`:
```
RenderTextureDescriptor desc = new RenderTextureDescriptor(256, 256, RenderTextureFormat.Depth, 32);
bool isDepthOnly = GraphicsFormatUtility.IsDepthFormat(desc.graphicsFormat);

```

To check if a `RenderTexture` or `RenderTextureDescriptor` is depth-only, use one of the following:
  * `if (renderTexture.graphicsFormat == GraphicsFormat.None && renderTexture.depthStencilFormat != GraphicsFormat.None)`
  * `if (renderTexture.format == RenderTextureFormat.Depth || renderTexture.format == RenderTextureFormat.Shadowmap)`


## Mipmap Limits no longer affect runtime Textures by default
Runtime-created 2D textures will no longer have their mipmap upload limited by default. Before, mipmap limits had to be disabled explicitly via the Texture2D constructor (by providing an `ignoreMipmapLimit` boolean parameter when the constructor is called with a TextureFormat, or the `IgnoreMipmapLimit` TextureCreationFlag when it’s called with a GraphicsFormat), or by toggling `tex.ignoreMipmapLimit` of a constructed texture. This behavior has changed: **mipmap limits are now opt-in for runtime-created 2D textures**.
Without making project changes, in the following cases users miss out on GPU bandwidth and memory optimizations, and potentially see a better quality than intended because textures are now getting uploaded at full resolution:
  * Users who unknowingly expect runtime textures to follow the quality settings.
  * Users who intentionally wanted runtime textures to follow the quality settings and achieved this by using any default Texture2D-constructor.


In following cases, users are not affected by this change:
  * Users who explicitly wanted runtime textures to remain full-resolution.
  * Users who intentionally wanted runtime textures to follow the quality settings and achieved by making the following explicit: 
    * Using a constructor with a TextureFormat, with `false` for `ignoreMipmapLimit`,
    * Setting `tex.ignoreMipmapLimit` to `false` after construction.


These users may want to upgrade their **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) if they use deprecated constructors.
To upgrade your scripts, use a Texture2D constructor with a `MipmapLimitDescriptor` to indicate that a runtime Texture should be affected by the quality settings.
This change was made for consistency with the new mipmap limit support for Texture2DArrays. Rather than having each texture shape define its own default mipmap limit behavior, we opt for consistency and have decided that runtime textures should explicitly enable mipmap limits. This opt-in behavior is preferred over opt-out because runtime textures are often used in more versatile ways where unexpectedly uploading fewer mips than expected could be more harmful than unexpectedly uploading more mips.
## Enhanced custom controls creation with UXML
Simplified the creation of custom controls with UXML in UI Toolkit to speed up the workflow and make it more intuitive.
A key improvement is the introduction of UxmlElement and UxmlAttribute attributes. These attributes simplify attribute authoring and automatically derive the attribute names from property names, eliminating the need for UxmlTraits and UxmlFactory classes.
You can now create custom attribute converters for specific data types, ensuring seamless conversion of values to and from UXML attribute strings. We’ve also enhanced UxmlObjects, allowing custom, non-visual elements to be defined within **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). The new system leverages the Unity serialization and uses a source generator to create UxmlSerializedData classes for elements from all UxmlAttribute definitions for each custom element class, enabling support for custom **property drawers** A Unity feature that allows you to customize the look of certain controls in the Inspector window by using attributes on your scripts, or by controlling how a specific Serializable class should look [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-PropertyDrawers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PropertyDrawer), decorators, and various attributes.
The introduction of “attribute overrides” allows you to customize the behavior of UXML attributes, and provides flexibility when you work with inherited attributes. These improvements provide a more efficient and user-friendly experience for creating complex UI elements in Unity 2023.2 and beyond. 
For example, the following code sample is a custom control created with `UxmlFactory` and `UxmlTraits`:
```
public class HealthBar : VisualElement
{
   private const float k_LowValue = 0;
   private const float k_HighValue = 100;

   // Declare as usable with Uxml
   public new class UxmlFactory : UxmlFactory<HealthBar, UxmlTraits> { }
   // Define attributes (and connect with class properties) for Uxml 
   public new class UxmlTraits : BindableElement.UxmlTraits
   {
       UxmlColorAttributeDescription m_Color = new UxmlColorAttributeDescription { name = "color", defaultValue = Color.white };
       UxmlFloatAttributeDescription m_Value = new UxmlFloatAttributeDescription { name = "value", defaultValue = k_HighValue };

       public override void Init(VisualElement ve, IUxmlAttributes bag, CreationContext cc)
       {
           base.Init(ve, bag, cc);
           var bar = ve as HealthBar;
           bar.color = m_Color.GetValueFromBag(bag, cc);
           bar.value = m_Value.GetValueFromBag(bag, cc);
       }
   }

   public Color color { get; set; }

   [Range(k_LowValue, k_HighValue)]
   public float value { get; set; }
}

```

The following code sample does the same thing as the previous code sample, but uses the new `UxmlElement` and `UxmlAttributes` system:
```
[UxmlElement]
public class HealthBar2 : VisualElement
{
   private const float k_LowValue = 0;
   private const float k_HighValue = 100;

   [UxmlAttribute]
   public Color color { get; set; } = Color.white;

   [UxmlAttribute]
   [Range(k_LowValue, k_HighValue)]
   public float value { get; set; } = k_HighValue;
}

```

For more examples and information, refer to [Unity UI Toolkit documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html), and stay tuned for an in-depth blog post this fall.
## Assets/Create menu and ScriptTemplates have been reorganized
The **Assets/Create** menu has been reorganized and categorized. As part of this overhaul, the Unity Built-In ScriptTemplate files have been renamed. 
Users who have added elements to the **Assets/Create** menu with either `CreateAssetMenuAttribute``, MenuItemAt`tribute or a Custom ScriptTemplate might want to change their menu item’s priority as it’s placement relative to other elements is now different. 
Users who were creating assets by executing these menu items with the `EditorApplication.ExecuteMenuItem` API, must verify the new path to the menu item.
Users who have previously overridden the Unity Built-In ScriptTemplates must update the names of their override files to ensure they match the new names of the Built-In Templates.
## UI Toolkit event handling reorganization and simplification
The `ExecuteDefaultAction` and `ExecuteDefaultActionAtTarget` methods have been deprecated. The following methods are added to replace them: 
  * `HandleEventTrickleDown`
  * `HandleEventBubbleUp`


Unity executes these new methods on each element in the event dispatching path immediately after `TrickleDown` and before `BubbleUp` callbacks of that element. During those methods, the dispatching phase is set to `TrickleDown` or `BubbleUp` accordingly and the event’s `currentTarget`` coincides with the element executing the method.
The `AtTarget` dispatching phase and the `PreventDefault` method have been deprecated. Calling `StopPropagation` or `StopPropagationImmediately` now stops further executing `HandleEventTrickleDown` and `HandleEventBubbleUp` at the same time as it stops further invocation of the `TrickleDown` and `BubbleUp`` callbacks.
In most cases, if you don’t upgrade to the new methods, your code should not alter its behavior significantly. UI Tookkit still calls the obsolete methods in the same order as before, or with minimal adjustments. However, all the standard controls within UI Toolkit have migrated to using the new methods, aligning their logic execution order accordingly. Mixing calls to obsolete methods with the use of upgraded controls might lead to some logic being out of sync compared to previous Unity versions.
To upgrade existing code to the new methods, proceed as follows:
  * Replace `ExecuteDefaultAction` and `ExecuteDefaultActionAtTarget` by `HandleEventBubbleUp` and `PreventDefault` by `StopPropagation` (or remove calls to `PreventDefault` if `StopPropagation` has already been called in the same code block. This covers the majority of cases).
  * If you have problems because of old code calling `PreventDefault` during a `BubbleUp` callback, which is no longer possible and can’t be replaced by StopPropagation because the event has already reached its target, consider adding a callback during the `TrickleDown` phase to call `StopPropagation`. This step is generally sufficient to address such scenarios.
  * In rare cases where the above changes aren’t adequate to maintain the functionality of the old code, a thorough case-by-case analysis is necessary. The resolution might not always be straightforward in these contexts.


## Additional resources
  * [What’s New in Unity 2023.2](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew20232.html)
  * [Install Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/GettingStartedInstallingUnity.html)
  * [API updater](https://docs.unity3d.com/6000.0/Documentation/Manual/APIUpdater.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuideUnity6.html)
Upgrade to Unity 6.0
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20231.html)
Upgrade to Unity 2023.1
