* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.GetGroups.html

#  [TextureMipmapLimitGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html).GetGroups
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
public static string[] GetGroups(); 
### Returns
**string[]** String array of texture mipmap limit group names. 
### Description
Retrieves a string array containing the name of all texture mipmap limit groups available in the project.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Writes the name of all texture mipmap limit groups available in the project to the Unity Console.
    void Start()
    {
        string[] textureMipmapLimitGroupNames = TextureMipmapLimitGroups.GetGroups[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.GetGroups.html)();  
  
        if (textureMipmapLimitGroupNames.Length == 0)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No texture mipmap limit groups have been created in this project.");
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(string.Join(" -- ", textureMipmapLimitGroupNames));
        }
    }
}

```

Additional resources: [RemoveGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.RemoveGroup.html).
* * *
