* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-custom-binding-bind-uss.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * [Runtime data binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-examples.html)
  * Create a custom binding to bind USS selectors


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-runtime-binding-type-converter.html)
Create a runtime binding with a type converter
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-list-view.html)
Bind ListView to a list with runtime binding
# Create a custom binding to bind USS selectors
**Version** : 2023.2+
This example shows how to create a custom binding that binds USS selectors to a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement).
## Example overview
This example creates a custom binding that assigns USS class selectors to each child element of a visual element based on the order of the child elements in the hierarchy. The first element always has the left round corner edge, while the last element always has the right round corner edge.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/2023.2/runtime-custom-binding).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)


## Create a custom binding type
Create a custom binding type that assigns USS classes based on the sibling index. The binding updates only when the sibling index changes.
  1. Create a project in Unity with any template.
  2. In the `Assets` folder of your project, create a C# script named `AddMenuUSSClass.cs` with the following content:
```
using UnityEngine.UIElements;
    
[UxmlObject]
public partial class AddMenuUssClass : CustomBinding
{
    protected override BindingResult Update(in BindingContext context)
    {
        // Assign USS classes based on the sibling index. The binding updates when the sibling index changes.
        var element = context.targetElement;
        var index = element.parent.IndexOf(element);
        element.EnableInClassList("menu-button--first", index == 0);
        element.EnableInClassList("menu-button--last", index == element.parent.childCount - 1);                
            
        return new BindingResult(BindingStatus.Success);
    }
}

```



## Create the UI and the binding
Generally speaking, you create a binding that binds to an existing property of the element. For demonstration purposes, this example creates a custom binding that binds to a property that doesn’t exist in the element. You must use UXML or C# to set up the binding that binds to a non-existing property. This example uses UXML to set up the binding.
  1. In the `Assets` folder of your project, create a USS file named `CustomBinding.uss` with the following contents:
```
.menu-button {
    flex-direction: row;
    height: 64px;
    align-items: center; 
    justify-content: center;
}
    
.menu-button--first {
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
    border-left-width: 2px;
}
    
.menu-button--last {
    border-top-right-radius: 15px;
    border-bottom-right-radius: 15px;
    border-right-width: 2px;
}
    
Button {
    margin: 0px;
    border-color: red;
}

```

  2. In the `Assets` folder of your project, create a UXML file named `CustomBinding.uxml` with the following contents:
```
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" editor-extension-mode="True">
    <ui:VisualElement class="menu-button">
        <ui:Button text="Bloub">
            <Bindings>
                <AddMenuUssClass property="add-menu-button-class" />
            </Bindings>
        </ui:Button>
        <ui:Button text="Bip">
            <Bindings>
                <AddMenuUssClass property="add-menu-button-class" />
            </Bindings>
        </ui:Button>
        <ui:Button text="Boop">
            <Bindings>
                <AddMenuUssClass property="add-menu-button-class" />
            </Bindings>
        </ui:Button>
    </ui:VisualElement>
</ui:UXML>

```

  3. Double-click the `CustomBinding.uxml` file to open it in UI Builder.
  4. In the StyleSheet panel, select **+** > **Add Existing USS** , and then select the `CustomBinding.uss` file.
  5. Save your changes. 


## Test the binding
To test the binding, change the order of the button elements in the UI Builder and observe the changes in the UI Builder **Viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport).
  1. Double-click the `CustomBinding.uxml` file to open it in UI Builder.
  2. In the Hierarchy panel, expand the root VisualElement to display the child elements, which are buttons.
  3. Drag and drop the buttons to change their order. The first button always has the left round corner edge, while the last button always has the right round corner edge.


## Additional resources
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * [Create runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-types.html)
  * [Create custom binding types](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-custom-types.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-runtime-binding-type-converter.html)
Create a runtime binding with a type converter
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-list-view.html)
Bind ListView to a list with runtime binding
