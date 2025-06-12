* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent.html

# CullingGroupEvent
struct in UnityEngine
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
Provides information about the current and previous states of one sphere in a CullingGroup.
Additional resources: [CullingGroup.onStateChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup-onStateChanged.html).
### Properties
Property | Description  
---|---  
[currentDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent-currentDistance.html) | The current distance band index of the sphere, after the most recent culling pass.  
[hasBecomeInvisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent-hasBecomeInvisible.html) | Did this sphere change from being visible to being invisible in the most recent culling pass?  
[hasBecomeVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent-hasBecomeVisible.html) | Did this sphere change from being invisible to being visible in the most recent culling pass?  
[index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent-index.html) | The index of the sphere that has changed.  
[isVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent-isVisible.html) | Was the sphere considered visible by the most recent culling pass?  
[previousDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent-previousDistance.html) | The distance band index of the sphere before the most recent culling pass.  
[wasVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent-wasVisible.html) | Was the sphere visible before the most recent culling pass?  
* * *
