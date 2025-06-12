* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle-axes.html

#  [PrimitiveBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.html).axes
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
[IMGUI.Controls.PrimitiveBoundsHandle.Axes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.Axes.html) axes; 
### Description
Flags specifying which axes should display control handles.
By default, all axes are enabled. You can use bitwise operations to enable or disable individual axes. Disabled axes are flattened out.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.IMGUI.Controls;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // create a 2D box handle that only works on the x- and y-axes
        BoxBoundsHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.BoxBoundsHandle.html) box = new BoxBoundsHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.BoxBoundsHandle.html)("MyBox".GetHashCode());
        box.axes = PrimitiveBoundsHandle.Axes.X[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.Axes.X.html) | PrimitiveBoundsHandle.Axes.Y[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.Axes.Y.html);
    }
}

```

* * *
