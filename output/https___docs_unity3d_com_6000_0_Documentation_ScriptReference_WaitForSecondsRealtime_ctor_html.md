* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime-ctor.html

# WaitForSecondsRealtime Constructor
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
## Declaration
public WaitForSecondsRealtime(float time); 
### Description
Creates a yield instruction to wait for a given number of seconds using unscaled time.
```
using UnityEngine;
using System.Collections;  
  
public class WaitForSecondsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(Example());
    }  
  
    IEnumerator Example()
    {
        print(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        yield return new WaitForSecondsRealtime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html)(5);
        print(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }
}

```

* * *
