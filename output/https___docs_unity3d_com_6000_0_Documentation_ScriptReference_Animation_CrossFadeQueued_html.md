* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.CrossFadeQueued.html

#  [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html).CrossFadeQueued
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animation.html "Go to Animation Component in the Manual")
## Declaration
public [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html) CrossFadeQueued(string animation, float fadeLength = 0.3F, [QueueMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueueMode.html) queue = QueueMode.CompleteOthers, [PlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html) mode = PlayMode.StopSameLayer); 
### Description
Cross fades an animation after previous animations has finished playing.
For example you might play a specific sequence of animations after each other.  
  
The animation duplicates itself before playing thus you can fade between the same animation. This can be used to overlay two same animations. For example you might have a sword swing animation. The player slashes two times quickly after each other. You could rewind the animation and play from the beginning but then you will get a jump in the animation.  
  
The following [queue modes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueueMode.html) are available:   
If `queue` is [QueueMode.CompleteOthers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueueMode.CompleteOthers.html) this animation will only start once all other animations have stopped playing.   
If `queue` is [QueueMode.PlayNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueueMode.PlayNow.html) this animation will start playing immediately on a duplicated animation state.  
  
After the animation has finished playing it will automatically clean itself up. Using the duplicated animation state after it has finished will result in an exception.  
  

* * *
