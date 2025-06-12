* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetKeyUp
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
public static bool GetKeyUp(string name); 
### Description
Returns true during the frame the user releases the key identified by `name`.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
Call this function from the [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) function, since the state gets reset each frame. It will not return true until the user has pressed the key and released it again.  
  
For the list of key identifiers see [Conventional Game Input](https://docs.unity3d.com/6000.0/Documentation/Manual/ConventionalGameInput.html). When dealing with input it is recommended to use [Input.GetAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html) and [Input.GetButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html) instead since it allows end-users to configure the keys.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html)("space"))
        {
            print("Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key was released");
        }
    }
}

```

* * *
## Declaration
public static bool GetKeyUp([KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) key); 
### Description
Returns true during the frame the user releases the key identified by the `key` [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) enum parameter.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            print("space key was released");
        }
    }
}

```

* * *
