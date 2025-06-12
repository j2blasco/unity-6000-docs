* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * Button


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Box.html)
Box
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ColorField.html)
ColorField
# Button
Use the Button element to create clickable buttons in a UI. For example, when a user clicks or taps on a Button element, it triggers an action or event, such as opening a new window, submitting a form, or playing a sound effect.
## Create a Button
You can create a Button with UI Builder, UXML, or C#. The following C# example creates a Button with a label:
```
var button = new Button(() => { Debug.Log("Button clicked"); }) { text = "Click me" };

```

## Add an icon to a Button
You can enhance the visual appeal of your Button by incorporating an icon, such as a Texture, **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture), **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite), or Vector image asset that exists in your project. For information on how to reference an image asset, refer to [Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-PropertyTypes.html#assets)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset).
To add an icon for a Button with UI Builder:
  * From the Button’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) tab, choose the desired icon from the **Icon Image** dropdown list.
  * Alternatively, drag the icon from the Assets window to the **Icon Image** field located in the Button’s Inspector tab.


To add an icon for a Button with UXML, provide the image source to the `icon-image` attribute:
```
<ui:Button name="Button" text="Button text" icon-image="/path/to/image-file.png" />

```

To add an icon for a Button with C#, assign the image source to the [`iconImage`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button-iconImage.html) property:
```
Button myButton = new Button();
var buttonIconImage = Resources.Load<Texture2D>("image-file");

myButton.text = "Button text";
myButton.iconImage = buttonIconImage;

```

## Change the Button icon position
When you add an icon to a Button, it adds two [read-only](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-structuring-ui-elements.html#read-only-elements) sub-elements to the Button: 
  * An [Image](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html) element to define the icon image.
  * A [TextElement](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextElement.html) to define the button text.


You can’t edit the sub-elements but you can change their layout using the USS `flex-direction` property for the Button element. By default, the icon is added on the left of the button text. 
To reposition the button icon, adjust the Button’s `flex-direction` with the following:
  * To shift the icon to the right of the button text, set it to `row-reverse`.
  * To move the icon above the button text, set it to `column`.
  * To place the icon below the button text, set it to `column-reverse`.


## Use sub-elements of a Button
The Button element allows you to provide additional information to the user with the `text`, `iconImage` properties, and the `background-image` style property. As with any **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement), you can also add sub-elements in a Button’s hierarchy, such as a Label or Image, to provide additional information to the user if you want to have more fine-grained control over the appearance and behavior of those elements.
In general, use sub-elements in the following situations:
  * Customization: Using sub-elements allows you to customize the appearance and behavior of each individual element separately. For example, you may want to use a custom font or color for the label text or add a specific animation to the image. When you add an Image element to your Button, you can add the element from your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) directly. In addition, an Image element also supports scale mode and repeat mode.
  * Dynamic content: If the content of the label or image is dynamic, using sub-elements allows you to update the content of each element separately without affecting the other properties of the button.
  * Interaction: If you want to add interactivity to a specific element within the button, such as allowing the user to click only the label (disregarding clicks on other elements of the button) to trigger an action, using sub-elements makes this possible.


Use properties for the following purposes:
  * Simple designs: If the design of the button is simple and doesn’t require customization or dynamic content, using properties is recommended.
  * Performance: If you have many buttons in your UI, using sub-elements for each one may negatively impact performance. In this case, it’s more efficient to use properties to set the appearance of the button.
  * Consistency: If you want to maintain consistency across your UI, using properties can ensure that all buttons have a consistent appearance and behavior.


## Examples
The following UXML example creates a Button:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <Button text="UXML Button" name="the-uxml-button" />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the Button:
```
/// <sample>
// Action to perform when button is pressed.
// Toggles the text on all buttons in 'container'.
Action action = () =>
{
    container.Query<Button>().ForEach((button) =>
    {
        button.text = button.text.EndsWith("Button") ? "Button (Clicked)" : "Button";
    });
};

// Get a reference to the Button from UXML and assign it its action.
var uxmlButton = container.Q<Button>("the-uxml-button");
uxmlButton.RegisterCallback<MouseUpEvent>((evt) => action());

// Create a new Button with an action and give it a style class.
var csharpButton = new Button(action) { text = "C# Button" };
csharpButton.AddToClassList("some-styled-button");
container.Add(csharpButton);
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## C# base class and namespace
**C# class** : [`Button`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`TextElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextElement.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`icon-image` | `Object` | The Texture, Sprite, or VectorImage that will represent an icon within a Button element.  
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`display-tooltip-when-elided` | `boolean` | When true, a tooltip displays the full version of elided text, and also if a tooltip had been previously provided, it will be overwritten.  
`emoji-fallback-support` | `boolean` | Specifies the order in which the system should look for Emoji characters when rendering text. If this setting is enabled, the global Emoji Fallback list will be searched first for characters defined as Emoji in the Unicode 14.0 standard.  
`enable-rich-text` | `boolean` | When false, rich text tags will not be parsed.  
`focusable` | `boolean` | True if the element can be focused.  
`parse-escape-sequences` | `boolean` | Specifies whether escape sequences are displayed as is or if they are replaced by the character they represent.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`text` | `string` | The text to be displayed.  
  
Changing this value will implicitly invoke the `INotifyValueChanged_1.value` setter, which will raise a `ChangeEvent_1` of type string.  
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
`ussClassName` | `.unity-button` | USS class name of elements of this type.  
  
Unity adds this USS class to every instance of the Button element. Any styling applied to this class affects every button located beside, or below the stylesheet in the visual tree.  
`iconUssClassName` | `.unity-button--with-icon` | The USS class name for Button elements with an icon.  
  
Unity adds this USS class to an instance of the Button element if the instance’s `Button.iconImage` property contains a valid Texture. Any styling applied to this class affects every button with an icon located beside, or below the stylesheet in the visual tree.  
`ussClassName` | `.unity-text-element` | USS class name of elements of this type.  
`selectableUssClassName` | `.unity-text-element__selectable` | USS class name of selectable text elements.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resources
  * [Image](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html)
  * [TextElement](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextElement.html)
  * [ToggleButtonGroup](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ToggleButtonGroup.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Box.html)
Box
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ColorField.html)
ColorField
