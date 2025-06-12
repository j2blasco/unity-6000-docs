* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-devices.html

#  [WebCamTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html).devices
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
devices; 
### Description
Return a list of available devices.
This queries the system for the list of devices connected and it can be slow. You should cache this value by keeping a copy of the result if you want to use it repeatedly.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Gets the list of devices and prints them to the console.
    void Start()
    {
        WebCamDevice[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamDevice.html)[] devices = WebCamTexture.devices[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-devices.html);
        for (int i = 0; i < devices.Length; i++)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(devices[i].name);
    }
}

```

* * *
