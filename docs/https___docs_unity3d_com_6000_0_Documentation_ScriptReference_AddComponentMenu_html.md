* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu.html

# AddComponentMenu
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
The AddComponentMenu attribute allows you to place a script anywhere in the "Component" menu, instead of just the "Component->Scripts" menu.
You can use this to organize the Component menu better and improve the workflow of adding scripts.
```
using UnityEngine;  
  
[AddComponentMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu.html)("Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)/Follow Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)")]
public class FollowTransform : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
}

```

### Properties
Property | Description  
---|---  
[componentOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu-componentOrder.html) | The order of the component in the component menu (lower values appear higher in the menu).  
### Constructors
Constructor | Description  
---|---  
[AddComponentMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu-ctor.html) | Add an item in the Component menu.  
* * *
