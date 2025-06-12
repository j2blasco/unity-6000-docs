* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetFlowLayoutedRects.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).GetFlowLayoutedRects
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
public static List<Rect> GetFlowLayoutedRects([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, float horizontalSpacing, float verticalSpacing, List<string> items); 
### Parameters
Parameter | Description  
---|---  
rect | Area where to layout the items.  
style | Style for the items.  
horizontalSpacing | Extra horizontal spacing between successive items.  
verticalSpacing | Extra vertical spacing between item rows.  
items | Strings to layout.  
### Returns
**List <Rect>** List of rectangles for the passed items. 
### Description
Layout list of string items left to right, top to bottom in the given area.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIUtilityGetFlowLayoutedRects.png)   
_Example of buttons positioned with GetFlowLayoutedRects._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Collections.Generic;  
  
public class MyWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/My Window")]
    static void OpenMyWindow()
    {
        EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<MyWindow>(true);
    }  
  
    void OnGUI()
    {
        // area to layout our items in
        var rect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, position.width - 20, position.height - 20);
        // items to layout
        var items = new List<string>
        {
            "One button", "Another button", "Yet another", "Hey there's more", "More!"
        };
        // get resulting rectangles of items
        var style = EditorStyles.miniButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-miniButton.html);
        var boxes = EditorGUIUtility.GetFlowLayoutedRects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetFlowLayoutedRects.html)(rect, style, 4, 4, items);
        // do actual UI for them
        for (var i = 0; i < boxes.Count; ++i)
        {
            GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(boxes[i], items[i], style);
        }
    }
}

```

* * *
