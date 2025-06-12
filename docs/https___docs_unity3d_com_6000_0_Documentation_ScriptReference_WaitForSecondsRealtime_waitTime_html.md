* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime-waitTime.html

#  [WaitForSecondsRealtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html).waitTime
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
waitTime; 
### Description
The given amount of seconds that the yield instruction will wait for.
```
using System.Collections;
using UnityEngine;  
  
public class WaitForSecondsRealtimeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float waitTime = 3;  
  
    WaitForSecondsRealtime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html) waitForSecondsRealtime;  
  
    IEnumerator DoWaitTest()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Start waiting: " + Time.realtimeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartup.html));  
  
        if (waitForSecondsRealtime == null)
            waitForSecondsRealtime = new WaitForSecondsRealtime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html)(waitTime);
        else
            waitForSecondsRealtime.waitTime = waitTime;
        yield return waitForSecondsRealtime;  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("End waiting: " + Time.realtimeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartup.html));
    }  
  
    void OnGUI()
    {
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Start Waiting"))
        {
            StartCoroutine(DoWaitTest());
        }
    }
}

```

* * *
