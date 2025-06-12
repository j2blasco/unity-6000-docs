* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).Get
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
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) Get(string uri); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) Get(Uri uri); 
### Parameters
Parameter | Description  
---|---  
uri | The URI of the resource to retrieve via HTTP GET.  
### Returns
**UnityWebRequest** An object that retrieves data from the uri. 
### Description
Create a UnityWebRequest for HTTP GET.
Use the method to create a [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html). Set the target URL to the `uri` with a `string` or `Uri` argument. No custom flags or headers are set.
```
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
// UnityWebRequest.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html) example  
  
// Access a website and use UnityWebRequest.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html) to download a page.
// Also try to download a non-existing page. Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the error.  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // A correct website page.
        StartCoroutine(GetRequest("https://www.example.com"));  
  
        // A non-existing page.
        StartCoroutine(GetRequest("https://error.html"));
    }  
  
    IEnumerator GetRequest(string uri)
    {
        using (UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) webRequest = UnityWebRequest.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html)(uri))
        {
            // Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.html) and wait for the desired page.
            yield return webRequest.SendWebRequest();  
  
            string[] pages = uri.Split('/');
            int page = pages.Length - 1;  
  
            switch (webRequest.result)
            {
                case UnityWebRequest.Result.ConnectionError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.ConnectionError.html):
                case UnityWebRequest.Result.DataProcessingError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.DataProcessingError.html):
                    Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)(pages[page] + ": Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html): " + webRequest.error);
                    break;
                case UnityWebRequest.Result.ProtocolError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.ProtocolError.html):
                    Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)(pages[page] + ": HTTP Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html): " + webRequest.error);
                    break;
                case UnityWebRequest.Result.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.Success.html):
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(pages[page] + ":\nReceived: " + webRequest.downloadHandler.text);
                    break;
            }
        }
    }
}

```

* * *
