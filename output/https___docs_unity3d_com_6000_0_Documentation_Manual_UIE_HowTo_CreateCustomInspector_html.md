* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateCustomInspector.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Support for Editor UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-editor-ui.html)
  * Create a custom Inspector


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateEditorWindow.html)
Create a custom Editor window with C# script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/create-default-inspector.html)
Create a default Inspector
# Create a custom Inspector
**Version** : 2022.3+
Although there is a default **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) for your MonoBehaviours and ScriptableObjects, you might want to write a custom Inspector for your classes. A custom Inspector can help you do the following:
  * Create a more user-friendly representation of script properties.
  * Organize and group properties together.
  * Display or hide sections of the UI depending on the user’s choices.
  * Provide additional information about the meaning of individual settings and properties.


## Example overview
This example creates a custom Inspector for a MonoBehaviour class. It uses both C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) and UI Builder to create the UI. The custom Inspector also features a custom **property drawer** A Unity feature that allows you to customize the look of certain controls in the Inspector window by using attributes on your scripts, or by controlling how a specific Serializable class should look [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-PropertyDrawers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PropertyDrawer).
The custom Inspector displays the properties of a `Car` class, including the make, year built, color, and a list of tires. The Inspector uses a PropertyField control to display the properties of the `Car` class, and a custom property drawer to display the properties of the `Tire` class.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/create-a-custom-inspector).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [Visual Tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * [Foldout](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Foldout.html)
  * [PropertyField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-PropertyField.html)
  * [PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html)


## Create a new MonoBehaviour
To create a custom Inspector, first define a custom class that inherits from a `MonoBehaviour`. The custom class represents a simple `car` with several properties.
  1. Create a project in Unity with any template.
  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `create-a-custom-inspector` to store all your files.
  3. Create a C# script named `Car.cs` with the following content:
```
using UnityEngine;

public class Car : MonoBehaviour
{
     public string m_Make = "Toyota";
     public int m_YearBuilt = 1980;
     public Color m_Color = Color.black;
}

```

  4. Create a new **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and attach the `Car` script component to it.
![Default Inspector for the Car object](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-defaultInspector.png) Default Inspector for the Car object


## Create a custom Inspector script
To create a custom Inspector for any serialized object, you need to create a class deriving from the [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) base class and add the [CustomEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html) attribute to it. This attribute lets Unity know which class this custom Inspector represents.
**Note** : The custom Inspector script must be in an `Editor` folder or an Editor-only assembly definition. This is because the `UnityEditor` namespace, which is essential for creating custom Inspectors, isn’t accessible outside these areas. If you try to create standalone builds without adhering to this, the build process fails.
  1. Create a folder named `Editor` inside the `create-a-custom-inspector` folder.
  2. Create a C# script named `Car_Inspector.cs` inside the `Editor` folder with the following content:
```
using UnityEditor;
using UnityEditor.UIElements;
using UnityEngine.UIElements;

[CustomEditor(typeof(Car))]
public class Car_Inspector : Editor
{
}

```

  3. Select the GameObject that has the `Car` component attached to it. The default Inspector displays. 
  4. To replace the default Inspector, inside the `Car_Inspector` class, add the following code to override [CreateInspectorGUI()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) and return a new **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) containing the UI:
```
public override VisualElement CreateInspectorGUI()
{
     // Create a new VisualElement to be the root of our Inspector UI.
     VisualElement myInspector = new VisualElement();

     // Add a simple label.
     myInspector.Add(new Label("This is a custom Inspector"));

     // Return the finished Inspector UI.
     return myInspector;
}

```

  5. Select the GameObject that has the `Car` component attached to it. The Inspector now displays the label `This is a custom Inspector` instead of the default Inspector.
![Custom Inspector with a label](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-label.png) Custom Inspector with a label


## Create a custom Inspector UI with UI Builder
You can create a custom Inspector UI with UI Builder, and use C# script to load and instantiate the UI from the UXML file.
  1. To open the UI Builder, select **Window** > **UI Toolkit** > **UI Builder**.
  2. Select **File** > **New** to create a new Visual Tree Asset.
![Custom Inspector with a label](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-uibuilder-new.png) Custom Inspector with a label
  3. To enable Editor-only controls in UI Builder, select the `<unsaved file>*.uxml` in the **Hierarchy** view and then select the **Editor Extension Authoring** checkbox.
![Custom Inspector with a label](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-uibuilder-extensionauthoring.png) Custom Inspector with a label
  4. Drag a label control from the **Library** to the **Hierarchy**. This adds a label control to the visual tree.
