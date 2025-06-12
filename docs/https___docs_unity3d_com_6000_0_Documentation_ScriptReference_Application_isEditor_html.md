* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isEditor.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).isEditor
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
isEditor; 
### Description
Whether the game is running inside the Unity Editor (Read Only).
Returns true if the game is being run from the Unity Editor; false if run from any deployment target.
```
using UnityEngine;  
  
class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (Application.isEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isEditor.html))
        {
            print("We are running this from inside of the editor!");
        }
    }
}

```

* * *
