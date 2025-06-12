* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-focus-order.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * Focus order of elements


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html)
Handle event callbacks and value changes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-events-handling-custom-control.html)
Respond to events with custom controls
# Focus order of elements
Each panel has a focus ring that defines the focus order of elements. By default, a depth-first search (DFS) on the **visual tree** An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree) defines the focus order of elements. For example, the focus order for the tree depicted below is F, B, A, D, C, E, G, I, H.
![Focus order](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/focus-order.png) Focus order
Some events use the focus order to define which element holds the focus. For example, the target for a keyboard event is the element in focus.
Use the `focusable` property to control whether a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) is focusable. By default, `VisualElements` aren’t focusable, but some subclasses, such as `TextField`, might be focusable by default.
Use the `tabIndex` property to control the focus order as follows (`tabIndex` default value of 0):
  * If the `tabIndex` is negative, you can’t use tab on the element.
  * If the `tabIndex` is zero, the element keeps its default tab order, as determined by the focus ring algorithm.
  * If the `tabIndex` is positive, the element is placed in front of other elements that either have a zero `tabIndex` (`tabIndex = 0`) or a `tabIndex` value smaller than its own.


## Additional resources
  * [Events reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html)
Handle event callbacks and value changes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-events-handling-custom-control.html)
Respond to events with custom controls
