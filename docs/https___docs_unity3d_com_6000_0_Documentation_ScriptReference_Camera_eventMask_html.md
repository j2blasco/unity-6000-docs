* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-eventMask.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).eventMask
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
eventMask; 
### Description
Mask to select which layers can trigger events on the camera.
Just as the camera's `cullingMask` determines if the camera is able to see the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), the event mask determines whether the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is able to receive mouse events. Only objects visible by the camera and whose `layerMask` overlaps with the camera's `eventMask` will be able to receive OnMouseXXX events. Setting this mask to zero will improve performance and is recommended if you don't use OnMouseXXX events. See [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) for more information.  
  
Additional resources: [MonoBehaviour.OnMouseEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseEnter.html), [MonoBehaviour.OnMouseExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseExit.html), [MonoBehaviour.OnMouseOver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseOver.html), [MonoBehaviour.OnMouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseDown.html), [MonoBehaviour.OnMouseOver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseOver.html), [MonoBehaviour.OnMouseUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseUp.html), [MonoBehaviour.OnMouseDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseDrag.html), [MonoBehaviour.OnMouseUpAsButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseUpAsButton.html).
* * *
