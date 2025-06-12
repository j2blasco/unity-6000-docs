* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput-mobileKeyboardSupport.html

#  [WebGLInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput.html).mobileKeyboardSupport
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
mobileKeyboardSupport; 
### Description
Enable mobile keyboard support for UI input fields.
This property determines whether to enable mobile keyboard support for UI input fields. If this is enabled (default), the browser's soft keyboard will be requested when selecting an input field, and may impose some overhead to touch down and up events.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
#if !UNITY_EDITOR && UNITY_WEBGL
        // disable WebGLInput.mobileKeyboardSupport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput-mobileKeyboardSupport.html) so the built-in mobile keyboard support is disabled.
        WebGLInput.mobileKeyboardSupport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput-mobileKeyboardSupport.html) = false;
#endif
    }
}

```

* * *
