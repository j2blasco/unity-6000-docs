* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).Start()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
Start is called on the frame when a script is enabled just before any of the Update methods are called the first time.
Like the [Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) function, Start is called exactly once in the lifetime of the script. Start may not be called on the same frame as [Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) if the script is not enabled at initialisation time.  
  
The [Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) function is called on all objects in the Scene before any object's Start function is called. This fact is useful in cases where object A's initialisation code needs to rely on object B's already being initialised; B's initialisation should be done in [Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html), while A's should be done in Start.  
  
Where objects are instantiated during gameplay, their [Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) function is called after the Start functions of Scene objects have already completed.  
  
The Start function can be defined as a [Coroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html), which allows [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html) to suspend its execution (yield).
```
// Initializes the target variable.
// target is private and thus not editable in the Inspector  
  
// The ExampleClass starts with Awake.  The GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) class has activeSelf
// set to false.  When activeSelf is set to true the Start() and Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
// functions will be called causing the ExampleClass to run.
// Note that ExampleClass (Script) in the Inspector is turned off.  It
// needs to be ticked to make script call Start.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float update;  
  
    void Awake()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Awake");
        update = 0.0f;
    }  
  
    IEnumerator Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Start1");
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(2.5f);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Start2");
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        update += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
        if (update > 1.0f)
        {
            update = 0.0f;
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)");
        }
    }
}

```

* * *
