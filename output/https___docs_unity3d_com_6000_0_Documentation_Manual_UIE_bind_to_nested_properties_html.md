* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-nested-properties.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)
  * Bind to nested properties


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-inspector.html)
Create a binding with the Inspector
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-uxml-template.html)
Bind to a UXML template
# Bind to nested properties
**Version** : 2021.3+
This example demonstrates how to use the `binding-path` attribute of a BindableElement in UXML to bind fields to nested properties of a SerializedObject.
## Example overview
This example creates a custom **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) UI with the following:
  * Two fields that bind to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s name and the scale of a USS transform
  * Two fields that bind to nested properties of a SerializedObject

![A custom Inspector for a script, which has fields that map to GameObjects and SerializedObjects.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie_bind_nested_properties.png) A custom Inspector for a script, which has fields that map to GameObjects and SerializedObjects.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/bind-nested-properties).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [Visual Tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree)
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [`BindableElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement.html)
  * [`PropertyField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html)


## Create the destructible tank object
Create a C# script to define a class for a tank that has health values to make it destructible.
  1. Create a project in Unity with any template.
  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `bind-nested-properties` to store all the files.
  3. Create a C# script named `DestructibleTankScript.cs` and replace its content with the following:
```
using System;
using UnityEngine;
using UnityEngine.Serialization;

[Serializable]
public struct Health
{
    public int armor;
    public int life;
}

[ExecuteInEditMode]
public class DestructibleTankScript : MonoBehaviour
{
    public string tankName = "Tank";
    public float tankSize = 1;

    public Health health;

    private void Update()
    {
        gameObject.name = tankName;
        gameObject.transform.localScale = new Vector3(tankSize, tankSize, tankSize);
    }

    public void Reset()
    {
        health.armor = 100;
        health.life = 10;
    }
}

```



## Create the UXML and the Inspector UI
Create a UXML file with a BindableElement. Set the BindableElement’s `binding-path` to the `health` property and set each child element’s `binding-path` of the BindableElement to the `armor` and `life` properties of `health`.
  1. In the **bind-nested-properties** folder, create a folder named `Editor`.
  2. In the **Editor** folder, create a USS file named `tank_inspector_styles.uss` and replace its contents with the following:
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

  3. Create a UI Document named `destructible_tank_editor.uxml` and replace its contents with the following:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:ue="UnityEditor.UIElements">
    <Style src="tank_inspector_styles.uss"/>
    <VisualElement name="row" class="container">
        <Label text="Tank Script - Custom Inspector" />
        <ue:PropertyField binding-path="tankName" name="tank-name-field" />
        <ue:PropertyField binding-path="tankSize" name="tank-size-field" />
        <BindableElement binding-path="health">
            <ue:PropertyField binding-path="armor"/>
            <ue:PropertyField binding-path="life"/>
        </BindableElement>
    </VisualElement>
</UXML>

```



## Create the custom Editor
Create a C# script that registers a custom Editor for the `DestructibleTankScript`. 
  1. Create a C# script named `DestructibleTankEditor.cs` and replace its content with the following:
```
using UnityEditor;
using UnityEngine;
using UnityEngine.UIElements;

[CustomEditor(typeof(DestructibleTankScript))]
public class DestructibleTankEditor : Editor
{
    [SerializeField]
    VisualTreeAsset visualTreeAsset;

    public override VisualElement CreateInspectorGUI()
    {
        return visualTreeAsset.CloneTree();
    }
}

```

  2. Select `DestructibleTankEditor.cs` in the Project window.
  3. Drag `destructible_tank_editor.uxml` to **Visual Tree Asset** in the Inspector. 


## Test the binding
  1. In Unity, add an empty GameObject to a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  2. Select the GameObject.
  3. Add the **Destructible Tank Script** component in the Inspector. The **Armor** and **Life** fields are bound to the `health.armor` and `health.life` properties. If you change the values in the Inspector, the values of the underlying properties change.


## Additional resources
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)
  * [Bindable elements](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bindable-elements.html)
  * [Binding data type conversion](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-data-type-conversion.html)
  * [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-implementation-details.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-inspector.html)
Create a binding with the Inspector
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-uxml-template.html)
Bind to a UXML template
