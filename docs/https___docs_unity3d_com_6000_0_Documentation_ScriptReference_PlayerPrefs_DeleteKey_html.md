* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.DeleteKey.html

#  [PlayerPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html).DeleteKey
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
public static void DeleteKey(string key); 
### Description
Removes the given `key` from the PlayerPrefs. If the key does not exist, [DeleteKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.DeleteKey.html) has no impact.
The following example shows a public function called ‘DeleteKey’. The function takes a string variable called ‘KeyName’ as a parameter, which PlayerPrefs.DeleteKey uses to delete the key from the registry.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void DeleteKey(string KeyName)
    {
        PlayerPrefs.DeleteKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.DeleteKey.html)(KeyName);
    }
}

```

* * *
