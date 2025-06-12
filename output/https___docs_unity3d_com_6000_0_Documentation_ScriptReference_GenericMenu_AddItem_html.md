* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddItem.html

#  [GenericMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html).AddItem
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
## Declaration
public void AddItem([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, bool on, [GenericMenu.MenuFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.MenuFunction.html) func); 
### Parameters
Parameter | Description  
---|---  
content | The GUIContent to add as a menu item.  
on | Specifies whether to show the item is currently activated (i.e. a tick next to the item in the menu).  
func | The function to call when the menu item is selected.  
### Description
Add an item to the menu.
Additional resources: [GenericMenu.AddDisabledItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddDisabledItem.html), [GenericMenu.AddSeparator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddSeparator.html).
* * *
## Declaration
public void AddItem([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, bool on, [GenericMenu.MenuFunction2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.MenuFunction2.html) func, object userData); 
### Parameters
Parameter | Description  
---|---  
content | The GUIContent to add as a menu item.  
on | Specifies whether to show the item is currently activated (i.e. a tick next to the item in the menu).  
func | The function to call when the menu item is selected.  
userData | The data to pass to the function called when the item is selected.  
### Description
Add an item to the menu.
Additional resources: [GenericMenu.AddDisabledItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddDisabledItem.html), [GenericMenu.AddSeparator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddSeparator.html).
```
// This example shows how to create a context menu inside a custom EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class MyWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("TestContextMenu/Open Window")]
    public static void Init()
    {
        var window = GetWindow(typeof(MyWindow));
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 50, 250, 60);
        window.Show();
    }  
  
    public void Callback(object obj)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Selected: " + obj);
    }  
  
    public void OnGUI()
    {
        Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) evt = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) contextRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 100);  
  
        if (evt.type == EventType.ContextClick[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ContextClick.html))
        {
            Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) mousePos = evt.mousePosition;
            if (contextRect.Contains(mousePos))
            {
                // Now create the menu, add items and show it
                GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) menu = new GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html)();  
  
                menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("MenuItem1"), false, Callback, "item 1");
                menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("MenuItem2"), false, Callback, "item 2");
                menu.AddSeparator("");
                menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("SubMenu/MenuItem3"), false, Callback, "item 3");
                menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("SubMenu/MenuItem4"), false, Callback, "item 4");
                menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("SubMenu/MenuItem5"), false, Callback, "item 5");
                menu.AddSeparator("SubMenu/");
                menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("SubMenu/MenuItem6"), false, Callback, "item 6");  
  
                menu.ShowAsContext();  
  
                evt.Use();
            }
        }
    }
}

```

```
// This example shows how to create a context menu inside a custom EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class MyWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("TestContextMenu/Open Window")]
    public static void Init()
    {
        var window = GetWindow(typeof(MyWindow));
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 50, 250, 60);
        window.Show();
    }  
  
    bool item2enabled = false;
    public void Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)()
    {
        item2enabled = !item2enabled;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("item2enabled: " + item2enabled);
    }  
  
    public void Item2Callback()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) 2 Selected");
    }  
  
    public void OnGUI()
    {
        Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) evt = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) contextRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 100);  
  
        if (evt.type == EventType.ContextClick[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ContextClick.html))
        {
            Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) mousePos = evt.mousePosition;
            if (contextRect.Contains(mousePos))
            {
                // Now create the menu, add items and show it
                GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) menu = new GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html)();  
  
                menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) item 2"), item2enabled, Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html));
                if (item2enabled)
                {
                    menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) 2"), false, Item2Callback);
                }
                else
                {
                    menu.AddDisabledItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) 2"));
                }  
  
                menu.ShowAsContext();  
  
                evt.Use();
            }
        }
    }
}

```

* * *
