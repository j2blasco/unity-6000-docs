* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).GetWindow
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
public static [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) GetWindow(Type windowType, bool utility = false, string title = null, bool focus = true); 
### Parameters
Parameter | Description  
---|---  
windowType | The type of the window. Must derive from EditorWindow.  
utility | Set this to true, to create a floating utility window, false to create a normal window.  
title | If GetWindow creates a new window, it will get this title. If this value is null, use the class name as title.  
focus | Whether to give the window focus, if it already exists. (If GetWindow creates a new window, it will always get focus).  
### Returns
**EditorWindow** An EditorWindow instance of `windowType`. 
### Description
Returns the first EditorWindow of type `windowType` which is currently on the screen.
If there is none, creates and shows new window and returns the instance of it.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GetWindowEx.png)  
_Simple Empty non-dockable window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);

// Simple script that creates a new non-dockable window.
public class EditorWindowTest : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) simple Window")]
    static void Initialize()
    {
        var window = (EditorWindowTest)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(EditorWindowTest), true, "My Empty Window");
    }
}

```

* * *
## Declaration
public static T GetWindow(); 
## Declaration
public static T GetWindow(bool utility); 
## Declaration
public static T GetWindow(bool utility, string title); 
## Declaration
public static T GetWindow(string title); 
## Declaration
public static T GetWindow(string title, bool focus); 
## Declaration
public static T GetWindow(bool utility, string title, bool focus); 
### Parameters
Parameter | Description  
---|---  
T | The type of the window. Must derive from EditorWindow.  
utility | Set this to true, to create a floating utility window, false to create a normal window.  
title | If GetWindow creates a new window, it will get this title. If this value is null, use the class name as title.  
focus | Whether to give the window focus, if it already exists. (If GetWindow creates a new window, it will always get focus).  
### Returns
**T** An EditorWindow instance of type `T`. 
### Description
Returns the first EditorWindow of type `T` which is currently on the screen.
If there is none, creates and shows new window and returns the instance of it.
* * *
## Declaration
public static T GetWindow(params Type[] desiredDockNextTo); 
## Declaration
public static T GetWindow(string title, params Type[] desiredDockNextTo); 
## Declaration
public static T GetWindow(string title, bool focus, params Type[] desiredDockNextTo); 
### Parameters
Parameter | Description  
---|---  
T | The type of the window. Must derive from EditorWindow.  
title | If GetWindow creates a new window, it will get this title. If this value is null, use the class name as title.  
desiredDockNextTo | An array of EditorWindow types that the window will attempt to dock onto.  
focus | Whether to give the window focus, if it already exists. (If GetWindow creates a new window, it will always get focus).  
### Returns
**T** An EditorWindow instance of type `T`. 
### Description
Returns the first EditorWindow of type `T` which is currently on the screen.
If there is none, creates and shows new window and returns the instance of it. The created window will attempt to be docked next to the first founds specified window type.
* * *
