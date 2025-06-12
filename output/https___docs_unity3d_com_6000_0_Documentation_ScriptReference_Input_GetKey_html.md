* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetKey
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
public static bool GetKey(string name); 
### Description
Returns true while the user holds down the key identified by `name`.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
[GetKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html) will report the status of the named key. This might be used to confirm a key is used for auto fire. For the list of key identifiers see [Input Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/ConventionalGameInput.html). When dealing with input it is recommended to use Input.GetAxis and Input.GetButton instead since it allows end-users to configure the keys.  
  
**iOS, tvOS** : Due platform limitations, [GetKeyUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html) event for keyboard events is delayed by about half a second, see UnityView+Keyboard.mm in the generated Xcode project for more information.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)("up"))
        {
            print("up arrow key is held down");
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)("down"))
        {
            print("down arrow key is held down");
        }
    }
}

```

* * *
## Declaration
public static bool GetKey([KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) key); 
### Description
Returns true while the user holds down the key identified by the `key` [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) enum parameter.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.UpArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.UpArrow.html)))
        {
            print("up arrow key is held down");
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.DownArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.DownArrow.html)))
        {
            print("down arrow key is held down");
        }
    }
}

```

* * *
