* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogColor.html

#  [RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings.html).fogColor
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) fogColor; 
### Description
The color of the fog.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        // Set the fog color to be blue
        RenderSettings.fogColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogColor.html) = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);  
  
        // And enable fog
        RenderSettings.fog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fog.html) = true;
    }
}

```

* * *
