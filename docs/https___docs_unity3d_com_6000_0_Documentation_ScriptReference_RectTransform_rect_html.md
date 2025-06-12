* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform-rect.html

#  [RectTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html).rect
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
[Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect; 
### Description
The calculated rectangle in the local space of the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).
Unity automatically attaches these to UI elements. Manipulate aspects of the rectangle in the Inspector such as the position, dimensions, rotation, and scale. This is read-only in a script.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html) rectTransform;  
  
    void Start()
    {
        //Fetch the RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        rectTransform = GetComponent<RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html)>();
    }  
  
    void OnGUI()
    {
        //The Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) shows the current Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) settings on the screen
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 150, 80), "Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) : " + rectTransform.rect);
    }
}

```

* * *
