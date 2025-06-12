* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitUntil-ctor.html

# WaitUntil Constructor
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
public WaitUntil(Func<bool> predicate); 
### Parameters
Parameter | Description  
---|---  
predicate | Supplied delegate will be evaluated each frame after [MonoBehaviour.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) and before [MonoBehaviour.LateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.LateUpdate.html) until delegate returns `true`.  
### Description
Initializes a yield instruction with a given delegate to be evaluated.
* * *
## Declaration
public WaitUntil(Func<bool> predicate, TimeSpan timeout, [Unity.Android.Gradle.Manifest.Action](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) onTimeout, [WaitTimeoutMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitTimeoutMode.html) timeoutMode); 
### Parameters
Parameter | Description  
---|---  
predicate | Supplied delegate will be evaluated each frame after [MonoBehaviour.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) and before [MonoBehaviour.LateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.LateUpdate.html) until delegate returns `true`.  
timeout | Maximum time to wait after creation of the instance for the predicate to return `true`.  
onTimeout | The action to perform when the `timeout` is reached. Only performed if the predicate fails to return `true` before the maximum time specified.  
timeoutMode | Mode in which to measure time to determine `timeout`. Real time by default. Can be set to in-game time, which is scaled according to the value of [Time.timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html).  
### Description
Initializes a yield instruction with a given delegate to be evaluated.
```
using UnityEngine;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;  
  
public class WaitUntilExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public bool buttonPressed;  
  
    void Start()
    {
        StartCoroutine(Example());
    }  
  
    IEnumerator Example()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Waiting for button to be pressed...");
        yield return new WaitUntil[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitUntil.html)(() => buttonPressed, TimeSpan.FromSeconds(3), () => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("button was not pressed in time!"));
    }
}

```

* * *