![Custom Inspector with a label](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-uibuilder-label.png) Custom Inspector with a label
  5. In the label control’s Inspector panel, update the label text.
![Custom Inspector with a label](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-uibuilder-text.png) Custom Inspector with a label
  6. Select **File** > **Save** and save the visual tree as `Car_Inspector_UXML.uxml` to the `Assets/create-a-custom-inspector` folder.


## Use UXML inside a custom Inspector
To use the UXML file you created inside your custom Inspector, assign the file to the custom Inspector, and load and clone it inside the `CreateInspectorGUI()` function and add it to the visual tree. To do this, you can use the [CloneTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualTreeAsset.CloneTree.html) method. You can pass any `VisualElement` as a parameter to act as a parent for the created elements.
  1. In `Car_Inspector.cs`, create a public variable for a `VisualTreeAsset` in your script and assign `Car_Inspector_UXML.uxml` to it.
```
public VisualTreeAsset m_InspectorUXML;

```

  2. Update the `CreateInspectorGUI()` method to load the UXML file and clone it into the visual tree. The finished `Car_Inspector.cs` file looks like the following:
```
 using UnityEditor;
 using UnityEditor.UIElements;
 using UnityEngine.UIElements;
     
 [CustomEditor(typeof(Car))]
 public class Car_Inspector : Editor
 {
     public VisualTreeAsset m_InspectorUXML;
     public override VisualElement CreateInspectorGUI()
     {
          // Create a new VisualElement to be the root of our Inspector UI.
         VisualElement myInspector = new VisualElement();
     
         // Add a simple label.
         myInspector.Add(new Label("This is a custom Inspector"));
     
         // Load the UXML file and clone its tree into the inspector.
         if (m_InspectorUXML != null)
         {
             VisualElement uxmlContent = m_InspectorUXML.CloneTree();
             myInspector.Add(uxmlContent);
         }
     
         // Return the finished Inspector UI.
         return myInspector;
     }
 }
     

```

  3. In the Inspector window of `Car_Inspector.cs`, assign the `Car_Inspector_UXML.uxml` file to the **Inspector UXML** field.
  4. Select the GameObject that has the `Car` component attached to it. The Inspector for the `Car` component now displays two labels: one through script, and one through UI Builder/UXML.
![Custom Inspector with two labels label](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-labels.png) Custom Inspector with two labels label


