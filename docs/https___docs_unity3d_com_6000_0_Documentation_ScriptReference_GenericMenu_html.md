* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html

# GenericMenu
class in UnityEditor
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
GenericMenu lets you create custom context menus and dropdown menus.
The example below opens an Editor window with a button. Clicking the button displays a context menu, which lets you change the color to apply to the GUI in the window. Copy the example's contents into a script called GenericMenuExample.cs and put it into a folder in your project called Editor.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GenericMenu.png).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class GenericMenuExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    // open the window from the menu item Example -> GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow<GenericMenuExample>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50f, 50f, 200f, 24f);
        window.Show();
    }  
  
    // serialize field on window so its value will be saved when Unity recompiles
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) m_Color = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);  
  
    void OnEnable()
    {
        titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)");
    }  
  
    // a method to simplify adding menu items
    void AddMenuItemForColor(GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) menu, string menuPath, Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color)
    {
        // the menu item is marked as selected if it matches the current value of m_Color
        menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)(menuPath), m_Color.Equals(color), OnColorSelected, color);
    }  
  
    // the GenericMenu.MenuFunction2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.MenuFunction2.html) event handler for when a menu item is selected
    void OnColorSelected(object color)
    {
        m_Color = (Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html))color;
    }  
  
    void OnGUI()
    {
        // set the GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) to use the color stored in m_Color
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = m_Color;  
  
        // display the GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) when pressing a button
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Select GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)"))
        {
            // create the menu and add items to it
            GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) menu = new GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html)();  
  
            // forward slashes nest menu items under submenus
            AddMenuItemForColor(menu, "RGB/Red", Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
            AddMenuItemForColor(menu, "RGB/Green", Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html));
            AddMenuItemForColor(menu, "RGB/Blue", Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html));  
  
            // an empty string will create a separator at the top level
            menu.AddSeparator("");  
  
            AddMenuItemForColor(menu, "CMYK/Cyan", Color.cyan[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-cyan.html));
            AddMenuItemForColor(menu, "CMYK/Yellow", Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html));
            AddMenuItemForColor(menu, "CMYK/Magenta", Color.magenta[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-magenta.html));
            // a trailing slash will nest a separator in a submenu
            menu.AddSeparator("CMYK/");
            AddMenuItemForColor(menu, "CMYK/Black", Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html));  
  
            menu.AddSeparator("");  
  
            AddMenuItemForColor(menu, "White", Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html));  
  
            // display the menu
            menu.ShowAsContext();
        }
    }
}

```

### Properties
Property | Description  
---|---  
[allowDuplicateNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu-allowDuplicateNames.html) | Allow the menu to have multiple items with the same name.  
### Public Methods
Method | Description  
---|---  
[AddDisabledItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddDisabledItem.html) | Add a disabled item to the menu.  
[AddItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddItem.html) | Add an item to the menu.  
[AddSeparator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddSeparator.html) | Add a seperator item to the menu.  
[DropDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.DropDown.html) | Show the menu at the given screen rect.  
[GetItemCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.GetItemCount.html) | Get number of items in the menu.  
[ShowAsContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.ShowAsContext.html) | Show the menu under the mouse when right-clicked.  
### Delegates
Delegate | Description  
---|---  
[MenuFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.MenuFunction.html) | Callback function, called when a menu item is selected.  
[MenuFunction2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.MenuFunction2.html) | Callback function with user data, called when a menu item is selected.  
* * *
