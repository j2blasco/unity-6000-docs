* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.html

# PlayableOutputExtensions
class in UnityEngine.Playables
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Extensions for all the types that implements [IPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayableOutput.html).
Extension methods are static methods that can be called as if they were instance methods on the extended type.
```
using UnityEngine;
using UnityEngine.Playables;  
  
public class ExamplePlayableBehaviour : PlayableBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html)
{
    void Start()
    {
        PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)();
        ScriptPlayableOutput[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.html) scriptOutput = ScriptPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.Create.html)(graph, "MyOutput");  
  
        // Calling method PlayableExtensions.SetWeight on ScriptPlayableOutput[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.html) as if it was an instance method.
        scriptOutput.SetWeight(10);  
  
        // The line above is the same as calling directly PlayableExtensions.SetDuration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetDuration.html), but it is more compact and readable.
        PlayableOutputExtensions.SetWeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.SetWeight.html)(scriptOutput, 10);
    }
}

```

### Static Methods
Method | Description  
---|---  
[AddNotificationReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.AddNotificationReceiver.html) | Registers a new receiver that listens for notifications.  
[GetNotificationReceivers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.GetNotificationReceivers.html) | Retrieves the list of notification receivers currently registered on the output.  
[GetSourceOutputPort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.GetSourceOutputPort.html) | Returns the source playable's output connection index.  
[GetSourcePlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.GetSourcePlayable.html) | Returns the source playable.  
[GetUserData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.GetUserData.html) | Returns the opaque user data. This is the same value as the last last argument of ProcessFrame.  
[GetWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.GetWeight.html) | Returns the weight of the connection from the PlayableOutput to the source playable.  
[IsOutputNull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.IsOutputNull.html) | Returns true if the PlayableOutput is null, false otherwise.  
[IsOutputValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.IsOutputValid.html) |   
[PushNotification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.PushNotification.html) | Queues a notification to be sent through the Playable system.  
[RemoveNotificationReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.RemoveNotificationReceiver.html) | Unregisters a receiver on the output.  
[SetReferenceObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.SetReferenceObject.html) | Sets the bound object to a new value. Used to associate an output to an object (Track asset in case of Timeline).  
[SetSourcePlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.SetSourcePlayable.html) | Sets which playable that computes the output and which sub-tree index.  
[SetUserData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.SetUserData.html) | Sets the opaque user data. This same data is passed as the last argument to ProcessFrame.  
[SetWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.SetWeight.html) | Sets the weight of the connection from the PlayableOutput to the source playable.  
* * *
