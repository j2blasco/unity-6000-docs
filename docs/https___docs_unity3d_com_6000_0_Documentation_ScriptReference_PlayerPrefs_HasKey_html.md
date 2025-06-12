* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.HasKey.html

#  [PlayerPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html).HasKey
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
public static bool HasKey(string key); 
### Description
Returns true if the given `key` exists in PlayerPrefs, otherwise returns false.
The following example demonstrates using PlayerPrefs.HasKey in a conditional statement. It prints one message to the console if the conditional statement returns true (if the key does exist in the `PlayerPrefs` data), and a different message if the conditional statement returns false (if the key does not exist in the `PlayerPrefs` data).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void HasKey(string KeyName)
    {
        if (PlayerPrefs.HasKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.HasKey.html)(KeyName))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The key " + KeyName + " exists");
        }
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The key " + KeyName + " does not exist");
    }
}

```

* * *
