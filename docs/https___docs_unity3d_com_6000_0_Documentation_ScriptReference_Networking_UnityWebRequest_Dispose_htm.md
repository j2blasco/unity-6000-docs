* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Dispose.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).Dispose
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
public void Dispose(); 
### Description
Signals that this [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) is no longer being used, and should clean up any resources it is using.
You must call Dispose once you have finished using a [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) object, regardless of whether the request succeeded or failed.  
  
For safety, it is usually a best practice to employ the [using statement](https://msdn.microsoft.com/en-us/library/yh598w02.aspx) to ensure that a [UnityWebRequest] is properly cleaned up in case of uncaught exceptions.
```
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class MyExampleBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public IEnumerator Start()
    {
        using (UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) request = UnityWebRequest.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html)("https://my-website.com"))
        {
            yield return request.SendWebRequest();
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Server responded: " + request.downloadHandler.text);
        }
    }
}

```

* * *
