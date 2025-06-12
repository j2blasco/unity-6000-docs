* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput-captureAllKeyboardInput.html

#  [WebGLInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput.html).captureAllKeyboardInput
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
captureAllKeyboardInput; 
### Description
Capture all keyboard inputs.
This property determines whether keyboard inputs are captured by WebGL. If this is enabled (default), all inputs will be received by the WebGL canvas regardless of focus, and other elements in the webpage will not receive keyboard inputs. You need to disable this property if you need inputs to be received by other html input elements.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
#if !UNITY_EDITOR && UNITY_WEBGL
        // disable WebGLInput.captureAllKeyboardInput[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput-captureAllKeyboardInput.html) so elements in web page can handle keyboard inputs
        WebGLInput.captureAllKeyboardInput[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLInput-captureAllKeyboardInput.html) = false;
#endif
    }
}

```

* * *
