* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-deviceName.html

#  [WebCamTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html).deviceName
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
deviceName; 
### Description
Set this to specify the name of the device to use.
This only has an effect when set while the camera is not running.  
  
Note: if you want to use WebCamTexture to get the camera stream from device connected through Unity Remote, then you must initalize it through the constructor. It's not possible to change device using [WebCamTexture.deviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-deviceName.html) from regular devices to remote devices and vice versa.
```
// Sets the device of the WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html) to the first one available and starts playing it
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        WebCamDevice[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamDevice.html)[] devices = WebCamTexture.devices[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-devices.html);
        WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html) webcamTexture = new WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html)();  
  
        if (devices.Length > 0)
        {
            webcamTexture.deviceName = devices[0].name;
            webcamTexture.Play();
        }
    }
}

```

* * *
