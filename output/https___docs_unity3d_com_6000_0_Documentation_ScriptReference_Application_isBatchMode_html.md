* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isBatchMode.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).isBatchMode
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
isBatchMode; 
### Description
Returns true when Unity is launched with the **-batchmode** flag from the command line (Read Only).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (Application.isBatchMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isBatchMode.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("In BatchMode");
        }
    }
}

```

* * *
