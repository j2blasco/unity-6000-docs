* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-bind.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)
  * Bind with UXML and C# script


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-without-bindpath.html)
Bind without the binding path
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-inspector.html)
Create a binding with the Inspector
# Bind with UXML and C# script
**Version** : 2021.3+
This example demonstrates how to create a binding and set the binding path with UXML, and call the `Bind()` method with a C# script.
## Example overview
This example creates a custom Editor window with a TextField that binds to the name property of any **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
![Displays a Unity Editor window with a custom field to change the name of a GameObject.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie_uxml_binding.png) Displays a Unity Editor window with a custom field to change the name of a GameObject.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/bind-with-uxml-csharp).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [Visual Tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree)
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [`bindingPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement-bindingPath.html)
  * [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html)


## Define the binding path in UXML
Define the **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) and the binding path in UXML.
  1. Create a project in Unity with any template.
  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `bind-with-uxml-csharp` folder to store all your files.
  3. Create a UI Document named `binding_example.uxml` and replace its content with the following:
```
<UXML xmlns:ui="UnityEngine.UIElements">
    <ui:VisualElement name="top-element">
        <ui:Label name="top-label" text="UXML-Defined Simple Binding"/>
        <ui:TextField name="GameObjectName" label="Name" text="" binding-path="m_Name"/>
    </ui:VisualElement>
</UXML>

```



## Create the binding in C#
Create the binding in a C# script and make an explicit call to the `Bind()` method.
  1. Create a folder named `Editor`.
  2. In the **Editor** folder, create a C# script file named `SimpleBindingExampleUXML.cs`.
  3. Replace the contents of `SimpleBindingExampleUXML.cs` with the following:
```
using UnityEditor;
using UnityEngine;
using UnityEditor.UIElements;
using UnityEngine.UIElements;

namespace UIToolkitExamples
{
    public class SimpleBindingExampleUXML : EditorWindow
    {
        [SerializeField]
        VisualTreeAsset visualTree;

        [MenuItem("Window/UIToolkitExamples/Simple Binding Example UXML")]
        public static void ShowDefaultWindow()
        {
            var wnd = GetWindow<SimpleBindingExampleUXML>();
            wnd.titleContent = new GUIContent("Simple Binding UXML");
        }

        public void CreateGUI()
        {
            visualTree.CloneTree(rootVisualElement);
            OnSelectionChange();
        }

        public void OnSelectionChange()
        {
            GameObject selectedObject = Selection.activeObject as GameObject;
            if (selectedObject != null)
            {
                // Create the SerializedObject from the current selection
                SerializedObject so = new SerializedObject(selectedObject);
                // Bind it to the root of the hierarchy. It will find the right object to bind to.
                rootVisualElement.Bind(so);
            }
            else
            {
                // Unbind the object from the actual visual element
                rootVisualElement.Unbind();

                // Clear the TextField after the binding is removed
                var textField = rootVisualElement.Q<TextField>("GameObjectName");
                if (textField != null)
                {
                    textField.value = string.Empty;
                }
            }
        }
    }
}

```

  4. In the Project window, select `SimpleBindingExampleUXML.cs` and drag `binding_example.uxml` to the **Visual Tree** field in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).


## Test the binding
  1. In Unity, select **Window** > **UIToolkitExamples** > **Simple Binding Example UXML**. A custom Editor window appears with a text field.
  2. Select any GameObject in your scene. The name of the GameObject appears in your Editor window’s text field.
  3. If you change the name of the GameObject in the text field, the name of the GameObject changes.


## Additional resources
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)
  * [Bindable elements](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bindable-elements.html)
  * [Binding data type conversion](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-data-type-conversion.html)
  * [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-implementation-details.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-without-bindpath.html)
Bind without the binding path
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-inspector.html)
Create a binding with the Inspector
