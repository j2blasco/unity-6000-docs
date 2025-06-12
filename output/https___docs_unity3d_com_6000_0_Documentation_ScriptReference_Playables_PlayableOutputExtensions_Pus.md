* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.PushNotification.html

#  [PlayableOutputExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.html).PushNotification
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
public static void PushNotification(U output, [Playables.Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) origin, [Playables.INotification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.INotification.html) notification, object context); 
### Parameters
Parameter | Description  
---|---  
output | The output sending the notification.  
origin | The originating playable of the notification.  
notification | The notification to be sent.  
context | Extra information about the state when the notification was fired.  
### Description
Queues a notification to be sent through the Playable system.
```
using UnityEngine;
using UnityEngine.Playables;
class ExamplePlayableBehaviour : PlayableBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html)
{
    private static readonly Notification[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Notification.html) s_BlendNotification = new Notification[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Notification.html)("BlendComplete");
    private float m_lastWeight = 0;  
  
    public override void PrepareFrame(Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) playable, FrameData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html) info)
    {
        if (m_lastWeight < 1 && info.effectiveWeight == 1)
        {
            info.output.PushNotification(playable, s_BlendNotification, m_lastWeight);
        }
        m_lastWeight = info.effectiveWeight;
    }
}

```

* * *
