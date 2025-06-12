* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PIX.IsAttached.html

#  [PIX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PIX.html).IsAttached
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
## Declaration
public static bool IsAttached(); 
### Description
Returns true if running via PIX and in a development build.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class PixControl : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int frameCaptureCount = 1;  
  
    int frameCount = 0;
    bool capturing = false;  
  
    void Awake()
    {
        if (PIX.IsAttached[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PIX.IsAttached.html)())
        {
            PIX.BeginGPUCapture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PIX.BeginGPUCapture.html)();
            capturing = true;
        }
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (frameCount > frameCaptureCount && capturing)
        {
            PIX.EndGPUCapture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PIX.EndGPUCapture.html)();
            capturing = false;
        }  
  
        frameCount++;
    }
}

```

* * *
