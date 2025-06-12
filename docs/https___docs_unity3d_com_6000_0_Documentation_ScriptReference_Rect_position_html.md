* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-position.html

#  [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html).position
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position; 
### Description
The X and Y position of the rectangle.
This is the same as [min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-min.html), except that setting it will move the rectangle rather than resize it.
```
using UnityEngine;  
  
// Show Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html), the position selected randomly.  
  
public class RectExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect;  
  
    void Start()
    {
        rect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(600 * Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html), 450 * Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html), 200, 150);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)("space"))
        {
            rect.position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(600 * Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html), 450 * Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html));
        }
    }  
  
    // display a rectangle
    void OnGUI()
    {
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(rect, "");
    }
}

```

* * *
