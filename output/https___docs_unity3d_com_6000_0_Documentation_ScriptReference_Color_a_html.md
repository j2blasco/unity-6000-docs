* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-a.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).a
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
a; 
### Description
Alpha component of the color (0 is transparent, 1 is opaque).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);  
  
    void Start()
    {
        color.a = 0.42f;
    }
}

```

* * *
