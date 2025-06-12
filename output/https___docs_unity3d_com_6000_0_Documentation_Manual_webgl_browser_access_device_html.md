* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-browser-access-device.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * Web browser access to device features


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-canvas-size.html)
Configure a Web Canvas size
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-networking.html)
Web networking
# Web browser access to device features
The Unity Web platform supports [WebCam access](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamDevice.html). To allow a Web application to access the webcam on a device, the browser must request its user to provide access to the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). Without the permission to access the camera, the browser returns incomplete or inaccurate information.
**Note:** Currently, the Web platform supports WebCam devices only.
To request browser permission to access the webcam, use the `Application.RequestUserAuthorization` API:
```
using UnityEngine;
using UnityEngine.iOS;
using System.Collections;

// Get WebCam information from the browser
public class ExampleClass : MonoBehaviour
{
    private WebCamDevice[] devices;
    
    // Use this for initialization
    IEnumerator Start()
    {
        yield return Application.RequestUserAuthorization(UserAuthorization.WebCam);
        if (Application.HasUserAuthorization(UserAuthorization.WebCam))
        {
            Debug.Log("webcam found");
            devices = WebCamTexture.devices;
            for (int cameraIndex = 0; cameraIndex < devices.Length; ++cameraIndex)
            {
                Debug.Log("devices[cameraIndex].name: ");
                Debug.Log(devices[cameraIndex].name);
                Debug.Log("devices[cameraIndex].isFrontFacing");
                Debug.Log(devices[cameraIndex].isFrontFacing);
            }
        }
        else
        {
            Debug.Log("no webcams found");
        }
    }
}

```

**Note:** Unity recommends to use the `MediaDevices.getUserMedia()` API to request user permission for accessing the device. This feature is available only in secure contexts (HTTPS).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-canvas-size.html)
Configure a Web Canvas size
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-networking.html)
Web networking
