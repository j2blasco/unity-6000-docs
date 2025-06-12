* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-panels.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [The visual tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree-landing.html)
  * Panels


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)
Introduction to visual elements and the visual tree
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-draw-order.html)
Draw order
# Panels
The panel is the parent object of a [visual tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree). It owns the `rootVisualElement` but itself isn’t a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). A visual tree must connect to a panel for the visual elements inside a tree to render. All panels belong to either an [Editor Window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) or a runtime [UIDocument](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument.html). The panel also handles focus control and event dispatching for the visual tree.
Every element in a visual tree holds a direct reference to the panel that holds the visual tree. To verify the connection of a [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) to a panel, you can test the [`panel`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-panel.html) property of this element. When the visual element isn’t connected, the test returns `null`.
## Additional resources
  * [Dispatch events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Dispatching.html)
  * [The visual tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)
  * [The Panel Settings asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html)
  * [Relative and absolute positioning C# example](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-relative-absolute-positioning-example.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)
Introduction to visual elements and the visual tree
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-draw-order.html)
Draw order
