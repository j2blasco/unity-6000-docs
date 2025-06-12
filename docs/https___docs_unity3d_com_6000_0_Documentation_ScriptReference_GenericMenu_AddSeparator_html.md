* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddSeparator.html

#  [GenericMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html).AddSeparator
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
public void AddSeparator(string path); 
### Parameters
Parameter | Description  
---|---  
path | The path to the submenu, if adding a separator to a submenu. When adding a separator to the top level of a menu, use an empty string as the path.  
### Description
Add a seperator item to the menu.
Additional resources: [GenericMenu.AddItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddItem.html), [GenericMenu.AddDisabledItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.AddDisabledItem.html).
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
* * *
