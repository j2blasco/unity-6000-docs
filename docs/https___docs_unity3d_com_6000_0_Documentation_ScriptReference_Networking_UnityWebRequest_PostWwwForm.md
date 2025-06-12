* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.PostWwwForm.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).PostWwwForm
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
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) PostWwwForm(string uri, string form); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) PostWwwForm(Uri uri, string form); 
### Parameters
Parameter | Description  
---|---  
uri | The target URI to which form data will be transmitted.  
form | An HTML form to send.  
### Returns
**UnityWebRequest** A UnityWebRequest configured to send form data to `uri` via `POST`. 
### Description
Creates a UnityWebRequest configured to send form data to a server via HTTP `POST`.
This method creates a UnityWebRequest, sets the `uri` and sets the method to `POST`. The `Content-Type` header will be set to `application/x-www-form-urlencoded` by default.  
  
This method attaches a [DownloadHandlerBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerBuffer.html) to the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html). This is for convenience, as we anticipate most users will use the [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) to check replies from the server, particularly in the case of REST APIs.  
  
The string in the `form` parameter is expected to be a preformatted HTML form. It will be escaped and sent as UTF-8 string.
```
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class MyBehavior : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(Upload());
    }  
  
    IEnumerator Upload()
    {
        using (UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) www = UnityWebRequest.PostWwwForm[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.PostWwwForm.html)("https://www.my-server.com/myapi", "field1=1&field2=value2"))
        {
            yield return www.SendWebRequest();  
  
            if (www.result != UnityWebRequest.Result.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.Success.html))
            {
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)(www.error);
            }
            else
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Form upload complete!");
            }
        }
    }
}

```

* * *
