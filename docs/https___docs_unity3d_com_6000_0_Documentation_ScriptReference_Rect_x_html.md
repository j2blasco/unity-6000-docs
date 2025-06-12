* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-x.html

#  [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html).x
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
x; 
### Description
The X coordinate of the rectangle.
This value is the same as [xMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-xMin.html), but setting it will move the rectangle rather than resize it.
```
using UnityEngine;  
  
public class RectExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Use this for initialization
    void Start()
    {
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 50, 30);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("x = " + rect.x); // -- prints: x = 10
        rect.x = 20;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(rect); // prints: (x:20, y:10, width:50, height:30)
    }
}

```

* * *
