* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.LayerToName.html

#  [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html).LayerToName
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
public static string LayerToName(int layer); 
### Description
Given a layer number, returns the name of the layer as defined in either a Builtin or a User Layer in the [Tags and Layers manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Prints the name of the layer 1  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(LayerMask.LayerToName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.LayerToName.html)(1));
    }
}

```

**Note:** [LayerToName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.LayerToName.html) takes an integer argument. This argument selects the name of Layer and returns it. The layers are listed in the inspector. As an example assume User Layer 13 has a string. This string can be accessed by calling [LayerToName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.LayerToName.html) with the value 2^13, which is 8192.
* * *
