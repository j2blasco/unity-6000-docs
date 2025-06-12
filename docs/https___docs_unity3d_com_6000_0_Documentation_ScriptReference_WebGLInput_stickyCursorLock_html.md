* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput-stickyCursorLock.html

#  [WebGLInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput.html).stickyCursorLock
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
stickyCursorLock; 
### Description
Set cursor lock behavior to be "sticky" or "unsticky".
Sticky cursor lock means if the browser unlocks the cursor when the user presses the ESC key, the cursor will remain locked in Unity. To match the browser's behavior, this property can be set to false, which will "unstick" the cursor lock and unlock it in Unity as well. The default value for this propery is true.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
#if !UNITY_EDITOR && UNITY_WEBGL
        // disable WebGLInput.stickyCursorLock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput-stickyCursorLock.html) so if the browser unlocks the cursor (with the ESC key) the cursor will unlock in Unity
        WebGLInput.stickyCursorLock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput-stickyCursorLock.html) = false;
#endif
    }
}

```

* * *
