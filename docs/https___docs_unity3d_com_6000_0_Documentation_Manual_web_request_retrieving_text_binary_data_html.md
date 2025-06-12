* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-retrieving-text-binary-data.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Interacting with web servers](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request.html)
  * [Common operations: using the HLAPI](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-hlapi.html)
  * Retrieving text or binary data from an HTTP Server (GET)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-hlapi.html)
Common operations: using the HLAPI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-retrieving-texture.html)
Retrieving a Texture from an HTTP Server (GET)
# Retrieving text or binary data from an HTTP Server (GET)
To retrieve simple data such as textual data or binary data from a standard HTTP or HTTPS web server, use the `UnityWebRequest.GET` call. This function takes a single string as an argument, with the string specifying the URL from which data is retrieved.
This function is analogous to the standard WWW constructor:
```
WWW myWww = new WWW("https://www.myserver.com/foo.txt");
// ... is analogous to ...
UnityWebRequest myWr = UnityWebRequest.Get("https://www.myserver.com/foo.txt");

```

## Details
  * This function creates a `UnityWebRequest` and sets the target URL to the string argument. It sets no other custom flags or headers.
  * By default, this function attaches a standard `DownloadHandlerBuffer` to the `UnityWebRequest`. This handler buffers the data received from the server and make it available to your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) when the request is complete.
  * By default, this function attaches no `UploadHandler` to the `UnityWebRequest`. You can attach one manually if you wish.


## Example
```
using UnityEngine;
using System.Collections;
using UnityEngine.Networking;
 
public class MyBehaviour : MonoBehaviour {
    void Start() {
        StartCoroutine(GetText());
    }
 
    IEnumerator GetText() {
        UnityWebRequest www = UnityWebRequest.Get("https://www.my-server.com");
        yield return www.SendWebRequest();
 
        if (www.result != UnityWebRequest.Result.Success) {
            Debug.Log(www.error);
        }
        else {
            // Show results as text
            Debug.Log(www.downloadHandler.text);
 
            // Or retrieve results as binary data
            byte[] results = www.downloadHandler.data;
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-hlapi.html)
Common operations: using the HLAPI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-retrieving-texture.html)
Retrieving a Texture from an HTTP Server (GET)
