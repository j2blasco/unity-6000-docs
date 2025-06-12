* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticBatchingUtility.html

# StaticBatchingUtility
class in UnityEngine
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
StaticBatchingUtility can prepare your objects to take advantage of Unity's static batching.
This step is useful as a performance optimization allowing engine to reduce number of draw-calls dramatically, but keep amount of rendered geometry intact.  
  
By calling one of the Combine methods you will create an internal mesh which will contain combined geometry, however each original GameObject will be present in the Scene and will be culled individually. The fact that GameObjects can be culled individually allows run-time to render the same amount of geometry as it would without batching, unlike combining geometry in the modeling tool. Combining geometry in the modeling tool prevents efficient culling and results in much higher amount of geometry being rendered.  
  
Note that you do not need to call Combine methods on objects which were already marked as "Static" in the Editor. They will be prepared for static batching automatically during the Build Player step.  
  
**IMPORTANT:** only objects with the same material can be batched, thus it is useful to share as many textures/material as you can.
### Static Methods
Method | Description  
---|---  
[Combine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticBatchingUtility.Combine.html) | Combines all children GameObjects of the staticBatchRoot for static batching.  
* * *
