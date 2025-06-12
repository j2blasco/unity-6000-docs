* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap-format.html

#  [Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html).format
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
[TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) format; 
### Description
The format of the pixel data in the texture (Read Only).
Use this to determine the format of the texture.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Print the format of a given cubemap.
    public Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) cubeMap;  
  
    void Start()
    {
        if (cubeMap != null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(cubeMap.format);
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No cubemap was assigned, please assing one on the inspector.");
        }
    }
}

```

* * *
