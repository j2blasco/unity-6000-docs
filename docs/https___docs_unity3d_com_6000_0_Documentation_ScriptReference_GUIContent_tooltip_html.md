* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-tooltip.html

#  [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html).tooltip
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
tooltip; 
### Description
The tooltip of this element.
The tooltip associated with this content. Read GUItooltip to get the tooltip of the gui element the user is currently over.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 20), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("A Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)", "This is the tooltip"));
        // If the user hovers the mouse over the button, the global tooltip gets set
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 40, 100, 40), GUI.tooltip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html));
    }
}

```

* * *
