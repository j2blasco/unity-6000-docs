* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-retrieving-texture.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Interacting with web servers](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request.html)
  * [Common operations: using the HLAPI](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-hlapi.html)
  * Retrieving a Texture from an HTTP Server (GET)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-retrieving-text-binary-data.html)
Retrieving text or binary data from an HTTP Server (GET)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-downloading-asset-bundle.html)
Downloading an AssetBundle from an HTTP server (GET)
# Retrieving a Texture from an HTTP Server (GET)
To retrieve a Texture file from a remote server, you can use `UnityWebRequestTexture.GetTexture`. This function is very similar to `UnityWebRequest.Get`, but is optimized for downloading and storing textures efficiently.
`UnityWebRequestTexture.GetTexture` takes a string or `Uri` object as an argument that specifies a URL of an image file to download and use as a Texture. Additionally, it can take `DownloadedTextureParams` as second argument, allowing you more control over the texture that will be created.
## Details
  * This function creates a `UnityWebRequest` and sets the target URL to the string argument. This function sets no other flags or custom headers.
  * This function attaches a `DownloadHandlerTexture` object to the `UnityWebRequest`. DownloadHandlerTexture is a specialized Download Handler which is optimized for storing images which are to be used as Textures in the Unity Engine. Using this class significantly reduces memory reallocation compared with downloading raw bytes and creating a Texture manually in script.
  * By default, this function does not attach an Upload Handler. You can add one manually if you wish.


## Example
```
using UnityEngine;
using System.Collections;
using UnityEngine.Networking;
 
public class MyBehaviour : MonoBehaviour {
    void Start() {
        StartCoroutine(GetTexture());
    }
 
    IEnumerator GetTexture() {
        UnityWebRequest www = UnityWebRequestTexture.GetTexture("https://www.my-server.com/image.png");
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success) {
            Debug.Log(www.error);
        }
        else {
            Texture myTexture = DownloadHandlerTexture.GetContent(www);
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-retrieving-text-binary-data.html)
Retrieving text or binary data from an HTTP Server (GET)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-downloading-asset-bundle.html)
Downloading an AssetBundle from an HTTP server (GET)
