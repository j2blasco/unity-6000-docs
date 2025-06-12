* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [The visual tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree-landing.html)
  * Introduction to visual elements and the visual tree


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree-landing.html)
The visual tree
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-panels.html)
Panels
# Introduction to visual elements and the visual tree
The most basic building block in UI Toolkit is a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). The visual elements are ordered into a hierarchy tree with parent-child relationships. This is called the **visual tree** An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree).
The diagram below displays a simplified example of the visual tree, and the rendered result in UI Toolkit.
![Simplified hierarchy of the visual tree](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VisualTreeExample.png) Simplified hierarchy of the visual tree
The Root in the diagram represents the [`EditorWindow.rootVisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-rootVisualElement.html) in the Editor UI and the [`UIDocument.rootVisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument-rootVisualElement.html) in a runtime UI. 
The [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class is the base for all nodes in the visual tree. The `VisualElement` base class contains properties such as styles, layout data, and event handlers. Visual elements can have children and descendant visual elements. For example, in the diagram above, the first `Box` visual element has three child visual elements: `Label`, `Checkbox`, and `Slider`.
You can customize the appearance of visual elements through inline styles and stylesheets. You can also use event callbacks to modify the behavior of a visual element.
[`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) derives into subclasses that define additional behavior and functionality, such as controls. UI Toolkit includes a variety of built-in controls with specialized behavior. A control is an element of a graphical user interface. For example, the following items are available as built-in controls:
  * [Buttons](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html)
  * [Toggles](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html)A checkbox that allows the user to switch an option on or off. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toggle)
  * [Text input fields](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextField.html)A field that allows the user to input a Text string [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-InputField.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextInputField)


A control includes the visual of the control, and the scripted logic to operate and interact with the control. It can consist of a single visual element, or a combination of multiple visual elements. For example, the Toggle control contains three elements:
  * A text label
  * An image of a box
  * An image of a checkmark

![Toggle control](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-toggle-control.png) Toggle control
The implementation of the Toggle control defines the behavior of the control. It has an internal value of whether the toggle state is true or false. This logic alternates the visibility of the checkmark image when the value changes.
You can also combine visual elements together and modify their behavior to create [custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html). 
To use a control in a UI, add it to the visual tree. 
## Additional resources
  * [Structure UI with UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [Structure UI with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Controls.html)
  * [UXML elements Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree-landing.html)
The visual tree
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-panels.html)
Panels
