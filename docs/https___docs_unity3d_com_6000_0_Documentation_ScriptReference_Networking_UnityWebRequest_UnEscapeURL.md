* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.UnEscapeURL.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).UnEscapeURL
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
public static string UnEscapeURL(string s); 
## Declaration
public static string UnEscapeURL(string s, Encoding e); 
### Parameters
Parameter | Description  
---|---  
s | A string containing escaped characters.  
e | The text encoding to use.  
### Description
Converts URL-friendly escape sequences back to normal text.
Certain text characters have special meanings when present in URLs. If you need to include those characters in URL parameters then you must represent them with escape sequences. This function takes a string containing these escape sequences and converts them back to normal text. See Also: [UnityWebRequest.EscapeURL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.EscapeURL.html).
```
using UnityEngine;
using UnityEngine.Networking;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        string plainName = UnityWebRequest.UnEscapeURL[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.UnEscapeURL.html)("Fish+%26+Chips");
    }
}

```

* * *
