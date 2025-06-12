* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.CanStreamedLevelBeLoaded.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).CanStreamedLevelBeLoaded
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
public static bool CanStreamedLevelBeLoaded(int levelIndex); 
### Description
Checks if the streamed level can be loaded.
Additional resources: [GetStreamProgressForLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.GetStreamProgressForLevel.html) function.
```
// Check if level at index 1 can be loaded.
// If it can be loaded then load it.
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;  
  
public class SampleBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (Application.CanStreamedLevelBeLoaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.CanStreamedLevelBeLoaded.html)(1))
        {
            Application.LoadLevel(1);
        }
    }
}

```

* * *
## Declaration
public static bool CanStreamedLevelBeLoaded(string levelName); 
### Description
Checks if the streamed level can be loaded.
Additional resources: [GetStreamProgressForLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.GetStreamProgressForLevel.html) function.
```
// Check if "Level1" can be loaded, if it can be loaded then load it.
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;  
  
public class SampleBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (Application.CanStreamedLevelBeLoaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.CanStreamedLevelBeLoaded.html)("Level1"))
        {
            Application.LoadLevel("Level1");
        }
    }
}

```

* * *
