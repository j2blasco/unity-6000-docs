* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-llapi.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Interacting with web servers](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request.html)
  * Advanced operations: Using the LLAPI


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-uploading-raw-data.html)
Uploading raw data to an HTTP server (PUT)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-unity-web-requests.html)
Creating UnityWebRequests
# Advanced operations: Using the LLAPI
While the HLAPI is designed to minimize boilerplate code, the Low-Level API (LLAPI) is designed to permit maximum flexibility. In general, using the LLAPI involves creating UnityWebRequests then creating appropriate `DownloadHandlers` or `UploadHandlers`and attaching them to your `UnityWebRequests`.
This section details the options available in the Low-Level API and the scenarios they’re intended to address:
  * [Creating UnityWebRequests](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-unity-web-requests.html)
  * [Creating UploadHandlers](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-upload-handlers.html)
  * [Creating DownloadHandlers](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-download-handlers.html)


Note that the HLAPI and LLAPI aren’t mutually exclusive. You can always customize UnityWebRequest objects created via the HLAPI if you need to tweak a common scenario.
For full details on each of the objects described in this section, please refer to the Unity Scripting API.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-uploading-raw-data.html)
Uploading raw data to an HTTP server (PUT)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-unity-web-requests.html)
Creating UnityWebRequests
