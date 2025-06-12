* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.SetString.html

#  [PlayerPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html).SetString
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
public static void SetString(string key, string value); 
### Description
Sets a single string value for the preference identified by the given key. You can use [PlayerPrefs.GetString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetString.html) to retrieve this value. 
Keep the value at 2 KB or smaller. To store larger amounts of data, write them to a file in `Application.persistentDataPath`.  
  
The following example passes the `KeyName` and `Value` variables to a function called `SetString`. The function uses the `KeyName` variable in `PlayerPrefs.SetString` as an identifier, and `Value` as the contents to store. For example, you could use `PlayerPrefs.SetString` to store the user’s name, like this: `PlayerPrefs.SetString(“CharacterName”, “James”)`  
  
The `GetString` function then uses the same `KeyName` variable to retrieve the value stored in the `PlayerPrefs` data.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void SetString(string KeyName, string Value)
    {
        PlayerPrefs.SetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.SetString.html)(KeyName, Value);
    }  
  
    public string GetString(string KeyName)
    {
        return PlayerPrefs.GetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetString.html)(KeyName);
    }
}

```

* * *
