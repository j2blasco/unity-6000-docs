* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndScrollView.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).EndScrollView
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
public static void EndScrollView(); 
### Description
End a scroll view begun with a call to BeginScrollView.
Additional resources: [GUILayout.BeginScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginScrollView.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutScrollView.png)  
_Scroll View in the Game View.._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // The variable to control where the scrollview 'looks' into its child elements.
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition;  
  
    // The string to display inside the scrollview. 2 buttons below add & clear this string.
    string longString = "This is a long-ish string";  
  
    void OnGUI()
    {
        // Begin a scroll view. All rects are calculated automatically -
        // it will use up any available screen space and make sure contents flow correctly.
        // This is kept small with the last two parameters to force scrollbars to appear.
        scrollPosition = GUILayout.BeginScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginScrollView.html)(
            scrollPosition, GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(100), GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(100));  
  
        // We just add a single label to go inside the scroll view. Note how the
        // scrollbars will work correctly with wordwrap.
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)(longString);  
  
        // Add a button to clear the string. This is inside the scroll area, so it
        // will be scrolled as well. Note how the button becomes narrower to make room
        // for the vertical scrollbar
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Clear"))
            longString = "";  
  
        // End the scrollview we began above.
        GUILayout.EndScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndScrollView.html)();  
  
        // Now we add a button outside the scrollview - this will be shown below
        // the scrolling area.
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Add More Text"))
            longString += "\nHere is another line";
    }
}

```

* * *
