* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/create-default-inspector.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Support for Editor UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-editor-ui.html)
  * Create a default Inspector


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateCustomInspector.html)
Create a custom Inspector
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ViewData.html)
View data persistence
# Create a default Inspector
Default **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) is a standard way to display serialized object properties without any custom modifications. When you use [FillDefaultInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.FillDefaultInspector.html) method of the [InspectorElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html) class, it automatically creates the default hierarchy with the default property fields.
## Example overview
This example extend the `CreateInspectorGUI()` method in the [Create a Custom Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateCustomInspector.html) example to create a default Inspector for the `Car` component. The example creates a `Foldout` control in the `Car_Inspector_UXML.uxml` file and attaches the default Inspector UI to it.
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [Foldout](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Foldout.html)
  * [InspectorElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html)


## Create the default Inspector container
Create a Foldout control to display the default Inspector UI.
  1. Double-click the `Car_Inspector_UXML.uxml` file to open it in UI Builder.
  2. Add a Foldout control to your UI, name it `Default_Inspector`, and set a label text:
![Foldout for the default Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-uibuilder-Foldout.png) Foldout for the default Inspector


## Attach the default Inspector UI
To attach the default Inspector UI to the Foldout, you must obtain a reference to it. You can retrieve the **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) of the Foldout from the **visual tree** An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree) of your Inspector using [UQuery](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UQuery.html), and use the [FillDefaultInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.FillDefaultInspector.html) method of the [InspectorElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html) class to attach the default Inspector UI to the Foldout control.
  1. In the `Car_Inspector.cs` file, update the `CreateInspectorGUI()` method to get a reference to the `Default_Inspector` Foldout and attach the default Inspector UI to it:
```
public override VisualElement CreateInspectorGUI()
{
   ...
       
   // Get a reference to the default Inspector Foldout control.
    VisualElement InspectorFoldout = myInspector.Q("Default_Inspector");
            
    // Attach a default Inspector to the Foldout.
    InspectorElement.FillDefaultInspector(InspectorFoldout, serializedObject, this);

    // Return the finished Inspector UI.
    return myInspector;
}

```

  2. Select the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that has the `Car` component to it. The Inspector for the `car` component now displays the `Default Inspector` Foldout with the default Inspector UI inside.
![Inspector with a default Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-custominspector-foldoutinspector.png) Inspector with a default Inspector


## Additional resources
  * [Create a custom Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateCustomInspector.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateCustomInspector.html)
Create a custom Inspector
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ViewData.html)
View data persistence
