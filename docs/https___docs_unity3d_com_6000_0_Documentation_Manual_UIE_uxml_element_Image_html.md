* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * Image


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-IMGUIContainer.html)
IMGUIContainer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-InspectorElement.html)
InspectorElement
# Image
Use the Image element to add graphical assets to your application. It’s a versatile and powerful tool for displaying visual content in your UI, such as image galleries, product listings, a rendering preview, and user profiles.
## Create an image
You must use either UXML or C# code to add an Image element in your UI and provide the image source to the [`--unity-image`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html#uss-custom-properties) USS custom property.
You can set the image scale mode with the [`--unity-image-size`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html#uss-custom-properties) USS custom property. You can also set the image tint color with the [`--unity-image-tint-color`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html#uss-custom-properties) USS custom property.
The following UXML example uses an inline style to add an image source:
```
<ui:Image style="--unity-image: url('path/to/image');"/>

```

You can set the size and layout of the Image element, as well as the sizing and layout of the image within the element. This allows you to control how the image is displayed within your UI, such as resizing it to fit a particular area or aligning it with other UI elements. You can also add interactivity to the Image element, such as allowing the user to click or tap on the image to trigger an action. You can apply styles to the Image element and the image itself, such as adjusting the opacity or applying a color filter.
## Image versus `VisualElement.style.backgroundImage`
You can use both the Image element and the `VisualElement.style.backgroundImage` property to add visual content to your UI. The choice between the two depends on the specific usage and requirements of your application. 
The Image element is typically used to display an image within a specific area of a UI, such as an image gallery or an **avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar) in a user profile. It provides more fine-grained control over the appearance of the image, including options for resizing, scaling, and cropping. Use Image when you want the size of an image to drive the size of an element in the layout. You can also add additional elements to the Image element to create overlays or add interactivity. However, for performance reasons, specify a fixed width and height if you use many instances of Image.
The `VisualElement.style.backgroundImage` property is used to [set an image as the background of a UI element](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-backgrounds.html). This is useful when you want to add visual interest to an element without detracting from the main content or functionality of the UI. The `VisualElement.style.backgroundImage` property also allows the convenience of using USS to change the source image for many different elements.
In general, it’s recommended to use the Image element when you need more control over the appearance and layout of an image; and to use the `VisualElement.style.backgroundImage` property when you simply want to add a background image to a UI element. However, both approaches are valid and you can use them together in the same UI if necessary.
**Note** : 
  * The Image element also supports the `style.backgroundImage` property. The background image won’t be visible if the Image element has an image source set and it’s not transparent.
  * UI Builder partially supports the Image element. It reads from and writes to UXML, and allows basic authoring as a standard **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). Most of the Image-specific settings are defined as USS custom properties and aren’t visible in the **Attributes** section of the UI Builder **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).


## C# base class and namespace
**C# class** : [`Image`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
This element also inherits the following attributes from [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-VisualElement.html):
**Name** | **Type** | **Description**  
---|---|---  
`content-container` | `string` | Child elements are added to it, usually this is the same as the element itself.  
`data-source` | `Object` | Assigns a data source to this VisualElement which overrides any inherited data source. This data source is inherited by all children.  
`data-source-path` | `string` | Path from the data source to the value.  
`data-source-type` | `System.Type` | The possible type of data source assignable to this VisualElement.  
  
This information is only used by the UI Builder as a hint to provide some completion to the data source path field when the effective data source cannot be specified at design time.  
`language-direction` | [`UIElements.LanguageDirection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LanguageDirection.html) | Indicates the directionality of the element’s text. The value will propagate to the element’s children.  
  
Setting the languageDirection to RTL adds basic support for right-to-left (RTL) by reversing the text and handling linebreaking and word wrapping appropriately. However, it does not provide comprehensive RTL support, as this would require text shaping, which includes the reordering of characters, and OpenType font feature support. Comprehensive RTL support is planned for future updates, which will involve additional APIs to handle language, script, and font feature specifications.  
  
To enhance the RTL functionality of this property, users can explore available third-party plugins in the Unity Asset Store and make use of `ITextElementExperimentalFeatures.renderedText`  
`name` | `string` | The name of this VisualElement.  
  
Use this property to write USS selectors that target a specific element. The standard practice is to give an element a unique name.  
`picking-mode` | [`UIElements.PickingMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PickingMode.html) | Determines if this element can be pick during mouseEvents or `IPanel.Pick` queries.  
`style` | `string` | Sets the `VisualElement` style values.  
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | [`UIElements.UsageHints`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html) | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence, such as tree expanded states, scroll position, or zoom level.  
  
This key is used to save and load the view data from the view data store. If you don’t set this key, the persistence is disabled for the associated `VisualElement`. For more information, refer to [View data persistence](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ViewData.html).  
## USS classes
The following table lists all the C# public property names and their related USS selector.
**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-image` | USS class name of elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
## USS custom properties
The following table outlines the custom properties that are available exclusively for the Image element in USS:
Property | Type | Description  
---|---|---  
`--unity-image` | string | The source of the image file. For information on how to reference an image asset, refer to [Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-PropertyTypes.html#assets)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset).  
`--unity-image-size` | string | The image scale mode. Available values are `stretch-to-fill`, `scale-and-crop` and `scale-to-fit`.  
`--unity-image-tint-color` | string | The image tint color.  
## Additional resources
  * [Set background images](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-backgrounds.html)
  * [Button](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-IMGUIContainer.html)
IMGUIContainer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-InspectorElement.html)
InspectorElement
