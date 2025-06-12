* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-csharp.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)
  * Bind with binding path in C# script


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)
Binding examples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-without-bindpath.html)
Bind without the binding path
# Bind with binding path in C# script
**Version** : 2021.3+
This example demonstrates how to bind with the binding path in a C# script.
## Example overview
This examples create a custom Editor window to change the name of a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). 
![Displays a Unity Editor window with a custom field to change the name of a GameObject.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie_simple_binding.png) Displays a Unity Editor window with a custom field to change the name of a GameObject.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/bind-with-binding-path).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [`bindingPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement-bindingPath.html)
  * [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html)


## Bind with the binding path
Create a custom Editor window in C# with a `TextField`. Set the binding path to the name property of a GameObject and make an explicit call to the `Bind()` method.
  1. Create a project in Unity with any template.
  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `bind-with-binding-path` folder to store your file.
  3. In the **bind-with-binding-path** folder, create a folder named `Editor`.
  4. In the **Editor** folder, create a C# script named `SimpleBindingExample.cs` and replace its contents with the following:
```
using UnityEditor;
using UnityEngine;
using UnityEditor.UIElements;
using UnityEngine.UIElements;

namespace UIToolkitExamples
{
    public class SimpleBindingExample : EditorWindow
    {
        TextField m_ObjectNameBinding;

        [MenuItem("Window/UIToolkitExamples/Simple Binding Example")]
        public static void ShowDefaultWindow()
        {
            var wnd = GetWindow<SimpleBindingExample>();
            wnd.titleContent = new GUIContent("Simple Binding");
        }

        public void CreateGUI()
        {
            m_ObjectNameBinding = new TextField("Object Name Binding");
            // Note: the "name" property of a GameObject is "m_Name" in serialization.
            m_ObjectNameBinding.bindingPath = "m_Name";
            rootVisualElement.Add(m_ObjectNameBinding);
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

                // Alternatively you can instead bind it to the TextField itself.
                // m_ObjectNameBinding.Bind(so);
            }
            else
            {
                // Unbind the object from the actual visual element that was bound.
                rootVisualElement.Unbind();
                // If you bound the TextField itself, you'd do this instead:
                // m_ObjectNameBinding.Unbind();

                // Clear the TextField after the binding is removed
                m_ObjectNameBinding.value = "";
            }
        }
    }
}

```



## Test the binding
  1. In Unity, select **Window** > **UIToolkitExamples** > **Simple Binding Example**. A custom Editor window appears with a text field.
  2. Select any GameObject in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). The name of the GameObject appears in your Editor window’s text field. If you change the name of the GameObject in the text field, the name of the GameObject changes.


## Additional resources
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)
  * [Bindable elements](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bindable-elements.html)
  * [Binding data type conversion](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-data-type-conversion.html)
  * [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-implementation-details.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)
Binding examples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-without-bindpath.html)
Bind without the binding path
