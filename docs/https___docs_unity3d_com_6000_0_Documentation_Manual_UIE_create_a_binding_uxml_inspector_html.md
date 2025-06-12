* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-inspector.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)
  * Create a binding with the Inspector


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-bind.html)
Bind with UXML and C# script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-nested-properties.html)
Bind to nested properties
# Create a binding with the Inspector
**Version** : 2021.3+
The example demonstrates how to create bindings among a custom **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), a custom Editor, and serialized objects. 
## Example overview
This example creates the following:
  * A custom Inspector UI component with two fields that bind to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s name and the scale of a USS transform.
  * A custom Editor window that creates the same bindings inside an `InspectorElement`.

![Displays a Unity Editor window and Inspector with a custom field to change the name of a GameObject, and another field to adjust its size.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie_bind_inspector.png) Displays a Unity Editor window and Inspector with a custom field to change the name of a GameObject, and another field to adjust its size.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/create-a-binding-inspector).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [Visual Tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree)
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [`CreateInspectorGUI`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html)
  * [`InspectorElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html)


## Define the custom Inspector component
Define a custom Inspector UI class called `TankScript`, style it with USS, and set the **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) and the binding path in UXML. 
  1. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `create-a-binding-inspector` to store all your files.
  2. Create a C# script named `TankScript.cs` and replace its content with the following:
```
using UnityEngine;

[ExecuteInEditMode]
public class TankScript : MonoBehaviour
{
    public string tankName = "Tank";
    public float tankSize = 1;

    private void Update()
    {
        gameObject.name = tankName;
        gameObject.transform.localScale = new Vector3(tankSize, tankSize, tankSize);
    }
}

```

  3. In the **create-a-binding-inspector** folder, create a folder named `Editor`.
  4. In the **Editor** folder, create a USS file named `tank_inspector_styles.uss` and replace its contents with the following:
```
.container {
    background-color: rgb(80, 80, 80);
    flex-direction: column;
}
Label {
    background-color: rgb(80, 80, 80);
}
TextField:hover {
    background-color: rgb(255, 255, 0);
}
FloatField {
    background-color: rgb(0, 0, 255);
}

```

  5. Create a UXML file named `tank_inspector_uxml.uxml` and replace its contents with the following:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:ue="UnityEditor.UIElements">
    <Style src="tank_inspector_styles.uss" />
    <VisualElement name="row" class="container">
        <Label text="Tank Script - Custom Inspector" />
        <ue:PropertyField binding-path="tankName" name="tank-name-field" />
        <ue:PropertyField binding-path="tankSize" name="tank-size-field" />
    </VisualElement>
</UXML>

```



## Create the Inspector UI with binding
Create a C# script to register the custom Inspector for `TankScript`. You don’t need to call the `Bind()` method as binding in the Inspector window is implicit.
  1. Create a C# script named `TankEditor.cs` and replace its contents with the following:
```
using UnityEditor;
using UnityEngine;
using UnityEngine.UIElements;

[CustomEditor(typeof(TankScript))]
public class TankEditor : Editor
{
    [SerializeField]
    VisualTreeAsset visualTree;

    public override VisualElement CreateInspectorGUI()
    {
        var uxmlVE = visualTree.CloneTree();
        return uxmlVE;
    }
}

```

  2. In the Project window, select `TankEditor.cs`.
  3. Drag `tank_inspector_uxml.uxml` to **Visual Tree** in the Inspector.
  4. Drag `tank_inspector_styles.uss` to **Style Sheet** in the Inspector.


## Test the first binding
  1. In Unity, add an empty GameObject to a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  2. Select the GameObject and drag `TankScript.cs` to **Add Component** in the Inspector. This generates the **Tank Script** component in the Inspector.
  3. In **Tank Script** , you can change the name of the Tank in the **Tank Name** box, and change the Transform scale value in the **Tank Size** box.


## Bind with `InspectorElement`
Create a custom Editor window with two fields that bind to the `TankScript` object. Create a C# script that calls the [`InspectorElement` constructor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement-ctor.html). The [`InspectorElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html) creates the UI and automatically binds the UI to objects.
  1. Create a C# file named `SimpleBindingExampleInspectorElement.cs` and replace its contents with the following:
```
using UnityEditor;
using UnityEngine;
using UnityEditor.UIElements;
    
namespace UIToolkitExamples
{
    public class SimpleBindingExampleInspectorElement : EditorWindow
    {
        [MenuItem("Window/UIToolkitExamples/Simple Binding Example Inspector Element")]
        public static void ShowDefaultWindow()
        {
            var wnd = GetWindow<SimpleBindingExampleInspectorElement>();
            wnd.titleContent = new GUIContent("Simple Binding with Inspector Element");
        }
    
        TankScript m_Tank;
        public void OnEnable()
        {
            m_Tank = FindObjectOfType<TankScript>();
            if (m_Tank == null)
                return;
    
            var inspector = new InspectorElement(m_Tank);
            rootVisualElement.Add(inspector);
        }
    }
}

```



## Test the second binding
  1. In Unity, select **Window** > **UIToolkitExamples** > **Simple Binding Example Inspector Element**.
  2. In the Editor window, if you change the values in the fields, the values in the Inspector change, and vice versa.


## Additional resources
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)
  * [Bindable elements](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bindable-elements.html)
  * [Binding data type conversion](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-data-type-conversion.html)
  * [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-implementation-details.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-bind.html)
Bind with UXML and C# script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-nested-properties.html)
Bind to nested properties
