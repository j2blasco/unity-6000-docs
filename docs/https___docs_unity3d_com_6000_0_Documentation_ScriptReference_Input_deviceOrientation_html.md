* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-deviceOrientation.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).deviceOrientation
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
[DeviceOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceOrientation.html) deviceOrientation; 
### Description
Device physical orientation as reported by OS. (Read Only)
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Start()
    {
        audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.deviceOrientation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-deviceOrientation.html) == DeviceOrientation.FaceDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceOrientation.FaceDown.html))
            audioSource.Play();
    }
}

```

* * *
