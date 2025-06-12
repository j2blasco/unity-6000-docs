* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html

#  [Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html).current
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
[Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) current; 
### Description
The current event that's being processed right now.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Current detected event: " + Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html));
    }
}

```

* * *
