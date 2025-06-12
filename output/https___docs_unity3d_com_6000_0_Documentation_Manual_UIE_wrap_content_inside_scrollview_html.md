* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-wrap-content-inside-scrollview.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Structure UI examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-examples.html)
  * Wrap content inside a scroll view


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateRuntimeUI.html)
Create a list view runtime UI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-tabbed-menu-for-runtime.html)
Create a tabbed menu
# Wrap content inside a scroll view
**Version** : 2021.3+
This example demonstrates how to use styles to wrap content inside a scroll view. For demonstration purposes, this guide is for the Editor UI. However, the instructions on styling the scroll view also apply to runtime UI.
## Example overview
This example creates a custom Editor window with two scroll views:
  * One has a label inside it. The text of the label displays in a line and displays to the next line if the line is full.
  * One has 15 buttons inside it. The buttons display in a row and display to the next line if the row is full.

![A custom Editor window that wraps text and buttons.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uxml/scroll-view-wrapping.png) A custom Editor window that wraps text and buttons.
To wrap text of the label inside the scroll view, [apply style to the Label control, and use a VisualElement to holder the label](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html#wrap-text-of-elements-inside-scrollview).
To wrap elements inside the scroll view, [apply style to the content container of the scroll view](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html#wrap-elements-inside-scrollview).
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/wrap-content-inside-scrollview).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * [ScrollView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html)A UI Control which displays a large set of Controls in a viewable area that you can see by using a scrollbar. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScrollView)


## Create the custom Editor window
To try the example, first create a custom Editor window with some default content.
  1. Create a Unity project with any template.
  2. Right-click in the Project window, and then select **Create** > **UI Toolkit** > **Editor Window**.
  3. In the **C#** box of the **UI Toolkit Editor Window Creator** window, enter `ScrollViewExample`.
  4. Select **Confirm**. This creates three files: `ScrollViewExample.cs`, `ScrollViewExample.uxml`, and `ScrollViewExample.uss`.


## Create the scroll view
Define the basic scroll view structure in the UI Document (UXML file), style the **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) in the USS file, and add 15 buttons inside the second scroll view in the C# script.
  1. Replace the content of `ScrollViewExample.uxml` with the following:
```
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xsi="http://www.w3.org/2001/XMLSchema-instance" engine="UnityEngine.UIElements" editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../../UIElementsSchema/UIElements.xsd" editor-extension-mode="True">
    <Style src="ScrollViewExample.uss" />
    <ui:ScrollView>
        <ui:VisualElement>
            <ui:Label text="ScrollView Wrapping Example" />
        </ui:VisualElement>
    </ui:ScrollView>
    <ui:ScrollView name="scroll-view-wrap-example" />
</ui:UXML>

```

  2. Replace the content of `ScrollViewExample.uss` with the following:
```
Label {
    font-size: 20px;
    -unity-font-style: bold;
    color: rgb(68, 138, 255);
    /* Style to wrap text of the label */
    white-space: normal;
}

/* Style to wrap elements inside the scroll view */
#scroll-view-wrap-example .unity-scroll-view__content-container {
    flex-direction: row;
    flex-wrap: wrap;
}

Button {
    width: 50px;
    height: 50px;
}

```

  3. Replace the content of `ScrollViewExample.cs` with the following:
```
using UnityEditor;
using UnityEngine;
using UnityEngine.UIElements;
using UnityEditor.UIElements;

public class ScrollViewExample : EditorWindow
{
    [MenuItem("Example/ScrollView Wrapping Example")]
    public static void ShowExample()
    {
        var wnd = GetWindow<ScrollViewExample>();
    }

    public void CreateGUI()
    {
        // Each editor window contains a root VisualElement object.
        VisualElement root = rootVisualElement;

        // Import UXML.
        var visualTree = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Assets/Editor/ScrollViewExample.uxml");
        VisualElement ScrollViewExample = visualTree.Instantiate();
        root.Add(ScrollViewExample);

        // Find the scroll view by name.
        VisualElement scrollview = root.Query<ScrollView>("scroll-view-wrap-example");
            
        // Add 15 buttons inside the scroll view.
        for (int i = 0; i < 15; i++) 
        {
            Button button = new Button();
            button.text = "Button";
            scrollview.Add(button);
        }
    }
}

```

  4. To test the scroll view wrapping, from the menu, select **Example** > **ScrollView Wrapping Example**.


## Additional resources
  * [UQuery](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UQuery.html)
  * [`ScrollView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateRuntimeUI.html)
Create a list view runtime UI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-tabbed-menu-for-runtime.html)
Create a tabbed menu
