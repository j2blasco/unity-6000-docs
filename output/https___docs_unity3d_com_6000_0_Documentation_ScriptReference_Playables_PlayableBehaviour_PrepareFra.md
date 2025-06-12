* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.PrepareFrame.html

#  [PlayableBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html).PrepareFrame
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
public void PrepareFrame([Playables.Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) playable, [Playables.FrameData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html) info); 
### Parameters
Parameter | Description  
---|---  
playable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) that owns the current PlayableBehaviour.  
info | A [FrameData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html) structure that contains information about the current frame context.  
### Description
This function is called during the PrepareFrame phase of the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).
PrepareFrame should be used to do topological modifications, change connection weights, time changes , etc.
* * *
