* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-invokeCollisionCallbacks.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).invokeCollisionCallbacks
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
invokeCollisionCallbacks; 
### Description
Whether or not [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) collision messages will be sent by the physics system.
If this property is set to `true`, [OnCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionEnter.html), [OnCollisionStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionStay.html), and [OnCollisionExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionExit.html) messages will be sent to the corresponding scripts that have these methods implemented.  
  
If this property is set to `false`, no [OnCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionEnter.html), [OnCollisionStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionStay.html), or [OnCollisionExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionExit.html) messages will be sent. This can be beneficial when only the [Physics.ContactEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ContactEvent.html) is used to read contacts as this will stop the physics system from iterating simulation results.  
  
Note: This does not affect trigger events.
* * *
