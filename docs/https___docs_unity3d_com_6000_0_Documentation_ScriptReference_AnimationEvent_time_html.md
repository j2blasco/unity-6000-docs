* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-time.html

#  [AnimationEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent.html).time
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
time; 
### Description
The time at which the event will be fired off.
The [AnimationEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent.html) obtains the clip length from its attached clip. The time property determines when the event is processed. For example, if the clip length is 2s and `time` is set to 1.5f, then the function is called 1.5s after the animation starts, and then every 2s. The example on the [AnimationEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent.html) page shows how to use the `time` property.
* * *
