* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-bindable-custom-control.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Structure UI examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-examples.html)
  * Create a bindable custom control


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-slide-toggle.html)
Create a slide toggle custom control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-style-custom-control.html)
Create a custom style for a custom control
# Create a bindable custom control
**Version** : 2023.2+
This example demonstrates how to create a bindable custom control in a custom Editor window.
## Example overview
This example creates a custom control bound to a property with the double data type. You can adapt this example to bind to properties with other data types such as a string or an integer.
![A script in the Unity Editor with a custom control.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/custom-control-binding-example.png) A script in the Unity Editor with a custom control.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/2023.2/create-bindable-custom-control).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * [Visual Tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree)
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)


## Create the custom control class
Create a C# class to define the custom control.
  1. Create a Unity project with any template.
  2. Create a folder named `ExampleField` to store your files.
  3. In the `ExampleField` folder, create a C# script named `ExampleField.cs` and replace its content with the following:

```
using UnityEngine.UIElements;

namespace UIToolkitExamples
{
    // ExampleField inherits from BaseField with the double type. ExampleField's underlying value, then, is a double.
    [UxmlElement]
    public partial class ExampleField : BaseField<double>
    {
        Label m_Input;

        // Default constructor is required for compatibility with UXML factory
        public ExampleField() : this(null)
        {

        }

        // Main constructor accepts label parameter to mimic BaseField constructor.
        // Second argument to base constructor is the input element, the one that displays the value this field is
        // bound to.
        public ExampleField(string label) : base(label, new Label() { })
        {
            // This is the input element instantiated for the base constructor.
            m_Input = this.Q<Label>(className: inputUssClassName);
        }

        // SetValueWithoutNotify needs to be overridden by calling the base version and then making a change to the
        // underlying value be reflected in the input element.
        public override void SetValueWithoutNotify(double newValue)
        {
            base.SetValueWithoutNotify(newValue);

            m_Input.text = value.ToString("N");
        }
    }
}

```

## Use the custom control in a UXML file
  1. In the `ExampleField` folder, create a UI Document named `ExampleField.uxml`.
  2. Open `ExampleField.uxml` in a text editor and replace its contents with the following:

```
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:example="UIToolkitExamples">
    <example:ExampleField label="Binding Target" binding-path="m_Value" />
</ui:UXML>

```

## Create the class for the binding target
  1. In Unity, double-click `ExampleField.uxml` to open it in the UI Builder. The ExampleField displays in the Hierarchy window and is visualized in the **Viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport). If you select the ExampleField in the Hierarchy window, the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window shows the values assigned to the **Binding Path** and **Label** boxes.
  2. In the `ExampleField` folder, create a C# script named `ExampleFieldComponent.cs` and replace its contents with the following:

```
using UnityEngine;

namespace UIToolkitExamples
{
    public class ExampleFieldComponent : MonoBehaviour
    {
        [SerializeField]
        double m_Value;
    }
}

```

## Create the custom Editor for the binding target
  1. In the `ExampleField` folder, create a folder named `Editor`.
  2. In the `Editor` folder, create a C# script named `ExampleFieldCustomEditor.cs` and replace its contents with the following:

```
using UnityEditor;
using UnityEngine.UIElements;
using UnityEngine;

namespace UIToolkitExamples
{
    [CustomEditor(typeof(ExampleFieldComponent))]
    public class ExampleFieldCustomEditor : Editor
    {
        [SerializeField]
        VisualTreeAsset m_Uxml;

        public override VisualElement CreateInspectorGUI()
        {
            var parent = new VisualElement();

            m_Uxml?.CloneTree(parent);

            return parent;
        }
    }
}

```

## Test the example
  1. In Unity, select `ExampleFieldCustomEditor.cs` in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow).
  2. Drag `ExampleField.uxml` into the **Uxml** box in the Inspector window.
  3. Add an empty **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  4. Add the `ExampleFieldComponent` component to the GameObject. The custom control appears in the Inspector with the default value of `0` for the Binding Target. If you change the value of the underlying double property, the UI reflects that change.


## Additional resources
  * [Custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-slide-toggle.html)
Create a slide toggle custom control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-style-custom-control.html)
Create a custom style for a custom control
