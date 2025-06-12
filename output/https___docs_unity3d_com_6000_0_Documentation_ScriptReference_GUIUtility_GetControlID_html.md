* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetControlID.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).GetControlID
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
public static int GetControlID([FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focus); 
## Declaration
public static int GetControlID([FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focus, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position); 
### Description
Get a unique ID for a control.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Prints a not used ID that can be assigned to a control  
  
    void OnGUI()
    {
        // Gets a ID for a control that cannot receive keyboard focus (A button)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Available id: " + GUIUtility.GetControlID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetControlID.html)(FocusType.Passive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.Passive.html)));
    }
}

```

* * *
## Declaration
public static int GetControlID(int hint, [FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focus); 
## Declaration
public static int GetControlID(int hint, [FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focusType, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect); 
### Description
Get a unique ID for a control, using an integer as a hint to help ensure correct matching of IDs to controls.
* * *
## Declaration
public static int GetControlID([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) contents, [FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focus); 
## Declaration
public static int GetControlID([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) contents, [FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focus, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position); 
### Description
Get a unique ID for a control, using a the label content as a hint to help ensure correct matching of IDs to controls.
* * *
