* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.EscapeURL.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).EscapeURL
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
public static string EscapeURL(string s); 
## Declaration
public static string EscapeURL(string s, Encoding e); 
### Parameters
Parameter | Description  
---|---  
s | A string with characters to be escaped.  
e | The text encoding to use.  
### Description
Escapes characters in a string to ensure they are URL-friendly.
Certain text characters have special meanings when present in URLs. If you need to include those characters in URL parameters then you must represent them with escape sequences. It is recommended that you use this function on any text supplied by a user before passing the text as a URL parameter. This will ensure that a malicious user can't manipulate the contents of the URL to attack the webserver. See Also: [UnityWebRequest.UnEscapeURL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.UnEscapeURL.html).
```
using UnityEngine;
using UnityEngine.Networking;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        string escName = UnityWebRequest.EscapeURL[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.EscapeURL.html)("Fish & Chips");
    }
}

```

* * *