## Bind a text field
This custom Inspector displays all properties of the `Car` class. When you update the UI controls, the values inside the instance of the `Car` class change. To do so, add UI controls to the visual tree and bind them to the individual properties of the class.
To bind a control to a serialized property, assign the property to the `binding-path` field of the control. When you create a custom inspector, binding is automatic. [`CreateInspectorGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) does an implicit bind after you return your visual tree. For more information, refer to [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html).
  1. Double-click `Car_Inspector_UXML.uxml` to open it in UI Builder.
  2. Add a **TextField control** A TextField control displays a non-interactive piece of text to the user, such as a caption, label for other GUI controls, or instruction. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/gui-Controls.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextFieldcontrol).
![Add a text field to the UI](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-textfield.png) Add a text field to the UI
  3. In the Inspector panel of the TextField, set the label text to `Make of the car`.
  4. Set the binding path to `m_Make`.
![Bind a property to a control in UI Builder](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-binding.png) Bind a property to a control in UI Builder
  5. Add a style class `unity-base-field__aligned` to the **Style Class List** so that the text field aligns with other fields in the Inspector window. For more information, refer to [BaseField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
![Add a style class to the text field](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-custominspector-align-fields.png) Add a style class to the text field
  6. In UI Builder, select **File** > **Save**.
  7. Select the GameObject that has the `Car` component attached to it. The Inspector for the `car` component now displays the `Make of the car` text field. The text field is bound to the `m_Make` property of the `Car` class.
![Custom Inspector showing a text field](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-firstproperty.png) Custom Inspector showing a text field


## Bind a property field
To display the properties of the `Car` class, add a control for each field. The control must match the property type. For example, you must bind an `int` to an Integer field or an Integer Slider.
Instead of adding a specific control based on the property type, you can use the generic [PropertyField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html) control. This control works for most types of serialized properties and generates the default Inspector UI for this property type.
The advantage of a `PropertyField` is the Inspector UI automatically adjusts when you change the variable type inside your script. However, you can’t get a preview of the control inside the UI Builder because the control type is unknown until the visual tree is bound to a serialized object.
  1. Double-click `Car_Inspector_UXML.uxml` to open it in UI Builder.
  2. Add a PropertyField control for the `m_YearBuilt` properties of the `Car` class, and set the binding path and the label text.
![Add a property field in UI Builder](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-uibuilder-propertyfield.png) Add a property field in UI Builder
  3. Add a style class `unity-base-field__aligned` to the **Style Class List**.
  4. Add a PropertyField control for the `m_Color` properties of the `Car` class, and set the binding path and the label text.
  5. Add a style class `unity-base-field__aligned` to the **Style Class List**.
  6. In UI Builder, select **File** > **Save**.
  7. Select the GameObject that has the `Car` component to it. The Inspector for the `car` component now displays the `Year Built` and `Paint Color` property fields.
![Custom Inspector with property fields](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-customInspector.png) Custom Inspector with property fields


## Create a custom property drawer
A custom property drawer is a custom Inspector UI for a custom serializable class. If that serializable class is part of another serialized object, the custom UI displays that property in the Inspector. In UI Toolkit, the `PropertyField` control displays the custom property drawer for a field if one exists.
  1. In the `create-a-custom-inspector` folder, create a new script named `Tire.cs` with the following content:
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
    
[System.Serializable]
public class Tire
{
    public float m_AirPressure = 21.5f;
    public int m_ProfileDepth = 4;
}
    

```

  2. In `Car.cs`, add a list `Tire` to the `Car` class. The finished `Car.cs` file looks like the following:
```
using UnityEngine;
    
public class Car : MonoBehaviour
{
    public string m_Make = "Toyota";
    public int m_YearBuilt = 1980;
    public Color m_Color = Color.black;
    
    // This car has four tires.
    public Tire[] m_Tires = new Tire[4];
}

```

  3. The PropertyField control works with all standard property types and also supports custom serializable classes and arrays. To display the properties of the car’s tires, add another `PropertyField` in `Car_Inspector_UXML.uxml` and bind it to `m_Tires`. The finished `Car_Inspector_UXML.uxml` file looks like the following:
```
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" editor-extension-mode="True">
    <ui:TextField picking-mode="Ignore" label="Make of the car" value="filler text" binding-path="m_Make" class="unity-base-field__aligned" />
    <uie:PropertyField binding-path="m_YearBuilt" label="Year Built" class="unity-base-field__aligned" />
    <uie:PropertyField binding-path="m_Color" label="Paint Color" class="unity-base-field__aligned" />
    <uie:PropertyField label="Tires" binding-path="m_Tires" class="unity-base-field__aligned" />
</ui:UXML>
    

```

  4. Select the GameObject with the `Car` component. The Inspector for the `car` component now displays the `Tires` property field.
![Use a PropertyField control to display an array](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-serializable.png) Use a PropertyField control to display an array


## Create UI for the custom property drawer
You can create a custom property drawer to customize the look of the individual `Tire` elements in the list. Instead of deriving from the `Editor` base class, custom property drawers derive from the [`PropertyDrawer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html) class. 
You can use C# script or UXML to create the UI for the property. This example uses C# script to create the custom UI. To create UI for the custom property, override the [CreatePropertyGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.CreatePropertyGUI.html) method.
  1. In the `Editor` folder, Create a new script named `Tire_PropertyDrawer.cs` with the following content:
```
using UnityEditor;
using UnityEditor.UIElements;
using UnityEngine.UIElements;
    
[CustomPropertyDrawer(typeof(Tire))]
public class Tire_PropertyDrawer : PropertyDrawer
{
    public override VisualElement CreatePropertyGUI(SerializedProperty property)
    {
        // Create drawer UI using C#.
        var popup = new UnityEngine.UIElements.PopupWindow();
        popup.text = "Tire Details";
        popup.Add(new PropertyField(property.FindPropertyRelative("m_AirPressure"), "Air Pressure (psi)"));
        popup.Add(new PropertyField(property.FindPropertyRelative("m_ProfileDepth"), "Profile Depth (mm)"));
    
        // Return the finished UI.
        return popup;
    }
}

```

  2. Select the GameObject that has the `Car` component to it. The Inspector for the `car` component now displays the `Tires` property field with a custom property drawer.
![Inspector using a custom property drawer](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-customInspector-custompropertydrawer.png) Inspector using a custom property drawer


## Additional resources
  * [Create a default Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/create-default-inspector.html)
  * [Get started with UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-simple-ui-toolkit-workflow.html)
  * [PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html)
  * [FillDefaultInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.FillDefaultInspector.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateEditorWindow.html)
Create a custom Editor window with C# script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/create-default-inspector.html)
Create a default Inspector
