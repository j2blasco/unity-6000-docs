* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-hasChanged.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).hasChanged
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
hasChanged; 
### Description
Has the transform changed since the last time the flag was set to 'false'?
A change to the transform can be anything that can cause its matrix to be recalculated: any adjustment to its position, rotation or scale. Note that operations which can change the transform will not actually check if the old and new value are different before setting this flag. So setting, for instance, transform.position will always set hasChanged on the transform, regardless of there being any actual change.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (transform.hasChanged)
        {
            print("The transform has changed!");
            transform.hasChanged = false;
        }
    }
}

```

* * *
