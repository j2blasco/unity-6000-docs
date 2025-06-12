* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-timeout.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).timeout
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
timeout; 
### Description
The number of seconds after which UnityWebRequest attempts to abort the request if no response is received.
The default value is `0` which means no timeout is applied and UnityWebRequest will wait until the response is received.  
  
When the response takes longer than the value specified in `timeout`, [UnityWebRequest.error](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-error.html) returns `Request timeout` message.
```
using UnityEngine;
using System.Collections;
using UnityEngine.Networking;  
  
// Ask the website to deliver an image that is very large.
// Set the download to take more than 60 seconds. This causes
// the "request timeout" error message.  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(GetText());
    }  
  
    IEnumerator GetText()
    {
        using UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) www = UnityWebRequest.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html)("https://my-website.com/verylargeimage.jpg");  
  
        // Set the timeout to 60 seconds.
        // Abort the request if the image doesn't download within the specified timeout.
        www.timeout = 60;
        yield return www.SendWebRequest();  
  
        if (www.result != UnityWebRequest.Result.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.Success.html))
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)(www.error);
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("image arrived");
        }
    }
}

```

* * *
