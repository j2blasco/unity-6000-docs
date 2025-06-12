* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Tab.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * Tab


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-SliderInt.html)
SliderInt
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TabView.html)
TabView
# Tab
A Tab element represents a single tab within a [TabView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TabView.html). In a window or menu, you can use a tab to group related content.
## Make a Tab closable
To make it so a Tab can be closed, set the [`closable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Tab-closeable.html) property to `true`. When a Tab is closable, a close icon appears on the Tab. If a user selects the close icon, the Tab closes.
## Add an icon to a Tab
You can add an icon to your Tab to make it more visually appealing. Icons can be image assets that exist in your project such as a Texture, **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture), **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite), or Vector. For information on how to reference an image asset, refer to [Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-PropertyTypes.html#assets)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset).
Do one of the following to add an icon to a Tab with UI Builder:
  * From the Tab’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) panel, select an icon from the **Icon Image** dropdown list.
  * Drag an icon from the Assets window to the **Icon Image** field located in the Tab’s Inspector panel.


To add an icon for a Tab with UXML, add the source of the image to the `icon-image` attribute:
```
<ui:Tab name="Tab" text="Tab text" icon-image="/path/to/image-file.png" />

```

To add an icon for a Tab with C#, assign the image source to the [`iconImage`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Tab-iconImage.html) property:
```
Tab myTab = new Tab();
var TabIconImage = Resources.Load<Texture2D>("image-file");

myTab.text = "Tab text";
myTab.iconImage = TabIconImage;

```

## Examples
The following UXML example creates a TabView with Tabs:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <TabView>
       <Tab label="UXML Tab A">
           <Label text="UXML tab: This is some content for the first Tab." />
       </Tab>
       <Tab label="UXML Tab B">
           <Label text="UXML tab: This is some content for the second Tab." />
       </Tab>
    </TabView>
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the TabView and its Tabs:
```
/// <sample>
// Create a TabView with Tabs that only contains a label.
var csharpTabViewWithLabels = new TabView() { style = { marginTop = 15 } }; // marginTop not required, only for demonstration purposes.
var tabOne = new Tab("One");
tabOne.Add(new Label("Tab with labels only: This is some content for the first Tab.") { style = { marginTop = 10 } });
csharpTabViewWithLabels.Add(tabOne);
var tabTwo = new Tab("Two");
tabTwo.Add(new Label("Tab with labels only: This is some content for the second Tab.") { style = { marginTop = 10 } });
csharpTabViewWithLabels.Add(tabTwo);
container.Add(csharpTabViewWithLabels);

// Create a TabView with Tabs that only contains an icon.
var csharpTabViewWithIcons = new TabView() { style = { marginTop = 15 } }; // marginTop not required, only for demonstration purposes.
var tabIconConnect = new Tab(EditorGUIUtility.FindTexture("CloudConnect"));
tabIconConnect.Add(new Label("Tab with icons only: This is some content for the first Tab.") { style = { marginTop = 10 } });
csharpTabViewWithIcons.Add(tabIconConnect);
var tabIconStore = new Tab(EditorGUIUtility.FindTexture("Asset Store"));
tabIconStore.Add(new Label("Tab with icons only: This is some content for the second Tab.") { style = { marginTop = 10 } });
csharpTabViewWithIcons.Add(tabIconStore);
container.Add(csharpTabViewWithIcons);

// Create a TabView with Tabs that only contains an icon and a label.
var csharpTabViewWithIconsAndLabels = new TabView() { style = { marginTop = 15 } }; // marginTop not required, only for demonstration purposes.
var tabConnect = new Tab("Connect", EditorGUIUtility.FindTexture("CloudConnect"));
tabConnect.Add(new Label("Tab with an icon and a labels: This is some content for the first Tab.") { style = { marginTop = 10 } });
csharpTabViewWithIconsAndLabels.Add(tabConnect);
var tabStore = new Tab("Store", EditorGUIUtility.FindTexture("Asset Store"));
tabStore.Add(new Label("Tab with an icon and a labels: This is some content for the second Tab.") { style = { marginTop = 10 } });
csharpTabViewWithIconsAndLabels.Add(tabStore);
container.Add(csharpTabViewWithIconsAndLabels);

// Create a TabView that allows re-ordering of the tabs.
var csharpReorderableTabView = new TabView() { reorderable = true, style = { marginTop = 10 } }; // marginTop not required, only for demonstration purposes.
var tabA = new Tab("Tab A");
tabA.Add(new Label("Reorderable tabs: This is some content for Tab A") { style = { marginTop = 10 } });
csharpReorderableTabView.Add(tabA);
var tabB = new Tab("Tab B");
tabB.Add(new Label("Reorderable tabs: This is some content for Tab B") { style = { marginTop = 10 } });
csharpReorderableTabView.Add(tabB);
var tabC = new Tab("Tab C");
tabC.Add(new Label("Reorderable tabs: This is some content for Tab C") { style = { marginTop = 10 } });
csharpReorderableTabView.Add(tabC);
container.Add(csharpReorderableTabView);

// Create a TabView with closeable tabs.
var closeTabInfoLabel = new Label($"Last tab closed: None");
void UpdateLabel(string newLabel) => closeTabInfoLabel.text = $"Last tab closed: {newLabel}";
var cSharpCloseableTabs = new TabView() { style = { marginTop = 10 } }; // marginTop not required, only for demonstration purposes.
var closeableTabA = new Tab("Title A") { closeable = true };
closeableTabA.closed += (tab) => { UpdateLabel(tab.label); };
closeableTabA.Add(new Label("Closeable tabs: This is some content for Tab A") { style = { marginTop = 10 } });
cSharpCloseableTabs.Add(closeableTabA);
var closeableTabB = new Tab("Title B") { closeable = true };
closeableTabB.closed += (tab) => { UpdateLabel(tab.label); };
closeableTabB.Add(new Label("Closeable tabs: This is some content for Tab B") { style = { marginTop = 10 } });
cSharpCloseableTabs.Add(closeableTabB);
var closeableTabC = new Tab("Title C") { closeable = true };
closeableTabC.closed += (tab) => { UpdateLabel(tab.label); };
closeableTabC.Add(new Label("Closeable tabs: This is some content for Tab C") { style = { marginTop = 10 } });
cSharpCloseableTabs.Add(closeableTabC);
container.Add(cSharpCloseableTabs);
container.Add(closeTabInfoLabel);

// Create a TabView and apply custom styling to specific areas of their tabs.
var csharpCustomStyledTabView = new TabView() { style = { marginTop = 15 }, classList = { "some-styled-class" }}; // marginTop not required, only for demonstration purposes.
var customStyledTabOne = new Tab("One");
customStyledTabOne.Add(new Label("Custom styled tabs: This is some content for the first Tab."));
csharpCustomStyledTabView.Add(customStyledTabOne);
var customStyledTabTwo = new Tab("Two");
customStyledTabTwo.Add(new Label("Custom styled tabs: This is some content for the second Tab."));
csharpCustomStyledTabView.Add(customStyledTabTwo);
container.Add(csharpCustomStyledTabView);
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
For more examples, refer to the following:
-[Create a tabbed menu](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-tabbed-menu-for-runtime.html).
## C# base class and namespace
**C# class** : [`Tab`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Tab.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`closeable` | `boolean` | A property that adds the ability to close tabs.  
  
The default value is `false`. Set this value to `true` to allow the user to close tabs in the tab view.  
`icon-image` | `Object` | Sets the icon for the Tab’s header.  
`label` | `string` | Sets the label of the Tab’s header.  
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
`ussClassName` | `.unity-tab` | USS class name of elements of this type.  
`tabHeaderUssClassName` | `.unity-tab__header` | USS class name for the header of this type.  
`tabHeaderImageUssClassName` | `.unity-tab__header-image` | USS class name for the icon inside the header.  
`tabHeaderEmptyImageUssClassName` | `.unity-tab__header-image--empty` | USS class name for the icon inside the header when the value is null.  
`tabHeaderStandaloneImageUssClassName` | `.unity-tab__header-image--standalone` | USS class name for the icon inside the header when the label is empty or null.  
`tabHeaderLabelUssClassName` | `.unity-tab__header-label` | USS class name for the label of the header.  
`tabHeaderEmptyLabeUssClassName` | `.unity-tab__header-label--empty` | USS class name for the label of the header when the value is empty or null.  
`tabHeaderUnderlineUssClassName` | `.unity-tab__header-underline` | USS class name for the active state underline of the header.  
`contentUssClassName` | `.unity-tab__content-container` | USS class name of container element of this type.  
`draggingUssClassName` | `.unity-tab--dragging` | USS class name for the dragging state of this type.  
`reorderableUssClassName` | `.unity-tab__reorderable` | USS class name for reorderable tab elements.  
`reorderableItemHandleUssClassName` | `.unity-tab__reorderable-handle` | USS class name for drag handle in reorderable tabs.  
`reorderableItemHandleBarUssClassName` | `.unity-tab__reorderable-handle-bar` | USS class name for drag handlebar in reorderable tabs.  
`closeableUssClassName` | `.unity-tab__header__closeable` | The USS class name for a closeable tab.  
`closeButtonUssClassName` | `.unity-tab__close-button` | The USS class name for close button in closable tabs.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resources
  * [TabView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TabView.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-SliderInt.html)
SliderInt
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TabView.html)
TabView
