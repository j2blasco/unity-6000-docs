* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAccelerationEvent.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetAccelerationEvent
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
public static [AccelerationEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AccelerationEvent.html) GetAccelerationEvent(int index); 
### Description
Returns specific acceleration measurement which occurred during last frame. (Does not allocate temporary variables).
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Calculates weighted sum of acceleration measurements which occurred during the last frame
    // Might be handy if you want to get more precise measurements
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) acceleration = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
        for (var i = 0; i < Input.accelerationEventCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-accelerationEventCount.html); ++i)
        {
            AccelerationEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AccelerationEvent.html) accEvent = Input.GetAccelerationEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAccelerationEvent.html)(i);
            acceleration += accEvent.acceleration * accEvent.deltaTime;
        }
        print(acceleration);
    }
}

```

* * *
