* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-operator_add.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).operator +
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) operator +([Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) a, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) b); 
### Description
Adds two colors together. Each component is added separately.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) magenta = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html) + Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
    }
}

```

* * *
