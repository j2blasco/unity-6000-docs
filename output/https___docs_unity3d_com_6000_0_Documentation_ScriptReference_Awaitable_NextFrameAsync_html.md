* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.NextFrameAsync.html

#  [Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html).NextFrameAsync
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
public static [Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html) NextFrameAsync(CancellationToken cancellationToken); 
### Parameters
Parameter | Description  
---|---  
cancellationToken | Optional cancellation token.  
### Description
Resumes execution on the next frame.
**Note:** This method can only be called from the main thread and always completes on main thread.
```
async Awaitable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html) SampleSchedulingJobsForNextFrame()
{
    // Wait until end of frame to avoid competing over resources with other Unity subsystems
    await Awaitable.EndOfFrameAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.EndOfFrameAsync.html)();
    var jobHandle = ScheduleSomethingWithJobSystem();
    // Let the job execute while the next frame starts
    await Awaitable.NextFrameAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.NextFrameAsync.html)();
    jobHandle.Complete();
    // Use results of computation
}  
  
JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) ScheduleSomethingWithJobSystem()
{
    ...
}

```

* * *
