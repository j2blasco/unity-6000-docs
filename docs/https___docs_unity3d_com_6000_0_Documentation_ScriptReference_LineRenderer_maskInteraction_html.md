* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer-maskInteraction.html

#  [LineRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html).maskInteraction
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html "Go to LineRenderer Component in the Manual")
[SpriteMaskInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html) maskInteraction; 
### Description
Specifies how the LineRenderer interacts with [SpriteMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMask.html).
By default, lines do not interact with SpriteMasks and are visible regardless of whether you assign a SpriteMask or not. You can make the LineRenderer visible either inside or outside a SpriteMask. To do the former, set this to [SpriteMaskInteraction.VisibleInsideMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.VisibleInsideMask.html). To do the latter, set this to [SpriteMaskInteraction.VisibleOutsideMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.VisibleOutsideMask.html). Additional resources: [SpriteMaskInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html).
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html) r;
    public SpriteMaskInteraction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html) maskInteraction;  
  
    void Start()
    {
        r = GetComponent<LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        r.maskInteraction = maskInteraction;
    }  
  
    void OnGUI()
    {
        maskInteraction = (SpriteMaskInteraction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html))GUI.SelectionGrid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SelectionGrid.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 900, 30), (int)maskInteraction, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)[] { new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("No Masking"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Visible Inside Mask"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Visible Outside Mask") }, 3);
    }
}

```

* * *
