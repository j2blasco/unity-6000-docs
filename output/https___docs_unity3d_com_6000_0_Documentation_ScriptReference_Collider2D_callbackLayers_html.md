* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-callbackLayers.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).callbackLayers
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
[LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) callbackLayers; 
### Description
The Layers that this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) will report collision or trigger callbacks for during a contact with another [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).
When a contact occurs between two [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html), each [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) will get a collision or trigger callback. This options allows you to select which layer(s) will produce a callback.  
  
The ability to limit which layers will result in a callback can reduce the complexity of the script inside the callback so that it can safely assume only specific layers will be reported. There is also a performance benefit in not performing callbacks that are not required.  
  
These are all the physics callbacks which are affected by callback layers: 
  * [OnCollisionEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionEnter2D.html)
  * [OnCollisionStay2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionStay2D.html)
  * [OnCollisionExit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionExit2D.html)
  * [OnTriggerEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerEnter2D.html)
  * [OnTriggerStay2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerStay2D.html)
  * [OnTriggerExit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerExit2D.html)


**NOTES** : 
  * This does not control whether the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) will come into contact or not but simply if the resultant callback will happen.
  * Even if all callback layers are selected, only contacts captured via [Collider2D.contactCaptureLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-contactCaptureLayers.html), will be reported.
  * The other [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) involved in any contact callback disabled here will still receive callbacks defined by its own [callbackLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-callbackLayers.html) property.
  * Normally both the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) and the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) it is attached to receive a callback therefore this option controls both those component callbacks.
  * When enabling callback layers where callbacks already exist, those contacts will not be reported as new contacts i.e. there will not be an [OnCollisionEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionEnter2D.html) or [OnTriggerEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerEnter2D.html) callback produced.


Additional resources: [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html).
* * *
