* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).timeScale
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
timeScale; 
### Description
The scale at which time passes.
This can be used for slow motion effects or to speed up your application. When timeScale is 1.0, time passes as fast as real time. When timeScale is 0.5 time passes 2x slower than realtime.  
  
When timeScale is set to zero your application acts as if paused if all your functions are frame rate independent. Negative values are ignored.  
  
Note that changing the timeScale only takes effect on the following frames. How often [MonoBehaviour.FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) is executed per frame depends on the timeScale. Therefore, to keep the number of FixedUpdate callbacks per frame constant, you must also multiply [Time.fixedDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html) by timeScale. Whether this adjustment is desirable is game-specific.  
  
FixedUpdate functions and suspended Coroutines with [WaitForSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html) are not called when timeScale is set to zero. 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Toggles the time scale between 1 and 0.7
    // whenever the user hits the Fire1 button.  
  
    private float fixedDeltaTime;  
  
    void Awake()
    {
        // Make a copy of the fixedDeltaTime, it defaults to 0.02f, but it can be changed in the editor
        this.fixedDeltaTime = Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html)("Fire1"))
        {
            if (Time.timeScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) == 1.0f)
                Time.timeScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) = 0.7f;
            else
                Time.timeScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) = 1.0f;
            // Adjust fixed delta time according to timescale
            // The fixed delta time will now be 0.02 real-time seconds per frame
            Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html) = this.fixedDeltaTime * Time.timeScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html);
        }
    }
}

```

* * *
