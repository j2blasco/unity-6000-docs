* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.html

# GenericDropdownMenu
class in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
GenericDropdownMenu allows you to display contextual menus with default textual options or any [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html). 
The GenericDropdownMenu is a generic implementation of a dropdown menu that you can use in both Editor UI and runtime UI.   
  
The following example creates a dropdown menu with three items. It displays the menu when the user clicks the button. The example also demonstrates how to set the width of the dropdown menu with the `DropDown` method. 
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;  
  
public class MenuExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/UI Toolkit/MenuExample")]
    public static void ShowExample()
    {
        MenuExample wnd = GetWindow<MenuExample>();
        wnd.titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("MenuExample");
    }
    public void CreateGUI()
    {
        VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) root = rootVisualElement;  
  
        // Create a button.
        var button = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        button.text = "Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)";
        button.style.width = 70;  
  
        // Create a dropdown menu with three items.
        var menu = new GenericDropdownMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.html)();
        menu.AddItem("Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) 1", false, a => { Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) 1 was selected"); }, null);
        menu.AddItem("Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) 2", false, a => { Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) 2 was selected"); }, null);
        menu.AddItem("Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) 3 has a very very long label", false, a => { Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) 3 was selected"); }, null);  
  
        // When the button is clicked, the dropdown menu is displayed aligned with the button's world boundaries.
        button.clicked += () =>
        {
            // The third and the fourth parameters of the DropDown set the width of the dropdown menu.
            // This sets the width of the dropdown menu to the width of the container.
            menu.DropDown(button.worldBound, button, false);
            // This sets the width of the dropdown menu to the width of the button.
            // menu.DropDown(button.worldBound, button, true, false);
            // This sets the width of the dropdown menu to the width of the longest item.
            // menu.DropDown(button.worldBound, button, true, true);
        };
         root.Add(button);
    }
}

```

### Static Properties
Property | Description  
---|---  
[checkmarkUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-checkmarkUssClassName.html) |  USS class name of separators in elements of this type.   
[containerInnerUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-containerInnerUssClassName.html) |  USS class name of inner containers in elements of this type.   
[containerOuterUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-containerOuterUssClassName.html) |  USS class name of outer containers in elements of this type.   
[contentWidthUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-contentWidthUssClassName.html) |  USS class name that's added when the GenericDropdownMenu fits the width of its content.   
[itemContentUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-itemContentUssClassName.html) |  USS class name of labels in elements of this type.   
[itemUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-itemUssClassName.html) |  USS class name of labels in elements of this type.   
[labelUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-labelUssClassName.html) |  USS class name of labels in elements of this type.   
[separatorUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-separatorUssClassName.html) |  USS class name of separators in elements of this type.   
[ussClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-ussClassName.html) |  USS class name of elements of this type.   
### Properties
Property | Description  
---|---  
[contentContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-contentContainer.html) |  Returns the content container for the GenericDropdownMenu. Allows users to create their own dropdown menu if they don't want to use the default implementation.   
### Constructors
Constructor | Description  
---|---  
[GenericDropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu-ctor.html) |  Initializes and returns an instance of GenericDropdownMenu.   
### Public Methods
Method | Description  
---|---  
[AddDisabledItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.AddDisabledItem.html) |  Adds a disabled item to this menu using a default VisualElement.   
[AddItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.AddItem.html) |  Adds an item to this menu using a default VisualElement.   
[AddSeparator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.AddSeparator.html) |  Adds a visual separator after the previously added items in this menu.   
[DropDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.DropDown.html) |  Displays the menu at the specified position.   
* * *
