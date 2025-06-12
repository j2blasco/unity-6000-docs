* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-y.html

#  [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html).y
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
y; 
### Description
The Y coordinate of the rectangle.
This value is the same as [yMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-yMin.html), but setting it will move the rectangle rather than resize it.
```
using UnityEngine;  
  
public class RectExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 50, 30);
        // prints: y = 10
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("y = " + rect.y);  
  
        rect.y = 20;
        // prints: (x:10, y:20, width:50, height:30)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(rect);
    }
}

```

* * *
