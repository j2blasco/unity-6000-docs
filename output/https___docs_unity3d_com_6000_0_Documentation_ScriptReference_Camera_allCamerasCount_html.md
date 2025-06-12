* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-allCamerasCount.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).allCamerasCount
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
allCamerasCount; 
### Description
The number of cameras in the current Scene.
Returns the size of the array that [Camera.allCameras](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-allCameras.html) returns and the amount of cameras that [Camera.GetAllCameras](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetAllCameras.html) will fill.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private int count;  
  
    void Start()
    {
        count = Camera.allCamerasCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-allCamerasCount.html);
        print("We've got " + count + " cameras");
    }
}

```

* * *
