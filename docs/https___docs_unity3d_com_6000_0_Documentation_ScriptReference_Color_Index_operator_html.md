* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Index_operator.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).this[int]
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
this[int]; 
### Description
Access the r, g, b,a components using [0], [1], [2], [3] respectively.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
    void Start()
    {
        //The same as color.g = 5
        color[1] = 5;
    }
}

```

* * *
